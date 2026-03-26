import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import animation

# 定义心形函数
theta = np.arange(0, np.pi * 2, 0.01)  # 0到2pi，角度取弧度

# 建立极坐标绘图（projection参数设置为极坐标），方式1
fig = plt.figure()
ax = plt.subplot(111, projection='polar')
# 绘图
polygon1, = plt.fill([], [], c="r")  # 填充
line1, = plt.plot([], [], c="b")  # 描边
# 建议显式设置一个合适范围
ax.set_rgrids(np.arange(0, 10, 2), [])  # 半径网格（刻度）的取值和角度,不显示半径大小


def animate(i):
    a = i - 10
    r = (4 + np.sin(a)) / np.sqrt(1 - np.abs(np.cos(theta)) * np.sin(theta))  # 新型曲线，大小随a变化
    polygon1.set_xy(np.array([theta, r]).T)  # 参数形状为(N,2)
    line1.set_data(theta, r)
    return r


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=100)

plt.show()
