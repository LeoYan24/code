import matplotlib.pylab as plt
import numpy as np
from scipy.ndimage import shift

tao = -5  # 左移需要使用负数
n = np.arange(0, 20)
# 原始信号
x = np.sin(np.pi * n / 16)
print("原始序列：", x)
# 先经过系统，进行平移
y1 = x[::2]  # 实现系统y(n)=x(2n)
y1 = shift(y1, tao)  # 时移
# 先进行平移，在经过系统
x2 = shift(x, tao) #先将输入信号时移
y2 = x2[::2]

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
'''定义一个新的时间轴画图用，因为y(n)=x(2n)会改变时间轴的定义'''
n_ds = np.arange(0, 10)

plt.subplot(211)
plt.title("现经过系统再时移", loc='left')
plt.grid()
plt.stem(n_ds, y1)

plt.subplot(212)
plt.grid()
plt.title("先时移再经过系统", loc='left')
plt.stem(n_ds, y2)

plt.tight_layout()
plt.show()
