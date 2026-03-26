import control as ct
import matplotlib.pylab as plt
import numpy as np
from control import matlab
from scipy import signal

t = np.arange(0, 2.1, 0.01)  # 样本
e = np.heaviside(t, 1)  # 激励信号为u(t)
x0 = [1, 2]
A = [[1, 0], [1, -3]]
B = [[1], [0]]
C = [-0.25, 1]
D = [0]

# sys_tf = ct.ss2tf(A, B, C, D)

sys = signal.StateSpace(A, B, C, D)
t_out, y, x = signal.lsim(sys, e, t, x0, interp=True)

sys = ct.StateSpace(A, B, C, D)
y, t_out, x = matlab.lsim(sys, e, t, x0)

y0 = np.exp(-3 * t) * 11 / 6 - np.ones_like(t) / 12  # 给出理论值做对比

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8.0, 4.0))
# 系统状态
plt.subplot(121)
plt.plot(t, (x.T)[0], c='r', ls='--')
plt.plot(t, (x.T)[1], c='b', ls='-.')
plt.plot(t, y, c='g')
plt.legend(['$x_1 (t)$', '$x_2 (t)$', '$y(t)$'])
plt.xlabel('时间 (s)')

plt.subplot(122)  # 图2
plt.plot(t, y - y0)
plt.xlabel('时间 (s)')
plt.ylabel('误差')

plt.tight_layout()  # 紧凑显示图形
plt.show()
