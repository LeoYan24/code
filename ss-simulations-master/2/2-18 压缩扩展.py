import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(-10.0, 10.0, 0.01)  # 采样点：取-10.0到10.0，间隔为0.01
# 原始信号
a = 1
y_t = np.piecewise(t, [t >= 0, t >= 2, t >= 3], [1, lambda x: 3 - a * x, 0, 0])  # lambda中的x是局部变量
'''信号压缩扩展'''

a = 2  # y(2t)，即所有的t都变成2t
y_2t = np.piecewise(t, [a * t >= 0, a * t >= 2, a * t >= 3], [1, lambda x: 3 - a * x, 0, 0])
a = 0.5  # y(1/2t)，即所有的t都变成1/2t
y_05t = np.piecewise(t, [a * t >= 0, a * t >= 2, a * t >= 3], [1, lambda x: 3 - a * x, 0, 0])

'''波形图'''
plt.subplot(311)
plt.grid()
plt.plot(t, y_t)

plt.subplot(312)
plt.grid()
plt.xlim((-10, 10))
plt.plot(t, y_2t)

plt.subplot(313)
plt.grid()
plt.xlim((-10, 10))
plt.plot(t, y_05t)
plt.tight_layout()
plt.show()
