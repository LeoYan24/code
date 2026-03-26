import matplotlib.pylab as plt  # 绘制图形
import numpy as np

T = 1  # 定义周期
w1 = 2 * np.pi / T
t = np.arange(-1.5 * T, 1.5 * T, 0.01)
n = 50  # 谐波个数
f = np.ones_like(t) / T  # 相当于直流分量

'''画幅度频谱图'''
for i in range(1, n):
    f_harm = 2 * np.cos(i * w1 * t) / T
    plt.plot(t, f_harm, linewidth=0.2)  # 绘制各次谐波
    f = f + f_harm
plt.plot(t, f)  # 画出叠加之后的图
plt.grid()
plt.show()
