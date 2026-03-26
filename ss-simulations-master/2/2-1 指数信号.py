import matplotlib.pylab as plt
import numpy as np
'''定义连续（指数）信号'''
t = np.arange(0, 10, 0.01)
y1 = np.exp(0.5 * t)
'''定义离散信号（幂函数）和指数信号'''
n = np.arange(0, 11, 1)
y2 = np.exp(0.5 * n)
'''波形/序列图'''
plt.plot(t, y1, c="r", ls = "--")
plt.stem(n, y2)
plt.show()

