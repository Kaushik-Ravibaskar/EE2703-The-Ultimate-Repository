"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
End-Semester Examination
"""

#importing modules necessary for the program
import pylab as py
import numpy as np
import scipy.linalg as lst
import math as ma

#important data pertaining to the problem
l = 0.5                     #half length of antenna
wavelength = 4*l            #wavelength of the radiation
l_antenna = 2*l             #length of the antenna
c = 2.9979e8                #speed of light
mu0 = 4e-7*ma.pi            #permeability of free space
N = 100                     #number of sections in each half section
Im = 1                      #feed current
a = 0.01                    #radius of the wire
f = c/wavelength            #frequency of the radiation
k = 2*ma.pi/wavelength      #wave number
dz = l/N                    #spacing of current samples

#Statement 1

#constructing the vector z
i = np.linspace(-N, N, 2*N+1)
z = i*dz

#constructing the vector u
u = np.append(np.arange(-l+dz, 0, dz), np.arange(dz, l, dz))

#constructing current vectors I and J (which are unknown currently)
I = np.zeros(2*N + 1)
J = np.zeros(2*N - 2)
I[N] = Im

#Statement 2

#writing a function to return the matrix M
def matrix_M(dim):
    return (1/(2*ma.pi*a))*np.diag(np.ones(dim))


#Statement 3

#computing and creating vectors Rz and Ru
(Zj, Zi) = np.meshgrid(z, z)
Rz = np.sqrt(a**2 + (Zi - Zj)**2)           #radius is a

(Uj, Ui) = np.meshgrid(u, u)
Ru = np.sqrt(a**2 + (Uj - Ui)**2)           #radius is a

#computing and creating P and Pb matrix
P = mu0/(4*ma.pi)*np.exp(-k*Ru*(1j))*(1/Ru)*dz
RiN = np.delete(Rz[:, N], [0, N, 2*N])
Pb = (mu0/(4*ma.pi))*np.exp(-k*RiN*(1j))*(1/RiN)*dz

#Statement 4

#creating matrices Qij and Qb
Q = (P*a/mu0)*(k*(1j)*(1/Ru) + 1/(Ru*Ru))
Qb = Pb*(a/mu0)*((1j)*k/(RiN) + 1/(RiN*RiN))

#Statement 5

#obtaining J vector
J = np.dot(np.linalg.inv(matrix_M(2*N-2) - Q), Qb)*Im
I = np.insert(J, [0, N-1, 2*N-2], [0, Im, 0])

#obtaining the actual I vector from the mentioned equation
I_act = Im*np.sin(k*(l - np.abs(z)))

#plotting the computed I along with the assumed I_act
py.figure(1)
py.plot(z, np.abs(I), 'b', label = 'Estimated Plot')
py.plot(z, I_act, 'g', label = 'True plot')
py.xlabel('position along the wire (z-meters)')
py.ylabel('current (I-amperes)')
py.title('Plot of Assumed Current and Expected Current')
py.legend()
py.grid()
py.savefig('b.png', dpi = 1000)
py.show()
















