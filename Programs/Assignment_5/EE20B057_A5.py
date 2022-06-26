"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 5
"""

#importing the necessary modules required for the program
import math as ma
import sys
from turtle import title
import scipy.linalg as sp
import numpy as np
import pylab as py
import mpl_toolkits.mplot3d.axes3d as p3

#initializing the parameters for the program
if(len(sys.argv) == 5):
    Nx = float(sys.argv[1])
    Ny = float(sys.argv[2])
    radius = float(sys.argv[3])
    Niter = float(sys.argv[4])
    print('Using user provided parameters for the program.')
else:
    Nx = 25
    Ny = 25
    radius = 8
    Niter = 1500
    print('Using default parameters for the program.')


#creating the phi(potential) array and making the central circular portion (8u as default) of it as 1V
phi = py.zeros((Ny, Nx))

x = py.linspace(-0.5, 0.5, Nx)
y = py.linspace(-0.5, 0.5, Ny)
Y, X = py.meshgrid(y, x)
ii = py.where(X*X + Y*Y <= (0.35)*(0.35))
phi[ii] = 1.0


#plotting the contour of the initial potential distribution
x_arr = py.array(range(Nx))
y_arr = py.array(range(Ny))

fig1 = py.figure(1)
py.plot(ii[0]/Nx - 0.5 + (1/(2*Nx)), ii[1]/Ny - 0.5 + (1/(2*Ny)), 'ro', label = 'electrode points')
py.contourf(x, y, phi)
py.colorbar()
py.xlabel('x values')
py.ylabel('y values')
py.title('Initial Potential Distribution')
py.legend()
py.grid(True)
py.savefig('1.png', dpi = 1000)


#performing the main iteration to find the 'laplace based' potential distribution and finding corresponding error
error = py.zeros(Niter)

for index in range(Niter):
    oldphi = phi.copy()
    phi[1:-1, 1:-1] = 0.25*(phi[1:-1, 0:-2] + phi[1:-1, 2:] + phi[0:-2, 1:-1] + phi[2:, 1:-1])
    phi[1:-1, 0] = phi[1:-1, 1]
    phi[1:-1, Nx-1] = phi[1:-1, Nx-2]
    phi[0, 0:] = phi[1, 0:]
    phi[ii] = 1.0
    error[index] = abs(phi-oldphi).max()

#defining a function to compute the 'best fit' of the given error data
def fitfinder(a, b):
    return sp.lstsq(a, b)[0]

#plotting real and 'best fit' error data on various scales
M_all = py.column_stack((py.ones(Niter), py.array(range(Niter))))
M_5h = py.column_stack((py.ones(Niter)[500:], py.array(range(Niter))[500:]))

fit1_data = fitfinder(M_all, py.log(error))
fit2_data = fitfinder(M_5h, py.log(error[500:]))

fit1_final = py.dot(M_all, fit1_data)
fit2_final = py.dot(M_all, fit2_data)

fig2 = py.figure(2)     #semilog plot
py.semilogy(py.array(range(Niter)), error, 'r', label = 'true error')
py.semilogy(py.array(range(Niter))[::50], error[::50], 'ro')
py.semilogy(py.array(range(Niter)), py.exp(fit1_final), 'b', label = 'fit1')
py.semilogy(py.array(range(Niter))[::50], py.exp(fit1_final[::50]), 'bo')
py.semilogy(py.array(range(Niter)), py.exp(fit2_final), 'g', label = 'fit2')
py.semilogy(py.array(range(Niter))[::50], py.exp(fit2_final[::50]), 'go')
py.xlabel('iterations')
py.ylabel('error values on a log scale')
py.title('Semilog-y Error Plot')
py.grid(True)
py.legend()
py.savefig('2.png', dpi = 1000)

fig3 = py.figure(3)     #loglog plot
py.loglog(py.array(range(Niter)), error, 'r', label = 'true error')
py.loglog(py.array(range(Niter))[::50], error[::50], 'ro')
py.loglog(py.array(range(Niter)), py.exp(fit1_final), 'b', label = 'fit1')
py.loglog(py.array(range(Niter))[::50], py.exp(fit1_final[::50]), 'bo')
py.loglog(py.array(range(Niter)), py.exp(fit2_final), 'g', label = 'fit2')
py.loglog(py.array(range(Niter))[::50], py.exp(fit2_final[::50]), 'go')
py.xlabel('iterations on a log scale')
py.ylabel('error values on a log scale')
py.title('LogLog Error Plot')
py.grid(True)
py.legend()
py.savefig('3.png', dpi = 1000)

#calculating cummulative sum of errors for different values of iterations performed
A = ma.exp(fit1_data[0])
B = fit1_data[1]
x_axis = py.arange(100, 1501, 200)

def cumm_sum(a, b, i):
    return (-a/b)*py.exp(b*(i + 0.5))

fig4 = py.figure(4)         #semilog plot
py.semilogy(x_axis, cumm_sum(A, B, x_axis), 'go--', label = 'plot')
py.xlabel('iterations')
py.ylabel('cummulative error sum on a log scale')
py.title('Cummulative Sum Plot (Semilog-y)')
py.grid(True)
py.legend()
py.savefig('4.png', dpi = 1000)

fig5 = py.figure(5)         #loglog plot
py.loglog(x_axis, cumm_sum(A, B, x_axis), 'go--', label = 'plot')
py.xlabel('iterations on a log scale')
py.ylabel('cummulative error sum on a log scale')
py.title('Cummulative Sum Plot (LogLog)')
py.grid(True)
py.legend()
py.savefig('5.png', dpi = 1000)


#3D surface plot of potential on the plate
fig6 = py.figure(6) 
ax = p3.Axes3D(fig6)
surf = ax.plot_surface(-Y, X, phi.T, rstride=1, cstride=1, cmap = py.cm.jet)
py.xlabel('Y')
py.ylabel('X')
py.title('The 3-D Surface Plot of the Potential')
py.savefig('6.png', dpi = 1000)


#contour plot of the 'final potential distribution'
x_temp, y_temp = py.where(X*X + Y*Y <= (0.35)*(0.35))

fig7 = py.figure(7)
py.plot(x_temp/Nx - 0.5 + (1/(2*Nx)), y_temp/Ny - 0.5 + (1/(2*Ny)), 'ro')
py.contourf(y, x[::-1], phi)
py.colorbar()
py.xlabel('x_length')
py.ylabel('y_length')
py.title('The 2-D Contour Plot of the Potential')
py.grid(True)
py.savefig('7.png', dpi = 1000)


#plotting the current density in the plate
Jx = (0.5)*(phi[1:-1, 0:-2] - phi[1:-1, 2:])
Jy = (0.5)*(phi[0:-2, 1:-1] - phi[2:, 1:-1])

Y_arr, X_arr = py.meshgrid(y_arr, x_arr)
X_arr = Nx - X_arr
fig8 = py.figure(8)
py.quiver(Y_arr[1:-1,1:-1], X_arr[1:-1,1:-1], -Jx[:,::-1], -Jy[:,::-1], scale = 3)
x_temp, y_temp = py.where(X*X + Y*Y <= (0.35)*(0.35))
py.plot(x_temp, y_temp, 'ro', label = 'electrode nodes')
py.xlabel('x_values')
py.ylabel('y_values')
py.title('The Vector Plot of the Current Flow')
py.grid(True)
py.legend(loc = 'upper right')
py.savefig('8.png', dpi = 1000)

#showing all the plots in the program
py.show()