import matplotlib.pylab as plt
import numpy as np

'''定义连续（指数）信号'''
T = 1

t1 = np.arange(0, 5*T, T / 4)
t2 = np.arange(0, 5*T,  T / 8)
t3 = np.arange(0, 5*T,  T / 16)
t4 = np.arange(0, 5*T,  T / 32)

y1 = np.sin(2 * np.pi * T * t1)
y2 = np.sin(2 * np.pi * T * t2)
y3 = np.sin(2 * np.pi * T * t3)
y4 = np.sin(2 * np.pi * T * t4)

'''波形图'''
plt.subplot(2, 2, 1)
plt.title('ts=T/4')
plt.plot(t1, y1)

plt.subplot(2, 2, 2)
plt.title('ts=T/8')
plt.plot(t2, y2)

plt.subplot(2, 2, 3)
plt.title('ts=T/16')
plt.plot(t3, y3)

plt.subplot(2, 2, 4)
plt.title('ts=T/32')
plt.plot(t4, y4)
plt.tight_layout()
plt.show()

