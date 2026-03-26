import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
# 注意画圆在patches
from matplotlib import patches
from scipy import signal

'''展示特征根的解析解'''
import sympy as sy

x = sy.symbols('x')
R, L, C = sy.symbols('R L C')
rts = sy.roots(x ** 2 + R / L * x + 1 / L / C, x)
print(sy.pretty(rts))

t1 = np.arange(0, 20, 0.01)
'''图的初始化'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(12, 5))
# 第一个子图，显示特征根的变化
ax1 = plt.subplot(121)
# 分别画圆、画点、标签
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='black', ls='--')
ax1.add_patch(unit_circle)
scat = plt.scatter([], [], marker='x', c='r')
tx1 = ax1.text(-2, 0.01, "")
# 对图效果做美化
ax1.grid()
ax1.axis('scaled')  # 保持坐标系统正圆
ax1.axis([-2, 1, -1.5, 1.5])  # 坐标范围
# 定义坐标轴（边框）的位置，绑定定原点，

ax1.spines['bottom'].set_position(('data', 0))  # 实际修改的也是边框
ax1.spines['left'].set_position(('data', 0))  # 实际修改的也是边框
ax1.spines[['top', 'right']].set_visible(False)  # 隐藏不需要的轴（边框）
# 第二个子图，显示响应的阻尼变化
ax2 = plt.subplot(122)
ax2.grid()
line1, = ax2.plot([], [])
'''
注意，如果不用下面方式设置坐标范围，则plot等可能无法正确更新
'''
ax2.axis([0, 20, -1, 1])  # 坐标范围


def animate(i):
    L = 1
    C = 1
    R = i * 0.1  # i是整数，模拟R从0.1变到3左右
    # 求特征根
    x = np.array([1, R / L, 1 / L / C])
    rts = np.roots(x)
    # 求曲线
    system = ([1 / L / C], [1, R / L, 1 / L / C])
    t, y = signal.impulse(system, T=t1)
    line1.set_data(t, y)
    # 目前看只能逐点更新，每个点的位置是一个list，点的个数要和初始情况相同，所有点再放到一个元组里
    scat.set_offsets(([rts[0].real, rts[0].imag], [rts[1].real, rts[1].imag]))
    tx1.set_text(r"$R=$%.2f" % R)
    return line1, scat, tx1  # 返回值不是必须的


ani = animation.FuncAnimation(fig=fig, func=animate, frames=25, interval=200)
# ani.save("四种阻尼.gif", writer='pillow') #存储为gif
plt.show()
