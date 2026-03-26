import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

T = 2  # 基波周期
w = 2 * np.pi / T  # 基波角频率
tao = 1.2  # 脉冲宽度
duty = tao / T  # 占空比
t = np.arange(0, 3 * T, 0.01)  # 时间轴
# 定义一个幅度从0到1、偶对称的周期方波
Gate = 0.5 * signal.square(w * (t + tao / 2), duty=duty) + 0.5  # 周期方波，duty为占空比


# 叠加谐波的函数
def harmonic_sum(n, t):
    c0 = tao / T * np.ones(len(t))  # 直流分量
    sum_cn = c0  # 谐波叠加量的初始值
    for i in range(1, n + 1):
        Cn = 2 * tao / T * np.sinc(i * tao / T)
        sum_cn = sum_cn + Cn * np.cos(i * w * t)
    return sum_cn


'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

for i in range(1, 7):
    plt.subplot(3, 2, i)
    plt.grid()  
    plt.title("直流+%d个谐波" % (i * 10), loc='left')
    # plt.plot(t, Gate, 'r--')  # 对照组方波
    plt.plot(t, harmonic_sum(i * 10, t))  # 谐波叠加情况
plt.tight_layout()  
plt.show()
