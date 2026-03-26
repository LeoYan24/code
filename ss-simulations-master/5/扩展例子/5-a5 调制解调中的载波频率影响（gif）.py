import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import animation
from numpy.fft import fftfreq, fftshift, fft

# 公共参数
tau = 1
sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
# 定义时间区间
t = np.arange(-tau * 20, tau * 20, sample_interval)
# 频轴
f = fftshift(fftfreq(len(t), sample_interval))
# 产生矩形脉冲信号
ft = np.heaviside(t + tau / 2, 1) - np.heaviside(t - tau / 2, 1)
# 调制信号频谱
Fw = fftshift(fft(fftshift(ft)))
# 频谱模值为
Fw_amp = np.abs(Fw * sample_interval)

# 绘图参数，支持中文和非交互式（连续动画效果）
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
fig = plt.figure()

plt.subplot(221)
plt.title("调制信号", loc='left')
plt.xlabel('t(s)', loc='right')
plt.axis([-tau, tau, -0.1, 1.2])
plt.plot(t, ft)

plt.subplot(222)
plt.title("调制信号的频谱", loc='left')
plt.xlabel(r'$f$(Hz)', loc='right')
plt.axis([-20 / tau, 20 / tau, -0.1, 1.2])
plt.plot(f, Fw_amp)

ax1 = plt.subplot(223)
ax1.set_title("已调信号", loc='left')
ax1.set_xlabel('t(s)', loc='right')
ax1.axis([-tau, tau, -1.2, 1.2])
line1, = ax1.plot([], [], 'r')

ax2 = plt.subplot(224)
ax2.set_title("已调信号频谱", loc='left')
ax2.set_xlabel(r'$f$(Hz)', loc='right')
ax2.axis([-20 / tau, 20 / tau, -0.1, 1.2])
line2, = ax2.plot([], [], 'r')


def animate(i):
    carry = np.cos(np.pi * (i + 1) * 2 * t)
    f_mod = ft * carry
    Fw_mod = fftshift(fft(fftshift(f_mod)))
    # 模值为
    Fw_mod_amp = np.abs(Fw_mod * sample_interval)

    line1.set_data(t, f_mod)
    line2.set_data(f, Fw_mod_amp)
    ax1.set_title(r"已调信号$fc=%d(Hz)$" % (i + 1), loc='left')


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=300)
# ani.save("a-tau.gif", writer='pillow')
plt.tight_layout()
plt.show()
