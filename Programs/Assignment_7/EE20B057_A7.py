"""
Name: Kaushik Ravibaskar
Roll No: EE20B057
Assignment: 7
"""

#importing necessary libraries for the program
from cmath import pi
import sympy as sy
import pylab as py
import scipy.signal as sig

#defining some symbols which are used frequently in the program
s = sy.symbols('s')

#defining the low-pass filter function
def lowpass(R1, R2, C1, C2, G, Vi):
    t = sy.Matrix([[0, 0, 1, -1/G], [-1/(1+s*R2*C2), 1, 0, 0], [0, -G, G, 1], [-1/R1-1/R2-s*C1, 1/R2, 0, s*C1]])
    o = sy.Matrix([0, 0, 0, -Vi/R1])
    x = t.inv()*o
    return (t, o, x)

#defining the high-pass filter function
def highpass(R1, R3, C1, C2, G, Vi):
    t = sy.Matrix([[0, 1, 0, -1/G], [0, -G, G, -1], [-s*C2, 0, (s*C2 + (1/R3)), 0],  [s*(C1 + C2) + (1/R1), 0, -s*C2, -(1/R1)]])
    o = sy.Matrix([0, 0, 0, Vi*s*C1])
    x = t.inv()*o
    return (t, o, x)

#defining a function to get numerator and denominator coefficients of a symbolic expression
def sym_extract(K):
    K = sy.simplify(K)
    (num, den) = sy.fraction(K)
    num = sy.Poly(num, s)
    den = sy.Poly(den, s)
    num = num.all_coeffs()
    den = den.all_coeffs()
    num = [float(temp) for temp in num]
    den = [float(temp) for temp in den]
    return (num, den)

#Problem 1: Obtaining magnitude response and step response of the given Low-Pass Butterworth filter

#given data
r1_1 = 10000
r1_2 = 10000
c1_1 = 1e-9
c1_2 = 1e-9
G1 = 1.586

#obtaining and plotting magnitude response
(t_1, o_1, h_1) = lowpass(r1_1, r1_2, c1_1, c1_2, G1, 1)
h_1s = h_1[3]
(num_h1s, den_h1s) = sym_extract(h_1s)
h_1s = sig.lti(num_h1s, den_h1s)

h_1l = h_1[3]
w_1 = py.logspace(0, 9, 2001)
h_1l = sy.lambdify(s, h_1l, 'numpy')
h_1l = h_1l(w_1)

py.figure(1)
py.loglog(w_1, abs(h_1l), 'g', lw = 2)
py.xlabel('w (log-space)')
py.ylabel('|H(jw)| (log-scale)')
py.title('Low Pass Magnitude Response')
py.grid(True)
py.savefig('1.png', dpi = 1000)

#obtaining and plotting step response
(t_1, o_1, vi_1) = lowpass(r1_1, r1_2, c1_1, c1_2, G1, 1/s)
vi_1 = vi_1[3]
(num_vi_1, den_vi_1) = sym_extract(vi_1)
vi_1 = sig.lti(num_vi_1, den_vi_1)
(t1_x, vo_1) = sig.impulse(vi_1, None, py.linspace(0, 0.002, 7001))

py.figure(2)
py.plot(t1_x, vo_1, 'm')
py.xlabel('t')
py.ylabel('Vo(t)')
py.title('Step Response of the Low-Pass Filter')
py.grid(True)
py.savefig('2.png', dpi = 1000)

#Problem 2: Obtaining output response for the summation of sinusoidal inputs
t2_x = py.linspace(0, 0.002, 7001)
vi2_t = py.sin(2000*pi*t2_x) + py.cos(2000000*pi*t2_x)
(t2_x, vo_2, svec) = sig.lsim(h_1s, vi2_t, t2_x)

py.figure(3)
py.plot(t2_x, vo_2, 'y')
py.xlabel('t')
py.ylabel('Vo(t)')
py.title('Output of LPF to Summation of Sinusoidal Inputs')
py.grid(True)
py.savefig('3.png', dpi = 1000)

#Problem 3: Obtaining Magitude Plots of the High-Pass filter

