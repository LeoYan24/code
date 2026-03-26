import matplotlib.pyplot as plt
import numpy as np
from control import matlab  # 该工具集提供了部分
from scipy import signal

f = 200  # 模拟角频率
fs = 8000
N = 200
a = f * 2 * np.pi
'''
注意映射时间的方法
时间长度：按照8000的采样率，定义200个，因此总时间为 200/8000秒
下面语句的意思是先说采集200个点，再把他们除以采样频率，映射到所需的时间区间内
'''
t = np.arange(0, N) / fs
# 等价于：
# t = np.arange(0, N/fs ,1/ fs)
# 定义一个余弦
e1 = np.cos(2 * np.pi * f * t)
# 定义周期方波
e2 = signal.square(2 * np.pi * f * t, duty=0.5)
# 选一个信号做分析
e = e1

system = matlab.TransferFunction([0, a], [1, a])

ht, tout = matlab.impulse(system, T=t)
gt, tout = matlab.step(system, T=t)
yout, tout, xout = matlab.lsim(system, U=e, T=t)

# 上图是冲激响应
plt.subplot(3, 1, 1)
plt.grid()
plt.plot(t, ht)

# 中图是阶跃响应
plt.subplot(3, 1, 2)
plt.grid()
plt.plot(t, gt)

# 下图是零状态响应
plt.subplot(3, 1, 3)
plt.grid()
plt.plot(tout, yout)
plt.plot(t, e, 'r--')

plt.tight_layout()
plt.show()
