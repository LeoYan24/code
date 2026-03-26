import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

system = ([1, 0, 0], [1, 0.3, 0.1], 1)

system = ([1], [1, 0.3, 0.1], 1)
# system =([0,0,1],[1,0.3,0.1],1)
n = np.arange(0, 10)
x = np.ones_like(n)
n, h = signal.dimpulse(system, t=n)  # 单位样值响应
n, y = signal.dlsim(system, x, t=n)  # 零状态响应（阶跃响应）

'''绘图'''
plt.subplot(2, 1, 1)
plt.stem(n, np.squeeze(h))
plt.subplot(2, 1, 2)
plt.stem(n, np.squeeze(y))
plt.show()
