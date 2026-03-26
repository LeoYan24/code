import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import animation
from numpy.fft import fftfreq, fftshift, ifft, ifftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
tao = 0.5
f_l = 1 / tao  # 截止频率单位是Hz，注意低通的总宽度实际是两倍，但带宽只算正半轴
n = 20
'''定义t、f'''
t = np.arange(-10 * tao, 10 * tao, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))

'''图的初始化'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(12, 4))
# 第一个子图
ax1 = plt.subplot(121)
ax1.grid()
t1 = ax1.set_title([], loc='left')
ax1.set_xlabel(r'$frequency\rm{(Hz)}$', loc='right')
line0, = ax1.plot([], [], )  # 输入信号频谱
ax1.axis([- n * f_l, n * f_l, 0, 1.1])  # 坐标范围
# 第二个子图
ax2 = plt.subplot(122)
ax2.grid()  # 显示网格
ax2.set_title(r"理想低通的$h(t)$", loc='left')
ax2.set_xlabel(r'$time\rm{(s)}$', loc='right')
line1, = ax2.plot([], [])
ax2.axis([- 1 / f_l, 1 / f_l, -5, n * 2])  # 坐标范围


def animate(i):
    Hw = np.heaviside(f + (i * 0.5 + 1) * f_l, 1) - np.heaviside(f - (i * 0.5 + 1) * f_l, 1)
    ht = ifftshift(ifft(ifftshift(Hw / sample_interval))).real
    t1.set_text("低通带宽:%d Hz" % ((1 + i * 0.5) * f_l))
    line0.set_data(f, Hw)
    line1.set_data(t, ht)
    return


ani = animation.FuncAnimation(fig=fig, func=animate, frames=n, interval=200, blit=False)
# ani.save("低通带宽和时域宽度.gif", writer='pillow')
plt.show()
