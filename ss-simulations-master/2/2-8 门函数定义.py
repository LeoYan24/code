import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(-10.0, 10.0, 0.1)
'''定义门函数'''
# 方法1
x1 = np.heaviside(t + 1, 1) - np.heaviside(t - 1, 1)
# 方法2
x2 = np.piecewise(t, [t >= -1, t > 1], [1, 0, 0])

'''波形图'''
plt.plot(t, x1)  # 可自行选择绘制x1或x2
plt.show()
