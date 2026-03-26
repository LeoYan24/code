import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t = np.arange(0, 3, 0.01)
system = ([2, 0], [1, 3])
t, ht = signal.impulse(system, T=t)
t, gt = signal.step(system, T=t)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(t, ht, c='b')
plt.plot(t, gt, c='r',ls="--")
plt.legend(labels=['冲激响应', '阶跃响应'])
plt.show()