#given data
r3_1 = 10000
r3_3 = 10000
c3_1 = 1e-9
c3_2 = 1e-9
G3 = 1.586

#obtaining and plotting magnitude plots
(t_3, o_3, h_3) = highpass(r3_1, r3_3, c3_1, c3_2, G3, 1)
h_3l = h_3[3]
w_3 = py.logspace(0, 9, 2001)
h_3l = sy.lambdify(s, h_3l, 'numpy')
h_3l = h_3l(w_3)

h_3s = h_3[3]
(num_h3s, den_h3s) = sym_extract(h_3s)
h_3s = sig.lti(num_h3s, den_h3s)

py.figure(4)
py.loglog(w_3, abs(h_3l), 'r', lw = 2)
py.xlabel('w (log-space)')
py.ylabel('|H(jw)| (log-scale)')
py.title('High Pass Magnitude Response')
py.grid(True)
py.savefig('4.png', dpi = 1000)

#Problem 4: Obtaining responses for the damped sinusoidal signals by the above two filters
t_4l = py.linspace(0, 0.1, 5001)
t_4h = py.linspace(0, 0.0001, 5001)
vl_t = py.exp(-100*t_4l)*py.sin(2000*pi*t_4l)
vh_t = py.exp(-50000*t_4h)*py.sin(2000000*pi*t_4h)

(t_4, vo_lpl, svec) = sig.lsim(h_1s, vl_t, t_4l)
(t_4, vo_hpl, svec) = sig.lsim(h_3s, vl_t, t_4l)
(t_4, vo_lph, svec) = sig.lsim(h_1s, vh_t, t_4h)
(t_4, vo_hph, svec) = sig.lsim(h_3s, vh_t, t_4h)

py.figure(5)
py.plot(t_4l, vl_t, 'm')
py.xlabel('t')
py.ylabel('vi(t)')
py.title('Low Frequency Sinusoidal Input (1000Hz)')
py.grid(True)
py.savefig('5.png', dpi = 1000)

py.figure(6)
py.plot(t_4l, vo_lpl, 'g')
py.xlabel('t')
py.ylabel('vo(t)')
py.title('Low-Pass Filter Response to the 1000Hz Input')
py.grid(True)
py.savefig('6.png', dpi = 1000)

py.figure(7)
py.plot(t_4l, vo_hpl, 'r')
py.xlabel('t')
py.ylabel('vo(t)')
py.title('High-Pass Filter Response to the 1000Hz Input')
py.grid(True)
py.savefig('7.png', dpi = 1000)

py.figure(8)
py.plot(t_4h, vh_t, 'm')
py.xlabel('t')
py.ylabel('vi(t)')
py.title('High Frequency Sinusoidal Input (1000000Hz)')
py.grid(True)
py.savefig('8.png', dpi = 1000)

py.figure(9)
py.plot(t_4h, vo_lph, 'r')
py.xlabel('t')
py.ylabel('vo(t)')
py.title('Low-Pass Filter Response to the 1000000Hz Input')
py.grid(True)
py.savefig('9.png', dpi = 1000)

py.figure(10)
py.plot(t_4h, vo_hph, 'r')
py.xlabel('t')
py.ylabel('vo(t)')
py.title('High-Pass Filter Response to the 1000000Hz Input')
py.grid(True)
py.savefig('10.png', dpi = 1000)

#Problem 5: Obtaining Step Response for the High-Pass Filter
(t_5, o_5, vi_5) = highpass(r1_1, r1_2, c1_1, c1_2, G1, 1/s)
vi_5 = vi_5[3]
(num_vi_5, den_vi_5) = sym_extract(vi_5)
vi_5 = sig.lti(num_vi_5, den_vi_5)
(t5_x, vo_5) = sig.impulse(vi_5, None, py.linspace(0, 0.002, 7001))

py.figure(11)
py.plot(t5_x, vo_5, 'k')
py.xlabel('t')
py.ylabel('Vo(t)')
py.title('Step Response of the High-Pass Filter')
py.grid(True)
py.savefig('11.png', dpi = 1000)

#showing all the above output plots at once
py.show()







