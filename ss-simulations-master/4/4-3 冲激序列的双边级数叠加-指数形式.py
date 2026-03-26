import matplotlib.pylab as plt  # 绘制图形
import numpy as np

T = 1  # 定义周期
w1 = 2 * np.pi / T
t = np.arange(-1.5 * T, 1.5 * T, 0.01)
n = 50  # 谐波个数
f =np.zeros_like(t)

'''画幅度频谱图'''
for i in range(-n, n):
    f_harm = 1 / T * np.exp(1j * i * w1 * t)
    f = f + f_harm
plt.plot(t, f.real)  # 画出叠加之后的图
plt.grid()
plt.show()
