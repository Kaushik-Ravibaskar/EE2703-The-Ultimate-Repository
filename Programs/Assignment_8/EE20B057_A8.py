"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 8
"""

#importing modules necessary to run the program
import math as ma
import pylab as py

#Problem 1: Working out the examples given in the assignment

#Example 0: Checking the accuracy of DFT
x_0 = py.rand(256)
X_0 = py.fft(x_0)
y_0 = py.ifft(X_0)
print('The difference between the original and processed function is around {}.'.format(abs(x_0-y_0).max()))

#Example 1: Spectrum of sin(5t) function
t_1_1 = py.linspace(0, 2*ma.pi, 257)[: -1]
y_1_1 = py.sin(5*t_1_1)
Y_1_1 = py.fftshift(py.fft(y_1_1))/256
w_1_1 = py.linspace(-128, 127, 256)

py.figure(1)
py.subplot(2, 1, 1)
py.plot(w_1_1, abs(Y_1_1), 'g')
py.xlim([-15, 15])
py.ylabel('|Y|')
py.title(r'Spectrum of $\sin(5t)$')
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_1_1, py.angle(Y_1_1), 'ko')
temp_1_1 = py.where(abs(Y_1_1) >= 1e-3)
py.plot(w_1_1[temp_1_1], py.angle(Y_1_1[temp_1_1]), 'bo')
py.xlim([-15, 15])
py.xlabel('k')
py.ylabel('Phase of Y')
py.grid(True)
py.savefig('1.png', dpi = 1000)

#Example 2: Spectrum of (1 + 0.1cos(t))cos(10t) function
t_1_2 = py.linspace(-4*ma.pi, 4*ma.pi, 513)[: -1]
y_1_2 = (1 + 0.1*py.cos(t_1_2))*py.cos(10*t_1_2)
Y_1_2 = py.fftshift(py.fft(y_1_2))/512
w_1_2 = py.linspace(-64, 64, 513)[ :-1]

py.figure(2)
py.subplot(2, 1, 1)
py.plot(w_1_2, abs(Y_1_2), 'g')
py.xlim([-15, 15])
py.title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
py.ylabel('|Y|')
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_1_2, py.angle(Y_1_2), 'ko', lw =2)
temp_1_2 = py.where(abs(Y_1_2) >= 1e-3)
py.plot(w_1_2[temp_1_2], py.angle(Y_1_2[temp_1_2]), 'bo')
py.xlim([-15, 15])
py.ylabel('Phase of Y')
py.xlabel('k')
py.grid(True)
py.savefig('2.png', dpi = 1000)

#Problem 2: Spectrum of sin^3(t) and cos^3(t) functions

t_2 = py.linspace(-4*ma.pi, 4*ma.pi, 513)[: -1]
w_2 = py.linspace(-64, 64, 513)[ :-1]

#Spectrum of sin^3(t)
y_2_1 = (py.sin(t_2))**3
Y_2_1 = py.fftshift(py.fft(y_2_1))/512
py.figure(3)
py.subplot(2, 1, 1)
py.plot(w_2, abs(Y_2_1), 'g')
py.xlim([-15, 15])
py.title(r"Spectrum of $\sin^3(t)$")
py.ylabel('|Y|')
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_2, py.angle(Y_2_1), 'ko')
temp_2_1 = py.where(abs(Y_2_1) >= 1e-3)
py.plot(w_2[temp_2_1], py.angle(Y_2_1[temp_2_1]), 'bo')
py.xlim([-15, 15])
py.ylabel('Phase of Y')
py.xlabel('k')
py.grid(True)
py.savefig('3.png', dpi = 1000)

#Spectrum of cos^3(t)
y_2_2 = (py.cos(t_2))**3
Y_2_2 = py.fftshift(py.fft(y_2_2))/512
py.figure(4)
py.subplot(2, 1, 1)
py.plot(w_2, abs(Y_2_2), 'g')
py.xlim([-15, 15])
py.title(r"Spectrum of $\cos^3(t)$")
py.ylabel('|Y|')
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_2, py.angle(Y_2_2), 'ko')
temp_2_2 = py.where(abs(Y_2_2) >= 1e-3)
py.plot(w_2[temp_2_2], py.angle(Y_2_2[temp_2_2]), 'bo')
py.xlim([-15, 15])
py.ylabel('Phase of Y')
py.xlabel('k')
py.grid(True)
py.savefig('4.png', dpi = 1000)

#Problem 3: Spectrum of cos(20t +5cos(t)) function

t_3 = py.linspace(-4*ma.pi, 4*ma.pi, 513)[: -1]
w_3 = py.linspace(-64, 64, 513)[ :-1]
y_3 = py.cos(20*t_3 + 5*py.cos(t_3))
Y_3 = py.fftshift(py.fft(y_3))/512

py.figure(5)
py.subplot(2, 1, 1)
py.plot(w_3, abs(Y_3), 'g')
py.xlim([-30, 30])
py.title(r"Spectrum of $cos(20t + 5cos(t))$")
py.ylabel('|Y|')
py.grid(True)
py.subplot(2, 1, 2)
temp_3 = py.where(abs(Y_3) >= 1e-3)
py.plot(w_3[temp_3], py.angle(Y_3[temp_3]), 'bo')
py.xlim([-30, 30])
py.ylabel('Phase of Y')
py.xlabel('k')
py.grid(True)
py.savefig('5.png', dpi = 1000)

#Problem 4: Spectrum of Gaussian exp(-t^2/2)

T_4 = 8*ma.pi
N_4 = 512
Y_4_0 = 0
tolerance = 1e-6
error = tolerance + 1

#bringing accuracy to 6 digits
while error > tolerance:  
    t_4 = py.linspace(-T_4/2, T_4/2, N_4 + 1)[:-1]
    w_4 = py.linspace(-N_4*ma.pi/T_4, N_4*ma.pi/T_4, N_4 + 1)[:-1]
    y_4 = py.exp(-(t_4*t_4)/2)
    Y_4 = py.fftshift(py.fft(py.fftshift(y_4)))*T_4/(2*ma.pi*N_4)
    error = py.sum(abs(Y_4[::2] - Y_4_0))
    Y_4_0 = Y_4
    T_4 *= 2
    N_4 *= 2

py.figure(6)
py.subplot(2, 1, 1)
py.plot(w_4, abs(Y_4), 'g')
py.xlim([-4, 4])
py.title(r"Spectrum of $\exp(-t^2/2)$")
py.ylabel('|Y|')
py.grid(True)
py.subplot(2, 1, 2)
temp_4 = py.where(abs(Y_4) > tolerance)
py.plot(w_4[temp_4], py.angle(Y_4[temp_4]), 'ko')
temp_4 = py.where(abs(Y_4) >= 1e-3)
py.plot(w_4[temp_4], py.angle(Y_4[temp_4]), 'bo')
py.xlim([-4, 4])
py.ylabel('Phase of Y')
py.xlabel('k')
py.grid(True)
py.savefig('6.png', dpi = 1000)

#plotting all the plots together using the below function
py.show()
