import numpy as np
import matplotlib.pylab as plt
from scipy import signal

t = np.arange(0, 3, 0.01)
system = ([1, 3], [1, 3,2])
t, ht = signal.impulse(system, T=t)
t, gt = signal.step(system, T=t)

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(t, ht, c='b')
plt.plot(t, gt, c='r')
plt.legend(labels=['冲激响应', '阶跃响应'])
plt.show()

