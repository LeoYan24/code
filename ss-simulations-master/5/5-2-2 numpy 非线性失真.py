import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

fs = 1024  # 采样频率
Ts = 1 / fs  # 采样间隔
# ----------------------
'''定义信号'''
t = np.arange(-10, 10, Ts)
signal = 3 * np.cos(2 * np.pi * 10 * t)
# 削顶
signal1 = np.where((signal >= 1.5), 1.5, signal)
# 削底
signal2 = np.where((signal <= -1.5), -1.5, signal)
# 交越失真
'''交越失真的产生原因是乙类推挽功放中b-e（发射结）产生的0.7v分压，因此一般交越失真的量在0.7v左右'''
signal3 = np.where((signal >= -0.7) & (signal <= 0.7),
                   0, np.sign(signal) * (abs(signal) - 0.7))

'''计算FFT(幅度)'''
f = fftshift(fftfreq(len(t), Ts))
fft_amp = np.abs(fftshift(fft(signal))) * Ts
fft_amp1 = np.abs(fftshift(fft(signal1))) * Ts
fft_amp2 = np.abs(fftshift(fft(signal2))) * Ts
fft_amp3 = np.abs(fftshift(fft(signal3))) * Ts

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(321)
plt.grid()
plt.xlim(0, 3 / 10)  # 根据之前定义的cos角频率，3/10就是三个周期
plt.ylim(-4, 4)
plt.title("原信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, signal)
# 双边谱
plt.subplot(322)
plt.grid()
plt.xlim(-50, 50)
plt.title("原信号幅度谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp)

plt.subplot(323)
plt.grid()
plt.xlim(0, 3 / 10)  # 根据之前定义的cos角频率，3/10就是三个周期
plt.ylim(-4, 4)
plt.title("信号削顶", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
# plt.plot(t, signal, 'r--')
plt.plot(t, signal1, 'g')

plt.subplot(324)
plt.grid()
plt.xlim(-50, 50)
plt.title("削顶信号的幅度谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp1, 'g')

plt.subplot(325)
plt.grid()
plt.xlim(0, 3 / 10)  # 根据之前定义的cos角频率，3/10就是三个周期
plt.ylim(-4, 4)
plt.title("交越失真", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
# plt.plot(t, signal, 'r--')
plt.plot(t, signal3, 'b')

plt.subplot(326)
plt.grid()
plt.xlim(-50, 50)
plt.title("交越失真信号的幅度谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp3, 'b')

plt.tight_layout()  
plt.show()
