"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 9
"""

#importing necessary modules for the program
import math as ma
import pylab as py
import random as rand
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3

#Problem 1: Working out the problems given in the assignment sheet

#Ex 1: Spectrum of sin(sqrt(2)*t) computed in a straightforward manner
t_1_1 =  py.linspace(-ma.pi, ma.pi, 65)[ :-1]
dt_1_1 = t_1_1[1] - t_1_1[0]
f_1_1 = 1/dt_1_1
y_1_1 = py.sin(ma.sqrt(2)*t_1_1)
y_1_1[0] = 0 
y_1_1 = py.fftshift(y_1_1)
Y_1_1 = py.fftshift(py.fft(y_1_1))/64.0
w_1_1 = py.linspace(-ma.pi*f_1_1, ma.pi*f_1_1, 65)[ :-1]

py.figure(1)
py.subplot(2, 1, 1)
py.plot(w_1_1, abs(Y_1_1), 'r')
py.xlim([-10,10])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\sin\left(\sqrt{2}t\right)$")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_1_1, py.angle(Y_1_1), 'go')
py.xlim([-10,10])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("1.png", dpi = 1000)

#Ex 2: Plotting sin(sqrt(2)*t) over different time intervals
t_1_2_1 = py.linspace(-ma.pi, ma.pi, 65)[ :-1]
t_1_2_2 = py.linspace(-3*ma.pi, -ma.pi, 65)[ :-1]
t_1_2_3 = py.linspace(ma.pi, 3*ma.pi, 65)[ :-1]

py.figure(2)
py.plot(t_1_2_1, py.sin(ma.sqrt(2)*t_1_2_1), 'm')
py.plot(t_1_2_2, py.sin(ma.sqrt(2)*t_1_2_2), 'g')
py.plot(t_1_2_3, py.sin(ma.sqrt(2)*t_1_2_3), 'g')
py.ylabel(r"$y$")
py.xlabel(r"$t$")
py.title(r"$\sin\left(\sqrt{2}t\right)$ over different intervals")
py.grid(True)
py.savefig("2.png", dpi = 1000)

#Ex 3: Replicating sin(sqrt(2)*t) between -pi to +pi over the time axis
t_1_3_1 = py.linspace(-ma.pi, ma.pi, 65)[ :-1]
t_1_3_2 = py.linspace(-3*ma.pi, -ma.pi, 65)[ :-1]
t_1_3_3 = py.linspace(ma.pi, 3*ma.pi, 65)[ :-1]
y_1_3 = py.sin(ma.sqrt(2)*t_1_3_1)

py.figure(3)
py.plot(t_1_3_1, y_1_3, 'm')
py.plot(t_1_3_2, y_1_3, 'g')
py.plot(t_1_3_3, y_1_3, 'g')
py.ylabel(r"$y$")
py.xlabel(r"$t$")
py.title(r"$\sin\left(\sqrt{2}t\right)$ with $t$ wrapping every $2\pi$")
py.grid(True)
py.savefig("3.png", dpi = 1000)

#Ex 4: Spectrum of the ramp (-pi tp +pi) which is periodically repeating
t_1_4 = py.linspace(-ma.pi, ma.pi, 65)[ :-1]
dt_1_4 = t_1_4[1] - t_1_4[0]
f_1_4 = 1/dt_1_4
y_1_4 = t_1_4
y_1_4[0] = 0
y_1_4 = py.fftshift(y_1_4)
y_1_4 = py.fftshift(py.fft(y_1_4))/64.0
w_1_4 = py.linspace(-ma.pi*f_1_4, ma.pi*f_1_4, 65)[ :-1]

py.figure(4)
py.semilogx(abs(w_1_4), 20*py.log10(abs(y_1_4)), 'y')
py.xlim([1,10])
py.ylim([-20,0])
py.xticks([1,2,5,10],["1","2","5","10"])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of a digital ramp")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("4.png", dpi = 1000)

#Ex 5: Plot of sin(sqrt(2)*t) windowed using the Hamming window given in the assignment sheet
t_1_5_1 = py.linspace(-ma.pi, ma.pi, 65)[ :-1]
t_1_5_2 = py.linspace(-3*ma.pi, -ma.pi, 65)[ :-1]
t_1_5_3 = py.linspace(ma.pi, 3*ma.pi, 65)[ :-1]
n_1_5 = py.arange(64)
wnd_1_5 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_1_5/64))
y_1_5 = py.sin(ma.sqrt(2)*t_1_5_1)*wnd_1_5

py.figure(5)
py.plot(t_1_5_1, y_1_5, 'm')
py.plot(t_1_5_2, y_1_5, 'g')
py.plot(t_1_5_3, y_1_5, 'g')
py.ylabel(r"$y$")
py.xlabel(r"$t$")
py.title(r"$\sin\left(\sqrt{2}t\right)\times w(t)$ with $t$ wrapping every $2\pi$ ")
py.grid(True)
py.savefig("5.png", dpi = 1000)

#Ex 6: Spectrum of sin(sqrt(2)*t) windowed using the Hamming window given in the assignment sheet
t_1_6 = py.linspace(-4*ma.pi, 4*ma.pi, 257)[ :-1]
dt_1_6 = t_1_6[1] - t_1_6[0]
f_1_6 = 1/dt_1_6
n_1_6 = py.arange(256)
wnd_1_6 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_1_6/256))
y_1_6 = py.sin(ma.sqrt(2)*t_1_6)
y_1_6 = y_1_6*wnd_1_6
y_1_6[0] = 0 
y_1_6 = py.fftshift(y_1_6)
Y_1_6 = py.fftshift(py.fft(y_1_6))/256.0
w_1_6 = py.linspace(-ma.pi*f_1_6, ma.pi*f_1_6, 257)[ :-1]

py.figure(6)
py.subplot(2, 1, 1)
py.plot(w_1_6, abs(Y_1_6), 'r', w_1_6, abs(Y_1_6), 'bo')
py.xlim([-4,4])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_1_6, py.angle(Y_1_6), 'mo')
py.xlim([-4,4])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("6.png", dpi = 1000)

#Problem 2: Spectrum of cos^3(w_o*t)
w_o_2 = 0.86

#Ex 1: Without a Hamming window
t_2_1 = py.linspace(-4*ma.pi, 4*ma.pi, 257)[ :-1]
dt_2_1 = t_2_1[1] - t_2_1[0]
f_2_1 = 1/dt_2_1
y_2_1 = (py.cos(w_o_2*t_2_1))**3
y_2_1[0] = 0 
y_2_1 = py.fftshift(y_2_1)
Y_2_1 = py.fftshift(py.fft(y_2_1))/256.0
w_2_1 = py.linspace(-ma.pi*f_2_1, ma.pi*f_2_1, 257)[ :-1]

py.figure(7)
py.subplot(2, 1, 1)
py.plot(w_2_1, abs(Y_2_1), 'r')
py.xlim([-10, 10])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\cos^3(\omega_ot)$ (non-windowed)")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_2_1, py.angle(Y_2_1), 'go')
py.xlim([-10, 10])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("7.png", dpi = 1000)

#Ex 2: With a Hamming window
t_2_2 = py.linspace(-4*ma.pi, 4*ma.pi, 257)[ :-1]
dt_2_2 = t_2_2[1] - t_2_2[0]
f_2_2 = 1/dt_2_2
y_2_2 = (py.cos(w_o_2*t_2_2))**3
n_2_2 = py.arange(256)
wnd_2_2 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_2_2/256))
y_2_2 = y_2_2*wnd_2_2
y_2_2[0] = 0 
y_2_2 = py.fftshift(y_2_2)
Y_2_2 = py.fftshift(py.fft(y_2_2))/256.0
w_2_2 = py.linspace(-ma.pi*f_2_2, ma.pi*f_2_2, 257)[ :-1]

py.figure(8)
py.subplot(2, 1, 1)
py.plot(w_2_2, abs(Y_2_2), 'r')
py.xlim([-10, 10])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\cos^3(\omega_ot)$ (windowed)")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_2_2, py.angle(Y_2_2), 'go')
py.xlim([-10, 10])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("8.png", dpi = 1000)

#Problem 3: Spectrum of cos(w_o*t + delta) for random w_o and delta values
w_o_3 = rand.uniform(0.51, 1.5)
delta_3 = rand.uniform(-ma.pi, ma.pi)

t_3 = py.linspace(-ma.pi, ma.pi, 129)[ :-1]
dt_3 = t_3[1] - t_3[0]
f_3 = 1/dt_3
y_3 = py.cos(w_o_3*t_3 + delta_3)
n_3 = py.arange(128)
wnd_3 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_3/128))
y_3 = y_3*wnd_3
y_3[0] = 0 
y_3 = py.fftshift(y_3)
Y_3 = py.fftshift(py.fft(y_3))/128.0
w_3 = py.linspace(-ma.pi*f_3, ma.pi*f_3, 129)[ :-1]

print('This answer is for P3')
print('The value of true w_o is: {}'.format(w_o_3))
print('The value of true delta is: {}'.format(delta_3))

#estimating omega
temp_3 = py.where(w_3 > 0)
w_est_3 = py.sum(abs(Y_3[temp_3])**3*w_3[temp_3])/py.sum(abs(Y_3[temp_3])**3)
print('The estimated value of w_o is: {}'.format(w_est_3))

#estimating delta
temp_3 = py.where(py.logical_and(abs(Y_3)>3e-3, w_3>0))[0]
delta = (py.angle(Y_3[temp_3[0]]) + py.angle(Y_3[temp_3[1]]))/2
print('The estimated value of delta is: {}'.format(delta))

py.figure(9)
py.subplot(2, 1, 1)
py.plot(w_3, abs(Y_3), 'r')
py.xlim([-8, 8])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\cos(\omega_ot + \delta)$")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_3, py.angle(Y_3), 'go')
py.xlim([-8, 8])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("9.png", dpi = 1000)

print()

#Problem 4: Spectrum of cos(w_o*t + delta) with added 'White Gaussian Noise'
w_o_4 = rand.uniform(0.51, 1.5)
delta_4 = rand.uniform(-ma.pi, ma.pi)


t_4 = py.linspace(-ma.pi, ma.pi, 129)[ :-1]
dt_4 = t_4[1] - t_4[0]
f_4 = 1/dt_4
n_4 = py.arange(128)
y_4 = py.cos(w_o_4*t_4 + delta_4) + 0.1*np.random.randn(128)
wnd_4 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_4/128))
y_4 = y_4*wnd_4
y_4[0] = 0 
y_4 = py.fftshift(y_4)
Y_4 = py.fftshift(py.fft(y_4))/128.0
w_4 = py.linspace(-ma.pi*f_4, ma.pi*f_4, 129)[ :-1]

print('This answer is for P4')
print('The value of true w_o is: {}'.format(w_o_4))
print('The value of true delta is: {}'.format(delta_4))

#estimating omega
temp_4 = py.where(w_4 > 0)
w_est_4 = py.sum(abs(Y_4[temp_4])**3*w_4[temp_4])/py.sum(abs(Y_4[temp_4])**3)
print('The estimated value of w_o is: {}'.format(w_est_4))

#estimating delta
temp_4 = py.where(py.logical_and(abs(Y_4)>3e-3, w_4>0))[0]
delta = (py.angle(Y_4[temp_4[0]]) + py.angle(Y_4[temp_4[1]]))/2
print('The estimated value of delta is: {}'.format(delta))

py.figure(10)
py.subplot(2, 1, 1)
py.plot(w_4, abs(Y_4), 'r')
py.xlim([-3, 3])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of $\cos(\omega_ot + \delta)$ with Noise")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_4, py.angle(Y_4), 'go')
py.xlim([-3, 3])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("10.png", dpi = 1000)

#Problem 5: Spectrum of cos(16t(1.5 + t/(2*pi))) function (with Hamming window)
t_5 = py.linspace(-ma.pi, ma.pi, 1025)[ :-1]
dt_5 = t_5[1] - t_5[0]
f_5 = 1/dt_5
y_5 = py.cos(16*t_5*(1.5 + t_5/(2*ma.pi)))
n_5 = py.arange(1024)
wnd_5 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_5/1024))
y_5 = y_5*wnd_5
y_5[0] = 0 
y_5 = py.fftshift(y_5)
Y_5 = py.fftshift(py.fft(y_5))/1024.0
w_5 = py.linspace(-ma.pi*f_5, ma.pi*f_5, 1025)[ :-1]

py.figure(11)
py.subplot(2, 1, 1)
py.plot(w_5, abs(Y_5), 'r')
py.xlim([-80, 80])
py.ylabel(r"$|Y|$")
py.title(r"Spectrum of Chirped Signal")
py.grid(True)
py.subplot(2, 1, 2)
py.plot(w_5, py.angle(Y_5), 'go')
py.xlim([-80, 80])
py.ylabel(r"Phase of $Y$")
py.xlabel(r"$\omega$")
py.grid(True)
py.savefig("11.png", dpi = 1000)

#Problem 6: Analysing the variation of the frequency of the Chirped Signal (with Hamming window) with time
t_6 = py.linspace(-ma.pi, ma.pi, 1025)[ :-1]
t_6_array = py.split(t_6, 16)

#initialising the 2D magnitude and phase arrays
Y_6_mag = py.zeros((16,64))
Y_6_angles = py.zeros((16,64))

#computing the DFT and stroing it in the 2D array
for i in range(len(t_6_array)):
    t_6_temp = t_6_array[i]
    dt_6 = t_6_temp[1] - t_6_temp[0]
    f_6 = 1/dt_6
    y_6 = py.cos(16*t_6_temp*(1.5 + t_6_temp/(2*ma.pi)))
    n_6 = py.arange(64)
    wnd_6 = py.fftshift(0.54+0.46*py.cos(2*ma.pi*n_6/64))
    y_6 = y_6*wnd_6
    y_6[0] = 0 
    y_6 = py.fftshift(y_6)
    Y_6 = py.fftshift(py.fft(y_6))/64.0
    Y_6_mag[i] =  abs(Y_6)
    Y_6_angles[i] =  py.angle(Y_6)

#performing surface plots
fig12 = py.figure(12)
t_axis = py.linspace(-np.pi,np.pi,1025)[ :-1]
f_6 = 1/(t_axis[1] - t_axis[0])
t_axis = t_axis[::64]
w_axis = py.linspace(-f_6*ma.pi, f_6*np.pi, 65)[ :-1]
(T_axis, W_axis) = py.meshgrid(t_axis, w_axis)
ax = p3.Axes3D(fig12)
surf_6_1 = ax.plot_surface(W_axis, T_axis, Y_6_mag.T, rstride=1, cstride=1, cmap = py.cm.jet)
fig12.colorbar(surf_6_1, shrink=0.5, aspect=5)
py.ylabel("Time")
py.xlabel("Frequency")
py.title('Magnitude Surface Plot (Chirped Signal)')
py.savefig("12.png", dpi = 1000)

fig13 = py.figure(13)
ax = p3.Axes3D(fig13)
surf_6_2 = ax.plot_surface(W_axis, T_axis, Y_6_angles.T)
fig13.colorbar(surf_6_2, shrink=0.5, aspect=5)
py.ylabel("Time")
py.xlabel("Frequency")
py.title('Phase Surface Plot (Chirped Signal)')
py.savefig("13.png", dpi = 1000)

#showing all the plots simultaneously using the below function
py.show()
