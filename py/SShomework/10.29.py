import numpy as np
import matplotlib.pylab as plt

a = 1
t = np.linspace(-3,3,600)
f = np.heaviside(t,1)*np.exp(-a*t)

omega = np.linspace(-3,3,600)
F = 1/(a+1j*omega)
R = F.real
I = F.imag

plt.subplot(3,1,1)
plt.plot(t,f)
plt.xlabel('t')
plt.ylabel('f(t)')

plt.subplot(3,1,2)
plt.plot(omega,R)
plt.xlabel('omega')
plt.ylabel('Re{F(omega)}')

plt.subplot(3,1,3)
plt.plot(omega,I)
plt.xlabel('omega')
plt.ylabel('Im{F(omega)}')

plt.tight_layout()
plt.show()