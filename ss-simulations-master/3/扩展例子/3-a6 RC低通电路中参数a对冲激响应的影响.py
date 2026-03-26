from math import exp

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from scipy import signal

# 计算impulse的辅助时间轴
t1 = np.arange(0, 5, 0.01)

'''
# 
初始化:注意这里设置的所有空值，都必须再动画中更新，否则会报错
反之，这里如果设置的初值，后续动画中可以不更新
'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 主曲线
line2, = ax.plot([], [], ls='--', c='red')  # 横虚线
# 注意axvline的x参数需要输入一个float值，np.NaN是一个float型的空值，其实这里直接用0也行，但None不行
axv = ax.axvline(x=np.NaN, ls='--', c='red')  # 竖线r
tx1 = ax.text(None, None, "")
tx2 = ax.text(None, None, "")
tx3 = ax.text(None, None, "")
ax.grid()
ax.set_title('a对冲激响应的影响')
# 设置一下xy坐标范围，否则图的坐标范围会动态变化
ax.axis([0, 5, 0, 2])  # 坐标范围，先x后y


def animate(i):
    a = i * 0.1 + 0.2  # 注意i从0开始
    # print(i,a)
    system = ([a], [1, a])
    t, y = signal.impulse(system, T=t1)  # T不是必须的参数
    # 画图
    # 更新主曲线
    # line.set_ydata(y)如果只更新ydata，则初始化的时候就要给出横坐标
    line.set_data(t, y)
    '''下面这一段不是必须的'''
    # 根据公式1/tao * e^(-t/tao)，可以得到t=tao时刻的响应信号的值（a/e）
    y_tao = a * exp(-1)
    # 绘制一条横向的虚线，其y轴刻度为y_tao,x方向上的样本点数量为: tao / 采样间隔
    num_tao = int(1 / a / 0.01)
    # 更新tao时刻的横向虚线，更新值和横轴长度
    # set_data也可以改为分别set_xdata和set_ydata
    line2.set_data(t1[:num_tao], y_tao * np.ones(num_tao))
    # 在tao位置画一条竖虚线，注意ymax可以看作是百分比，结合ylim的取值范围，这里除以2得到所需长度
    # 这里复用了t1，实际就是为了构造一个从0到tao/2——因为是比例——的序列）
    # axv也可使用set_xdata和set_ydata
    axv.set_data(1 / a * np.ones(int(y_tao / 2 / 0.01)), t1[:int(y_tao / 2 / 0.01)])
    tx1.set_text(r"$\tau=$%.2f" % (1 / a))  # 动态标注tao时刻
    tx1.set_position((1 / a, 0.01))
    tx2.set_text("%.3f" % y_tao)  # 动态标注tao时刻的y值
    tx2.set_position((0, y_tao))
    tx3.set_text("a=%.2f" % a)  # 动态标注a的位置
    tx3.set_position((0, a))
    '''上面这一段不是必须的'''
    return line, line2, axv, tx1, tx2, tx3  # 返回值不是必须的


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=200)
# ani.save("a-tau.gif", writer='pillow')
plt.show()
