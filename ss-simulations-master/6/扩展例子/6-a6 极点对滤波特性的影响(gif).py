import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
# 注意画圆在patches
from matplotlib import patches
from scipy import signal

wn = 10 * 2 * np.pi

'''图的初始化'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

fig = plt.figure(figsize=(12, 5))
# 第一个子图，显示特征根的变化
ax1 = plt.subplot(121)
# 分别画圆、画点、标签
unit_circle = patches.Circle((0, 0), radius=wn, fill=False, color='black', ls='--')
ax1.add_patch(unit_circle)
# scat = plt.scatter([], [], marker='x', c='r')
poles, = ax1.plot([], [], 'x', c='b')
tx1 = ax1.text(0, 0.03, "")  # 显示zeta的值
# 对图效果做美化
ax1.grid()
ax1.axis('scaled')  # 保持坐标系统正圆
ax1.axis([-3 * wn, wn, -1.1 * wn, 1.1 * wn])  # 坐标范围
# 第二个子图，显示响应的阻尼变化
ax2 = plt.subplot(122)
ax2.grid()
line2, = ax2.semilogx([], [])
'''
注意，如果不用下面方式设置坐标范围，则plot等可能无法正确更新
'''
ax2.axis([0, 1000, -100, 100])  # 坐标范围


def animate(i):
    zeta = i / 10
    print(zeta)
    b = [wn ** 2]
    a = [1, 2 * zeta * wn, wn ** 2]
    sys = signal.lti(b, a)
    # 零极点
    p = sys.poles
    z = sys.zeros
    # 波特图
    omega, mag, phase = sys.bode(w=np.logspace(0, 4, 1000))
    f = omega / 2 / np.pi
    poles.set_data(p.real, p.imag)
    line2.set_data(f, mag)
    tx1.set_text(r"$\zeta=%.1f$" % zeta)
    return poles, line2, tx1  # 返回值不是必须的


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=300)
# ani.save("极点对滤波特习惯的影响.gif", writer='pillow')
plt.show()
