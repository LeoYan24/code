import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# 时间轴
t = np.arange(-10, 10, 0.01)
'''
初始化:注意这里设置的所有初值（空值），都必须再动画中更新，否则会报错
反之，这里如果设置的初值，后续动画中可以不更新
'''
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False
# 如果只有一个子图，用ax
fig, ax = plt.subplots()
ax.grid()
ax.set_title('曲线的动画')
'''注意，如果不用下面方式设置坐标范围，则曲线可能无法正确更新'''
ax.axis([-1, 1, -1, 1])  # 坐标范围
# 初始化2条曲线
line1, = ax.plot([], [])
line2, = ax.plot([], [], ls='--', c='red')


def animate(i):
    f1 = np.sin(10 * t - i)
    f2 = np.cos(10 * t - i)
    '''图1：更新折线：plot采用set_data方法更新数据，参数就是x和y的序列'''
    line1.set_data(t, f1)
    line2.set_data(t, f2)
    return


# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=200)

ani.save("a-tau-1.gif", writer='pillow')
plt.show()
