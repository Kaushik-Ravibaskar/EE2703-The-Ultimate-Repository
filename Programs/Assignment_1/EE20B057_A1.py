"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 1
"""

#importing the sys module into the namespace
import sys

#defining variables which can also be used for general naming conventions of circuit
CIRCUIT = '.circuit'
END = '.end'

#defining the default value of start and end variables to store the position of .circuit and .end
start = 7
end = 5

#checking whether a single file name in commandline is given or not
if (len(sys.argv) != 2):
    print('Please type in the netlist file (only one) in the commandline.')
    exit()

#checking for valid netlist file typed in commandline
if (not sys.argv[1].endswith('.netlist')):
    print('Invalid file type in commandline. Please give a netlist file in commandline.')
    exit()

#function to print the contents of a list in reversed order
def print_one_desc(list_temp):
    for i in range(1, (len(list_temp)+1)):
        if (i != (len(list_temp))):
            print(list_temp[-i], end = " ")
        else:
            print(list_temp[-i])


#function to perform analysis upon each line in the netlist file and store it in a dictionary in a meaningful manner
def analyse_line(list_temp):

    #for R, L, C, Independent sources
    if(len(list_temp) == 4):
        list_dict = {}
        name = list_temp[0]
        node_1 = list_temp[1]
        node_2 = list_temp[2]
        value = list_temp[3]

        if name[0] == 'R':
            list_dict['Type of the element'] = 'Resistor'
        elif name[0] == 'L':
            list_dict['Type of the element'] = 'Inductor'
        elif name[0] == 'C':
            list_dict['Type of the element'] = 'Capacitor'
        elif name[0] == 'V':
            list_dict['Type of the element'] = 'Independent Voltage Source'
        elif name[0] == 'I':
            list_dict['Type of the element'] = 'Independent Current Source'
        else:
            list_dict['Type of the element'] = 'Unknown element'

        list_dict['Name of the element (symbolic)'] = name
        list_dict['Node 1'] = node_1
        list_dict['Node 2'] = node_2
        list_dict['Value of the element'] = value
        
        return list_dict
    
    #for current controlled source
    if(len(list_temp) == 5):
        list_dict = {}
        name = list_temp[0]
        node_1 = list_temp[1]
        node_2 = list_temp[2]
        volt_source = list_temp[3]
        value = list_temp[4]
        
        if name[0] == 'H':
            list_dict['Type of the element'] = 'Current controlled voltage source'
        elif name[0] == 'F':
            list_dict['Type of the element'] = 'Current controlled current source'
        else:
            list_dict['Type of the element'] = 'Unknown element'
        
        list_dict['Name of the element (symbolic)'] = name
        list_dict['Node 1'] = node_1
        list_dict['Node 2'] = node_2
        list_dict['Voltage Source'] = volt_source
        list_dict['Value of the element'] = value

        return list_dict
            
    #for voltage controlled source
    if(len(list_temp) == 6):
        list_dict = {}
        name = list_temp[0]
        node_1 = list_temp[1]
        node_2 = list_temp[2]
        volt_source_node_1 = list_temp[3]
        volt_source_node_2 = list_temp[4]
        value = list_temp[5]
        
        if name[0] == 'E':
            list_dict['Type of the element'] = 'Voltage controlled voltage source'
        elif name[0] == 'G':
            list_dict['Type of the element'] = 'Voltage controlled current source'
        else:
            list_dict['Type of the element'] = 'Unknown element'
        
        list_dict['Name of the element (symbolic)'] = name
        list_dict['Node 1'] = node_1
        list_dict['Node 2'] = node_2
        list_dict['Voltage source node 1'] = volt_source_node_1
        list_dict['Voltage source node 2'] = volt_source_node_2
        list_dict['Value of the element'] = value

        return list_dict
   
    #empty line case
    if(len(list_temp) == 0):
        return []

#using try-except block to test whether the file name typed in is present in the directory or not
try:

    #opening of netlist file and aliasing it under mainfile
    with open(sys.argv[1]) as mainfile:
        
        #parsing each line in the mainfile object and storing it into line_desc variable
        line_desc = mainfile.readlines()
        
        #initialising the value of start and end variables before starting the main iteration
        for one_desc in line_desc:
            if (CIRCUIT == one_desc[:len(CIRCUIT)]):
                start = line_desc.index(one_desc)
            if (END == one_desc[:len(END)]):
                end = line_desc.index(one_desc)
        
        #checking for invalid circuit declaration case
        if (start > end):
            print('Invalid circuit declaration.')
            exit()
        
        #starting the iteration to print the analysed portion of the file using dictionaries
        for index in range(start+1, end):

            #this line of code takes out all tokens present in a line and puts it in a list
            list = line_desc[index].split('#')[0].split()
            
            dict_desc = analyse_line(list)

            for desc in dict_desc:
                print('{} is: {}'.format(desc, dict_desc[desc]))
        
            print('')

        #printing the lines in the reverse order
        for index in range(end-1, start, -1):
            list = line_desc[index].split('#')[0].split()
            print_one_desc(list)
            

#printing error script for wrong file name      
except IOError:
    print('The file you typed in commandline is not present in the directory.')
        

        


            





