import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from scipy import signal

f = 200  # 模拟角频率
fs = 8000  # 抽样频率
t = np.arange(0, 5 / f, 1 / fs)  # 信号长度，5个周期
# 定义周期方波（注意输入信号是不变的）
e = signal.square(2 * np.pi * f * t, duty=0.5)

# 计算lsim的辅助时间轴
t1 = np.arange(0, 5, 0.01)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
# 输入信号，不需要更新
ax.plot(t, e, 'r--', c='red')
# 输出信号图像
line, = ax.plot([], [])  # 横虚线
# 标注a值
tx = ax.text(0.02, -1.1, "")
ax.grid()
ax.set_title('a对冲激响应的影响')
# 设置一下xy坐标范围，否则图的坐标范围会动态变化
ax.axis([0, 0.025, -1.2, 1.2])  # 坐标范围，先x后y


def animate(i):
    a = f * i * np.pi
    # print(i,a)
    system = ([0, a], [1, a])
    tout, yout, _ = signal.lsim(system, U=e, T=t)
    # 画图
    # 更新主曲线
    # line.set_ydata(y)如果只更新ydata，则初始化的时候就要给出横坐标
    line.set_data(tout, yout)
    '''下面这一段不是必须的'''
    tx.set_text(r"$a=$%d" % int(a))  # 动态标注tao时刻

    '''上面这一段不是必须的'''
    return line, tx  # 返回值不是必须的


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=200)
# ani.save("a阶跃响应.gif", writer='pillow')
plt.show()
