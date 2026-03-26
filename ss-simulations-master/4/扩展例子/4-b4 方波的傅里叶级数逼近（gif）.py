import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import animation
from scipy import signal

# 定义周期
T1 = 1
w1 = 2 * np.pi / T1
tao = 0.5
# 范围
t = np.arange(-2 * T1, 2 * T1, 0.01)
n = 20
# 定义一个周期方波
Gate = 0.5 * signal.square(w1 * (t + tao / 2), duty=tao / T1) + 0.5  # 周期方波，duty为占空比

'''图的初始化'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = plt.subplot()
ti = ax.set_title([], loc='left')
ax.grid()  # 显示网格
ax.set_xlabel(r'$time\rm{(s)}$', loc='right')
ax.plot(t, Gate, "r--")
# ax.plot(t, Gate, 'r--')  # 对照组方波
line1, = ax.plot([], [])
ax.axis([-2 * T1, 2 * T1, -0.2, 1.2])  # 坐标范围


# 叠加谐波的函数
def harmonic(n, t):
    ft0 = tao / T1 * np.ones(len(t))  # 直流分量
    ft = ft0  # 直流分量
    # 利用for循环，在ft基础上依次叠加方波，叠加个数由n决定，注意开闭区间的问题
    for i in range(1, n + 1):
        Cn = 2 * tao / T1 * np.sinc(i * tao / T1)
        ft = ft + Cn * np.cos(i * w1 * t)
    return ft


def animate(i):
    harms = harmonic
    line1.set_data(t, harmonic(i * 2, t))
    ti.set_text("谐波个数:%d" % (1 + i))
    return


ani = animation.FuncAnimation(fig=fig, func=animate, frames=n, interval=200)
# ani.save("方波的cos谐波叠加.gif", writer='pillow')
plt.show()
