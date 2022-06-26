"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 6
"""

#importing necessary modules required in the program
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as py

#defining a function to compute laplace function of x(t) for the given differential equation and initial conditions
def trans_x(freq, decay):
    p_den_x = np.polymul([1.0, 0, 2.25], [1, 2*decay, (decay)*(decay) + (freq)*(freq)])
    return sp.lti([1, decay], p_den_x)

#defining the system transfer function X(s)/F(s)
def trans_sys():
    return sp.lti([1.], [1., 0, 2.25])

#Problem 1: Finding the time response of the position of the spring for decay = 0.5
(t_1, x_1) = sp.impulse(trans_x(1.5, 0.5), None, np.linspace(0, 50, 3001))
py.figure(1)
py.plot(t_1, x_1, 'g')
py.xlabel('t')
py.ylabel('x')
py.grid(True)
py.title('Forced Damping Oscillator with Decay = 0.5')
py.savefig('1.png', dpi = 1000)

#Problem 2: Finding the time response of the position of the spring for decay = 0.05
(t_2, x_2) = sp.impulse(trans_x(1.5, 0.05), None, np.linspace(0, 50, 3001))
py.figure(2)
py.plot(t_2, x_2, 'r')
py.xlabel('t')
py.ylabel('x')
py.grid(True)
py.title('Forced Damping Oscillator with Decay = 0.05')
py.savefig('2.png', dpi = 1000)

#Problem 3: Simulating the time response of the spring over a range of frequencies for decay = 0.05
fig_index = 3
t_3 = np.linspace(0, 200, 9001)
freq_sample = np.arange(1.4, 1.65, 0.05)

for index in freq_sample:
    py.figure(fig_index)
    f_t = np.cos(index*t_3)*np.exp(-0.05*t_3)
    (t, x_3, svec) = sp.lsim(trans_sys(), f_t, t_3)
    py.plot(t, x_3, label = 'freq: ' + str(index))
    py.xlabel('t')
    py.ylabel('x')
    py.legend()
    py.grid(True)
    py.title('Forced Damping Oscillator with frequency =' + str(index))
    py.savefig(str(fig_index) + '.png', dpi = 1000)
    fig_index += 1

#Problem 4: Solving coupled spring problem to obtain x(t) and y(t)
X_4 = sp.lti([1, 0, 2], [1, 0, 3, 0])
Y_4 = sp.lti([2], [1, 0, 3, 0])

(t, x_4) = sp.impulse(X_4, None, np.linspace(0, 50, 3001))
(t, y_4) = sp.impulse(Y_4, None, np.linspace(0, 50, 3001))

py.figure(8)
py.plot(t, x_4, 'c', label = 'x_position')
py.plot(t, y_4, 'm', label = 'y_position')
py.xlabel('t')
py.ylabel('position')
py.legend()
py.grid(True)
py.title('Coupled Oscillations in X and Y axes')
py.savefig('8.png', dpi = 1000)

#Problem 5: Obtaining magnitude and phase response of the RLC network
R = 100
L = 1e-6
C = 1e-6
H_ckt = sp.lti([1], [L*C, R*C, 1])
(w_ckt, s_ckt, phi_ckt) = H_ckt.bode()
py.figure(9)
py.subplot(2,1,1)
py.semilogx(w_ckt, s_ckt, 'g')
py.ylabel('|H(jw)| (db)')
py.title('Magnitude plot')
py.subplot(2,1,2)
py.semilogx(w_ckt, phi_ckt, 'y')
py.xlabel('w')
py.ylabel(r'L(H(jw)) (degrees)')
py.title('Phase Plot')
py.grid(True)
py.savefig('9.png', dpi = 1000)

#Problem 6: Obtaining vo(t) for the given vi(t) in the above problem

#for 0<t<30us case
t_ckt1 = np.arange(0, 301e-7, 1e-7)
vi_t1 = np.cos(1e3*t_ckt1) - np.cos(1e6*t_ckt1)
(t_ckt1, vo_t1, svec) = sp.lsim(H_ckt, vi_t1, t_ckt1)
py.figure(10)
py.plot(t_ckt1, vo_t1, 'r')
py.xlabel('t')
py.ylabel('Vo(t)')
py.title('Output Voltage Vo(t) for 0<t<30us')
py.grid(True)
py.savefig('10.png', dpi = 1000)

#for long t (ms) variation
t_ckt2 = np.arange(0, 30e-3, 1e-7)
vi_t2 = np.cos(1e3*t_ckt2) - np.cos(1e6*t_ckt2) 
(t_ckt2, vo_t2, svec) = sp.lsim(H_ckt, vi_t2, t_ckt2)
py.figure(11)
py.plot(t_ckt2, vo_t2, 'm')
py.xlabel('t')
py.ylabel('Vo(t)')
py.title('Output Voltage Vo(t) for 0<t<30ms')
py.grid(True)
py.savefig('11.png', dpi = 1000)

#showing all the graphs as output
py.show()









