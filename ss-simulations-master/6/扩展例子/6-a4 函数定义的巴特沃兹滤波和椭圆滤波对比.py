import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

# 截止频率
fp = 1000
wp = 2 * np.pi * fp
# 通带波纹
rp = -20 * np.log10(1 - 0.05)
# 阻带波纹
rs = -20 * np.log10(0.05)
# 滤波器阶次
N = 4
# 这个范围给的是频率，不是角频率
w = np.linspace(0, fp * 4, 1001) * 2 * np.pi
# Matlab中的“s”应该就是python的 analog=True
b1, a1 = signal.butter(N, wp, 'low', analog=True)
w1, H1 = signal.freqs(b1, a1, w)
# 椭圆滤波器
b2, a2 = signal.ellip(N, rp, rs, wp, 'low', analog=True)
w2, H2 = signal.freqs(b2, a2, w)
# 画图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
# 幅频特性
ax = plt.subplot(2, 1, 1)
ax.plot(w1 / (2 * np.pi), abs(H1), ls='--', c='blue')
ax.plot(w2 / (2 * np.pi), abs(H2), c='red')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅频特性')
plt.legend(['巴特沃兹滤波器', '椭圆滤波器'])
plt.grid()
# 阶跃响应
t = np.linspace(0, 10 / fp, 1001)
t1, h1 = signal.step((b1, a1), T=t)
t2, h2 = signal.step((b2, a2), T=t)
ax = plt.subplot(2, 1, 2)
ax.plot(t1 * 1000, h1, ls='--', c='blue')
ax.plot(t2 * 1000, h2, c='red')
plt.xlabel('时间 (ms)')
plt.ylabel('阶跃响应')
plt.legend(['巴特沃兹滤波器', '椭圆滤波器'])
plt.grid()

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
