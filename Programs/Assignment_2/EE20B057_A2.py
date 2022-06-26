"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 2
"""

#importing required modules
from cmath import nan
from pickle import NONE
import sys
import numpy as np
import math as ma

#setting variables to identify the start and end of circuit discription
CIRCUIT = '.circuit'
END = '.end'
AC = '.ac'

#initializing start and end variables to store the indices of starting and ending of circuit discription
start = 7
end = 5

#checking for number of input files given to the program
if (len(sys.argv) != 2):
    print('Please type in a single valid netlist file.')
    exit()

#checking for a valid netlist file
if (not sys.argv[1].endswith('.netlist')):
    print('Please type in a valid netlist file.')
    exit()

#defining class for passive elements
class passive_element:

    def __init__ (self, def_list):
        self.name = def_list[0]                 
        self.from_n = def_list[1]
        self.to_n = def_list[2]
    
    value = 0

    
#defining class for independent sources
class ind_source:
    
    def __init__ (self, def_list):
        self.name = def_list[0]
        self.from_n = def_list[1]
        self.to_n = def_list[2]
    
    p_p = 0
    freq = 0
    phase = 0
    value = 0

#defining class for voltage controlled source
class voltage_control_element:
    
    def __init__ (self, def_list):
        self.name = def_list[0]
        self.from_n = def_list[1]
        self.to_n = def_list[2]
        self.vc_n_1 = def_list[3]
        self.vc_n_2 = def_list[4]
    
    value = 0

#defining class for current controlled source
class current_control_element:

    def __init__ (self, def_list):
        self.name = def_list[0]
        self.from_n = def_list[1]
        self.to_n = def_list[2]
        self.volt_source = def_list[3]
    
    value = 0


#reading the available netlist file and printing error otherwise
try:
    with open(sys.argv[1]) as main:

        #creating variables which will be used in the later part of the code
        element_list = []                   #to be used to store each line from the parsed lines
        no_nodes = NONE                     #number of nodes
        ac_flag = 0                         #check for ac or dc circuit
        ac_freq = 0                         #stores ac frequency
        list_variables = []                 #stores the variables which are to be evaluated in the circuit
        volt_dict = {}                      #stores the row/colomn number of the current corresponding to the voltage key
        node_dict = {}                      #stores the key:node to the value:number alloted to it for filling in i_matrix
        node_dict['GND'] = 0                #setting 'GND' key to 0 value in the node dictionary

        #breaking the main file into a list of lines
        main_lines = main.readlines()

        #giving values to start and end variables and setting ac_flag for ac circuits
        for line in main_lines:
            if (CIRCUIT == line[:len(CIRCUIT)]):
                start = main_lines.index(line)
            if (END == line[:len(END)]):
                end = main_lines.index(line)
            if (AC == line[:len(AC)]):
                ac_freq = float(line.split('#')[0].split()[2])
                ac_flag = 1
            
        
        #checking for valid circuit discription
        if (start > end):
            print('Invalid circuit discription.')
            exit()
        
        #parsing each line and making a list of element's discription
        for i in range((start+1), end):
            parsed_line = main_lines[i].split('#')[0].split()
            element_list.append(parsed_line)
        
        #finding number of nodes in the circuit and creating node dictionary
        j = 0
        for i in element_list:

            if (not i[1] in node_dict):
                j += 1
                node_dict[i[1]] = j
            
            if(not i[2] in node_dict):
                j += 1
                node_dict[i[2]] = j

        no_nodes = len(node_dict)

        #initializing the temproary variable vector and temproary inpedence matrix
        for key in node_dict:
            list_variables.append(key)
        arr_variables = np.array(list_variables)
        i_matrix = np.zeros((no_nodes, no_nodes), dtype=complex)
        rhs_arr = np.zeros(no_nodes, dtype=complex)

        #creating a compatible format for reading netlist lines, so as to deal with CCXX edge cases
        list_temp = []
        for i in element_list:
            if (i[0][0] == 'R' or i[0][0] == 'L' or i[0][0] == 'C'):
                list_temp.append(i)
            else:
                continue
        for i in element_list:
            if (i[0][0] == 'V' or i[0][0] == 'I'):
                list_temp.append(i)
            else:
                continue
        for i in element_list:
            if (i[0][0] == 'E' or i[0][0] == 'G'):
                list_temp.append(i)
            else:
                continue
        for i in element_list:
            if (i[0][0] == 'F' or i[0][0] == 'H'):
                list_temp.append(i)
            else:
                continue
        
        element_list = list_temp

        #adding the stamps to i_matrix and rhs_array and also appending new variables to the 'variable array'
        for i in element_list:

            #adding labels for passive elements
            if (i[0][0] == 'R' or i[0][0] == 'L' or i[0][0] == 'C'):
                temp_analyse = passive_element(i)

                if (ac_flag == 0):
                    if (i[0][0] == 'R'):
                        temp_analyse.value = complex(float(i[3]))
                    elif (i[0][0] == 'L'):
                        temp_analyse.value = 0
                    else:
                        temp_analyse.value = nan
                else:
                    if (i[0][0] == 'R'):
                        temp_analyse.value = complex(float(i[3]))
                    elif (i[0][0] == 'L'):
                        temp_analyse.value = complex(0, (2*ma.pi*ac_freq*float(i[3])))
                    else:
                        temp_analyse.value = complex(0, (-1)*(1/(2*ma.pi*ac_freq*float(i[3]))))

                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.value

                i_matrix[node_dict[a]][node_dict[a]] += 1/c
                i_matrix[node_dict[b]][node_dict[b]] += 1/c
                i_matrix[node_dict[a]][node_dict[b]] += -1/c
                i_matrix[node_dict[b]][node_dict[a]] += -1/c
                

            #adding labels for independent elements  
            if (i[0][0] == 'V' or i[0][0] == 'I'):
                temp_analyse = ind_source(i)

                if (i[3] == 'ac'):
                    temp_analyse.p_p = float(i[4])
                    temp_analyse.phase = float(i[5])
                    temp_analyse.value = ((complex(temp_analyse.p_p))/2)*complex(ma.cos((temp_analyse.phase)), ma.sin((temp_analyse.phase)))
                else:
                    if (i[3] == 'dc'):
                        temp_analyse.value = complex(float(i[4]))
                    else:
                        temp_analyse.value = complex(float(i[3]))
                
                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.value
                
                #independent current source stamp
                if (i[0][0] == 'I'):
                    rhs_arr[node_dict[a]] += -c
                    rhs_arr[node_dict[b]] += c

                #independent voltage source stamp
                else:
                    no_nodes +=  1
                    i_matrix = np.column_stack((i_matrix, np.zeros(no_nodes-1)))
                    i_matrix = np.vstack((i_matrix, np.zeros(no_nodes)))
                    arr_variables = np.append(arr_variables, 'i' + '_' + i[0])
                    rhs_arr = np.append(rhs_arr, 0)
                    volt_dict[i[0]] = no_nodes-1
                
                    i_matrix[node_dict[a]][no_nodes-1] += 1
                    i_matrix[node_dict[b]][no_nodes-1] += -1
                    i_matrix[no_nodes-1][node_dict[b]] += -1
                    i_matrix[no_nodes-1][node_dict[a]] += 1
                    rhs_arr[no_nodes-1] += c
            
            #adding the labels for voltage control sources

            #VCVS stamp
            if(i[0][0] == 'E'):
                temp_analyse = voltage_control_element(i)
                no_nodes +=  1
                i_matrix = np.column_stack((i_matrix, np.zeros(no_nodes-1)))
                i_matrix = np.vstack((i_matrix, np.zeros(no_nodes)))
                arr_variables = np.append(arr_variables, 'i' + '_' + i[0])
                rhs_arr = np.append(rhs_arr, 0)
                volt_dict[i[0]] = no_nodes-1

                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.vc_n_1
                d = temp_analyse.vc_n_2
                e = complex(float(i[5]))

                i_matrix[node_dict[a]][no_nodes-1] += 1
                i_matrix[node_dict[b]][no_nodes-1] += -1
                i_matrix[no_nodes-1][node_dict[a]] += 1
                i_matrix[no_nodes-1][node_dict[b]] += -1
                i_matrix[no_nodes-1][node_dict[c]] += -e
                i_matrix[no_nodes-1][node_dict[d]] += e

            #VCCS stamp
            if(i[0][0] == 'G'):
                temp_analyse = voltage_control_element(i)

                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.vc_n_1
                d = temp_analyse.vc_n_2
                e = complex(float(i[5]))

                i_matrix[node_dict[a]][node_dict[c]] += e
                i_matrix[node_dict[a]][node_dict[d]] += -e
                i_matrix[node_dict[b]][node_dict[c]] += -e
                i_matrix[node_dict[b]][node_dict[d]] += e
            
            #adding labels for current control sources

            #CCVS stamp
            if (i[0][0] == 'H'):
                temp_analyse = current_control_element(i)
                no_nodes +=  1
                i_matrix = np.column_stack((i_matrix, np.zeros(no_nodes-1)))
                i_matrix = np.vstack((i_matrix, np.zeros(no_nodes)))
                arr_variables = np.append(arr_variables, 'i' + '_' + i[0])
                rhs_arr = np.append(rhs_arr, 0)
                volt_dict[i[0]] = no_nodes-1

                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.volt_source
                d = complex(float(i[4]))
                e = volt_dict[c]
                
                i_matrix[node_dict[a]][no_nodes-1] = 1
                i_matrix[node_dict[b]][no_nodes-1] = -1
                i_matrix[no_nodes-1][node_dict[a]] = 1
                i_matrix[no_nodes-1][node_dict[b]] = -1
                i_matrix[no_nodes-1][e] = -d
            
            #CCCS stamp
            if (i[0][0] == 'F'):
                temp_analyse = current_control_element(i)

                a = temp_analyse.from_n
                b = temp_analyse.to_n
                c = temp_analyse.volt_source
                d = complex(float(i[4]))
                e = volt_dict[c]
                
                i_matrix[node_dict[a]][e] = d
                i_matrix[node_dict[b]][e] = -d
            
        #making appropriate deletions 
        i_matrix = np.delete(i_matrix,0,0)          #deleting the row corresponding to 'GND' node
        i_matrix = np.delete(i_matrix,0,1)          #deleting the colomn corresponding to 'GND' node
        arr_variables = np.delete(arr_variables,0)  #deleting GND variable
        rhs_arr = np.delete(rhs_arr,0)              #deleting the first element of rhs_array

        
        print('The values of all node voltages (in V) and currents through the voltage sources (in A) are as follows:')
        print()
        print('GND has the value: (0+0j)')      #for 'GND' node

        #solving the system and printing the result simultaneously
        for i in range(len(arr_variables)):
            print('{} has the value: {}'.format(arr_variables[i], (np.linalg.solve(i_matrix, rhs_arr)[i])))
        print()
        print('Note: v_number denotes the node voltage and i_voltage_source denotes the current via the mentioned voltage source.')


#for non existent file
except IOError:
    print('The netlist file you gave is not present in the directory.')










