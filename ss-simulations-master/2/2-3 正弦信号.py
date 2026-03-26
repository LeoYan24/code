import matplotlib.pylab as plt
import numpy as np
'''定义连续正弦信号'''
omega = 0.5 * np.pi
T = 2 * np.pi / omega
t = np.arange(0, T * 2, 0.01)
x1 = np.sin(omega * t)
'''定义离散正弦信号'''
ts = 0.5  # 抽样间隔
n = np.arange(0, T / ts * 2)
x2 = np.sin(omega * ts * n)
'''波形/序列图'''
plt.subplot(211)
plt.plot(t, x1)
plt.subplot(212)
plt.stem(n, x2)
plt.show()
