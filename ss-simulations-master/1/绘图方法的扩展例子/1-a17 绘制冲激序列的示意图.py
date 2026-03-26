import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(-10, 10, 0.01)
n = np.arange(-10, 10, 1)
f1c = np.sin(np.pi / 4 * t) + 1
f1 = np.sin(np.pi / 4 * n) + 1

plt.figure()  # 新建绘图
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.stem(n, f1, linefmt='r', markerfmt='^r', basefmt='none')
plt.plot(t, f1c, 'b--')

plt.show()
