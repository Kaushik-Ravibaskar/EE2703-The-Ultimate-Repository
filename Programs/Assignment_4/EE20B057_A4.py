"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment 4
"""

#importing necessary modules required for the program
import scipy as sp
import math as ma
import pylab as py
from scipy.integrate import quad
import numpy as np
import scipy.special as spc

#defining function to compute exp(x)
def f1(x):
    return py.exp(x)

#defining function to compute cos(cos(x))
def f2(x):
    return py.cos(py.cos(x))

#defining a_coeff integrand
def u(x,k,selector):

    if(selector == 'f1'):
        return f1(x)*np.cos(k*x)
    else:
        return f2(x)*np.cos(k*x)

#defining b_coeff integrand
def v(x,k,selector):

    if(selector == 'f1'):
        return f1(x)*np.sin(k*x)
    else:
        return f2(x)*np.sin(k*x)


#Problem 1: Plotting the given functions along with their 'possible_fourier' counterparts

#for exponential function
x1_arr = py.linspace(-2*ma.pi, 4*ma.pi, 301)
a_arr = py.linspace(-2*ma.pi, 0, 101)
b_arr = py.linspace(0, 2*ma.pi, 101)
c_arr = py.linspace(2*ma.pi, 4*ma.pi, 101)
py.semilogy(x1_arr[:-1], f1(x1_arr[:-1]), label = 'true plot')
py.semilogy(a_arr[:-1], f1(a_arr[:-1]+2*ma.pi), 'y--', label = 'expected plot')
py.semilogy(b_arr[:-1], f1(b_arr[:-1]), 'y--')
py.semilogy(c_arr[:-1], f1(c_arr[:-1]-2*ma.pi), 'y--')
py.xlabel('x' + r'$\rightarrow$')
py.ylabel('log(exp(x))' + r'$\rightarrow$')
py.title('Figure 1: exp(x) on a semilog-y plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q1(a).png', dpi = 1000)
py.show()

#for cosine_like function
x2_arr = py.linspace(-2*ma.pi, 4*ma.pi, 301)
py.plot(x2_arr[:-1], f2(x2_arr[:-1]), label = 'true plot')
py.plot(x2_arr[:-1], f2(x2_arr[:-1]), 'y--', label = 'expected plot')
py.xlabel('x' + r'$\rightarrow$')
py.ylabel('cos(cos(x))' + r'$\rightarrow$')
py.title('Figure 2: Plot of cos(cos(x))')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q1(b).png', dpi = 1000)
py.show()

#Problem 2: Obtaining fourier coefficients for the two functions

#obtaining coefficients for f1(x)
a1_coeff = py.zeros(26)
b1_coeff = py.zeros(25)

a1_coeff[0] = quad(u, 0, 2*ma.pi, args=(0, 'f1'))[0]/(2*ma.pi)

#a_coefficients
for index in range(1, 26):
    a1_coeff[index] = quad(u, 0, 2*ma.pi, args=(index, 'f1'))[0]/(ma.pi)
#b_coefficients
for index in range(1, 26):
    b1_coeff[index-1] = quad(v, 0, 2*ma.pi, args=(index, 'f1'))[0]/(ma.pi)


#obtaining coefficients for f2(x)
a2_coeff = py.zeros(26)
b2_coeff = py.zeros(25)

a2_coeff[0] = quad(u, 0, 2*ma.pi, args=(0, 'f2'))[0]/(2*ma.pi)

#a_coefficients
for index in range(1, 26):
    a2_coeff[index] = quad(u, 0, 2*ma.pi, args=(index, 'f2'))[0]/(ma.pi)
#b_coefficients
for index in range(1, 26):
    b2_coeff[index-1] = quad(v, 0, 2*ma.pi, args=(index, 'f2'))[0]/(ma.pi)

#Problem 3: Plotting the fourier coefficients of the given functions
n = py.arange(0, 51, 1)

#creating the answer array for f1(x)
ans_arr1 = py.zeros(51)
ans_arr1[0] = a1_coeff[0]

j = 0
l = 1

for index in range(1,51):
    if(index%2 != 0):
        ans_arr1[index] = a1_coeff[l]
        l += 1
    else:
        ans_arr1[index] = b1_coeff[j]
        j += 1

#creating the answer array for f1(x)
ans_arr2 = py.zeros(51)
ans_arr2[0] = a2_coeff[0]

j = 0
l = 1

for index in range(1,51):
    if(index%2 != 0):
        ans_arr2[index] = a2_coeff[l]
        l += 1
    else:
        ans_arr2[index] = b2_coeff[j]
        j += 1

#f1(x) coefficients in semilog plot
py.semilogy(n, abs(ans_arr1), 'ro', label = 'coefficients')
py.xlabel('n' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 3: Coefficients of fourier series of exp(x) in a semilog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q3(a).png', dpi = 1000)
py.show()

#f1(x) coefficients in loglog plot
py.loglog(n, abs(ans_arr1), 'ro', label = 'coefficients')
py.xlabel('log(n)' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 4: Coefficients of fourier series of exp(x) in loglog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q3(b).png', dpi = 1000)
py.show()

#f2(x) coefficients in semilog plot
py.semilogy(n, abs(ans_arr2), 'ro', label = 'coefficients')
py.xlabel('n' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 5: Coefficients of fourier series of cos(cos(x)) in semilog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q3(c).png', dpi = 1000)
py.show()

#f2(x) coefficients in loglog plot
py.loglog(n, abs(ans_arr2), 'ro', label = 'coefficients')
py.xlabel('log(n)' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 6: Coefficients of fourier series of cos(cos(x)) in loglog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q3(d).png', dpi = 1000)
py.show()

#Problem 4: Constructing matrix M and RHS_array for the two functions
x_arr = py.linspace(0, 2*ma.pi, 401)
x_arr = x_arr[:-1]

#constructing M matrix
M = py.zeros((400, 51))
M[:,0] = 1
for index in range(1,26):
    M[:,(2*index-1)] = py.cos(index*x_arr)
    M[:,2*index] = py.sin(index*x_arr)

#constructing RHS_array for the two functions
rhs1 = f1(x_arr)
rhs2 = f2(x_arr)

#Problem 5: Using 'Least Square' method to compute the 'best fit' coefficients using the above developed vectors
ans_lsq_arr_1 = sp.linalg.lstsq(M,rhs1)[0]
ans_lsq_arr_2 = sp.linalg.lstsq(M,rhs2)[0]

#plots for f1(x) coefficients

#semilog plot
py.semilogy(n, abs(ans_arr1), 'ro', label = 'true')
py.semilogy(n, abs(ans_lsq_arr_1), 'go', label = 'approx')
py.xlabel('n' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 3: Coefficients of fourier series of exp(x) in semilog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q5(a).png', dpi = 1000)
py.show()

#loglog plot
py.loglog(n, abs(ans_arr1), 'ro', label = 'true')
py.loglog(n, abs(ans_lsq_arr_1), 'go', label = 'approx')
py.xlabel('log(n)' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 4: Coefficients of fourier series of exp(x) in loglog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q5(b).png', dpi = 1000)
py.show()

#plots for f2(x) coefficients

#semilog plot
py.semilogy(n, abs(ans_arr2), 'ro', label = 'true')
py.semilogy(n, abs(ans_lsq_arr_2), 'go', label = 'approx')
py.xlabel('n' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 5: Coefficients of fourier series of cos(cos(x)) in semilog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q5(c).png', dpi = 1000)
py.show()

#loglog plot
py.loglog(n, abs(ans_arr2), 'ro', label = 'true coefficients')
py.loglog(n, abs(ans_lsq_arr_2), 'go', label = 'approximated coefficients')
py.xlabel('log(n)' + r'$\rightarrow$')
py.ylabel('log(coeff)' + r'$\rightarrow$')
py.title('Figure 6: Coefficients of fourier series of cos(cos(x)) in loglog plot')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q5(d).png', dpi = 1000)
py.show()

#Problem 6: Comparing the actual coefficients and the 'least squared' ones
err_coeff1 = abs(ans_arr1 - ans_lsq_arr_1)
err_coeff2 = abs(ans_arr2 - ans_lsq_arr_2)

max_dev_1 = py.amax(err_coeff1)
max_dev_2 = py.amax(err_coeff2)

print('The difference between coefficients for f1(x) is:')
print(err_coeff1)
print()
print('The difference between coefficients for f2(x) is:')
print(err_coeff2)
print()
print('The maximum absolute deviation for f1(x) coefficients is {}'.format(max_dev_1))
print('The maximum absolute deviation for f2(x) coefficients is {}'.format(max_dev_2))
print('Hence, the two coefficients are not same.')

#Problem 7: Plotting the actual function and the 'least square generated' function

axis = py.linspace(0, 2*ma.pi, 401)[:-1]

#for f1(x) function
f1_gen = py.dot(M, ans_lsq_arr_1)
x1_arr = py.linspace(-2*ma.pi, 4*ma.pi, 301)
a_arr = py.linspace(-2*ma.pi, 0, 101)
b_arr = py.linspace(0, 2*ma.pi, 101)
c_arr = py.linspace(2*ma.pi, 4*ma.pi, 101)
py.semilogy(x1_arr[:-1], f1(x1_arr[:-1]), label = 'true plot')
py.semilogy(a_arr[:-1], f1(a_arr[:-1]+2*ma.pi), 'y', label = 'expected fourier plot')
py.semilogy(b_arr[:-1], f1(b_arr[:-1]), 'y')
py.semilogy(c_arr[:-1], f1(c_arr[:-1]-2*ma.pi), 'y')
py.semilogy(axis, f1_gen, 'go', label = 'approx fourier plot')
py.xlabel('x' + r'$\rightarrow$')
py.ylabel('log(exp(x))' + r'$\rightarrow$')
py.title('Figure 1: Plot of exp(x) in semilog scale')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q7(a).png', dpi = 1000)
py.show()

#for f2(x) function
f2_gen = py.dot(M, ans_lsq_arr_2)
x2_arr = py.linspace(-2*ma.pi, 4*ma.pi, 301)
py.plot(x2_arr[:-1], f2(x2_arr[:-1]), label = 'true plot')
py.plot(x2_arr[:-1], f2(x2_arr[:-1]), 'y--', label = 'expected fourier plot')
py.plot(axis, f2_gen, 'go', label = 'approx fourier plot')
py.xlabel('x' + r'$\rightarrow$')
py.ylabel('cos(cos(x))' + r'$\rightarrow$')
py.title('Figure 2: Plot of cos(cos(x))')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('Q7(b).png', dpi = 1000)
py.show()














