"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 3
"""

#importing important modules required for the program
import numpy as np
import statistics as st
import sys
import pylab as py
import scipy.special as sp
import scipy as sc

#defining function to compute the g(t,A,B) function
def g(t, A, B):
    return (A*sp.jn(2,t) + B*t)

#defining a function to calculate the mean of sum of square of difference
def mn_sum_sq_diff(in_arr, t_arr, val1, val2):
    temp_val_1 = (in_arr - g(t_arr, val1, val2))*(in_arr - g(t_arr, val1, val2))
    temp_val_sum = py.sum(temp_val_1)
    return (temp_val_sum/py.size(in_arr))



#creating variables to be used in the program
temp_list = []
t_array = []
data_colomns_list = []
given_data = []
Ao = 1.05
Bo = -0.105

#loading the data from 'fitting.dat' file and making time and given_data array out of it
data_lines = np.loadtxt("fitting.dat", dtype=float)
given_data = np.array(data_lines[:, 1:])
t_array = np.array(data_lines[:, 0])

#plotting the curves which have different amount of noises in them 
sigma_noise = py.logspace(-1, -3, 9)
for i in range(len(data_lines[0])-1):
    py.plot(t_array, given_data[:, i], label = r'$\sigma$' + str(i+1) + ' = ' + str(sigma_noise[i]))

#plotting the 'true value' curve in the same plot as above
true_value = g(t_array, 1.05, -0.105)
py.plot(t_array, true_value, c = 'k', label = 'True Value')

#annotating the above generated figure and showing the plot
py.xlabel(r't$\rightarrow$')
py.ylabel('f(t) + noise' + r'$\rightarrow$')
py.title('Q4: Data to be fitted to theory')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q4.png', dpi = 1000)
py.show()

#plotting the first coloumn of data with error bars and comparing it with the 'true plot'
py.errorbar(t_array[::5], given_data[:, 0][::5], st.stdev(given_data[:, 0]), fmt = 'ro', label = 'Errorbar')
py.plot(t_array, g(t_array, 1.05, -0.105), c = 'k', label = 'f(t)')
py.xlabel(r't$\rightarrow$')
py.title(r'Q5: Data points for $\sigma$ = 0.10 along with exact function')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q5.png', dpi = 1000)
py.show()

#generating M matrix and verifying the mentioned relation in problem 6
jn_array = sp.jn(2,t_array)
Ao = 1.05
Bo = -0.105
M = py.column_stack((jn_array, t_array))
p = py.array([Ao, Bo])
m_p = py.dot(M, p)
rhs_element = g(t_array, Ao, Bo)

if (m_p.all() == rhs_element.all()):
    print('The comparison is a true comparison.')
else:
    print('The comparison is a false comparison.')

#calculating the mean squared error of the first coloum of given_data over a range of A and B values and plotting the corresponding contour
A_array = py.arange(0, 2.1, 0.1)
B_array = py.arange(-0.2, 0.01, 0.01)
e_list = []

for a in A_array:
    for b in B_array:
        e_list.append(mn_sum_sq_diff(given_data[:, 0], t_array, a, b))
e_list = py.array(e_list)
e_list = e_list.reshape((py.size(A_array), py.size(B_array)))
py.clabel(py.contour(A_array, B_array, e_list, 20))
py.xlabel(r'A$\rightarrow$')
py.ylabel(r'B$\rightarrow$')
py.title(r'Q8: Contour plot of $\epsilon$ij')
py.plot(Ao, Bo, 'ro')
py.text(Ao, Bo, 'Exact Location')
py.grid(True)
py.savefig('Q8.png', dpi = 1000)
py.show()

#finding the best approximate value of A and B that fits the data in first coloum of given_data
app_1_tuple = sc.linalg.lstsq(M, given_data[:, 0])


#calculating A and B for different data lines and plotting the error in them with respect to the noise sigma
app_A = []
app_B = []
sigma_noise = py.logspace(-1, -3, 9)
for i in range(len(data_lines[0])-1):
    temp_app = sc.linalg.lstsq(M, given_data[:, i])
    app_A.append(temp_app[0][0])
    app_B.append(temp_app[0][1])
app_A = py.array(app_A)
app_B = py.array(app_B)
err_A = abs(app_A - 1.05)
err_B = abs(app_B + 0.105)

print('The values of A for each colomn is as follows:')
print(app_A)
print()
print('The values of B for each colomn is as follows:')
print(app_B)

py.plot(sigma_noise, err_A, 'r*--', label = 'Aerr')
py.plot(sigma_noise, err_B, 'b*--', label = 'Berr')
py.xlabel(r'Noise standard deviation $\rightarrow$')
py.ylabel(r'MS error $\rightarrow$')
py.title('Q10: Variation of error with noise')
py.grid(True)
py.savefig('Q10.png', dpi = 1000)
py.legend(loc = 'upper left')

py.show()

#plotting the loglog plot using errorbars for error in A and B
(py.errorbar(sigma_noise, err_A, st.stdev(err_A), fmt = 'ro', label = 'Aerr'))
(py.errorbar(sigma_noise, err_B, st.stdev(err_B), fmt = 'go', label = 'Berr'))
py.loglog()
py.grid(True)
py.xlabel(r'$\sigma$ $\rightarrow$')
py.ylabel(r'MSerror $\rightarrow$')
py.title('Q11: Variation of error with noise')
py.legend(loc = 'upper right')
py.savefig('Q11.png', dpi = 1000)
py.show()





    


    
    

    



    


