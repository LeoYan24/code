import matplotlib.pylab as plt
import numpy as np

T = 1
t = np.arange(0, 3 * T, 0.01)
x = 5 * np.exp(-1j * 2 * np.pi / T * t) + 5 * np.exp(1j * 2 * np.pi / T * t) \
    + 2 * np.exp(-3j * 2 * np.pi / T * t) + 2 * np.exp(3j * 2 * np.pi / T * t)

'''绘图'''
plt.plot(t, x)
plt.grid()
plt.show()
