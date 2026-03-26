import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import animation
from numpy.fft import fft, fftfreq, fftshift, ifft, ifftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
tao = 0.5
f_l = 1 / tao  # 截止频率单位是Hz，注意低通的总宽度实际是两倍，但带宽只算正半轴
n = 10
'''定义t、f'''
t = np.arange(-10 * tao, 10 * tao, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))

# 定义一个方波信号
et = 1 / tao * (np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1))
# 信号频谱
Ew = fftshift(fft(fftshift(et))) * sample_interval
Ew_amp = np.abs(Ew)

'''图的初始化'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(12, 4))

# 第一个子图
ax1 = plt.subplot(131)
plt.grid()  # 显示网格
plt.title("原信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)
plt.axis([- 2 * tao, 2 * tao, -0.2, 1 / tao * 1.2])  # 坐标范围

# 第二个子图
ax2 = plt.subplot(132)
ax2.grid()
ti = ax2.set_title([], loc='left')
ax2.set_xlabel(r'$frequency\rm{(Hz)}$', loc='right')
line0, = ax2.plot(f, Ew_amp)  # 输入信号频谱
line1, = ax2.plot([], [], ls='--')
ax2.axis([- n * f_l, n * f_l, 0, 1.05])  # 坐标范围

# 第3个子图
ax3 = plt.subplot(133)
ax3.grid()
ax3.set_title("响应信号和原信号的对比", loc='left')
ax3.set_xlabel(r'$time\rm{(s)}$', loc='right')
line2, = ax3.plot([], [], c='red')
ax3.plot(t, et, ls='--')  # 原信号做对照组
ax3.axis([- 2 * tao, 2 * tao, -0.2, 1 / tao * 1.2])


def animate(i):
    Hw = np.heaviside(f + (i + 1) * f_l, 1) - np.heaviside(f - (i + 1) * f_l, 1)
    Rw = Ew * Hw
    rt = ifftshift(ifft(ifftshift(Rw / sample_interval))).real
    ti.set_text("低通带宽:%d Hz" % ((1 + i) * f_l))
    line1.set_data(f, Hw)
    line2.set_data(t, rt)
    return


ani = animation.FuncAnimation(fig=fig, func=animate, frames=n, interval=200, blit=False)
# ani.save("低通宽度的影响.gif", writer='pillow')
plt.show()
