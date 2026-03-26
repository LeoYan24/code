import matplotlib.pylab as plt
import numpy as np
from scipy import signal

T = 2  # 基波周期
w = 2 * np.pi / T  # 基波角频率
tao = 0.8  # 脉冲宽度
duty = tao / T  # 占空比
Ts = 0.01
t = np.arange(0, 5 * T, Ts)
# 定义一个幅度从0到1、偶对称的周期方波
Gate = 0.5 * signal.square(w * (t + tao / 2), duty=duty) + 0.5  # 周期方波，duty为占空比
# 定义原方波的直流分量
c0 = tao / T * np.ones(len(t))

# 定义一个函数，定义原方波的谐波分量
def harmonic(n, t):
    cn = 4 / T * np.sin(n * w * tao / 2) / n /w
    print(cn)
    return cn * np.cos(n * w * t)
    #return 2 / (n * np.pi) * np.sin(n * w * tao / 2) * np.cos(n * w * t)


'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(321)
plt.grid()
plt.plot(t, c0)
plt.plot(t, Gate, 'r--')
plt.title("直流分量")
for i in range(1, 6):
    plt.subplot(3, 2, i + 1)
    plt.grid()
    plt.plot(t, harmonic(i, t))
    plt.plot(t, Gate, 'r--')
    plt.title("n=%d" % i)
plt.tight_layout()
plt.show()
