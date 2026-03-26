import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

fs = 4096  # 采样频率
Ts = 1 / fs  # 采样间隔

# ----------------------
'''定义信号'''
t = np.arange(-10, 10, Ts)
signal = np.cos(2 * np.pi * 20 * t) \
         + np.cos(2 * np.pi * 50 * t)
# 模拟三种输出
# 幅度加权不同
signal1 = 4 * np.cos(2 * np.pi * 20 * t) \
          + np.cos(2 * np.pi * 50 * t)
# 相位修正不同比例
signal2 = np.cos(2 * np.pi * 20 * t - 0.8 * np.pi) \
          + np.cos(2 * np.pi * 50 * t - 0.8 * np.pi)
# 无失真传输
signal3 = 3 * np.cos(2 * np.pi * 20 * t - 0.2 * np.pi) \
          - 3 * np.cos(2 * np.pi * 50 * t - 0.5 * np.pi)

'''计算FFT(幅度)'''
f = fftshift(fftfreq(len(t), Ts))
fft_amp = np.abs(fftshift(fft(signal))) * Ts
fft_amp1 = np.abs(fftshift(fft(signal1))) * Ts
fft_amp2 = np.abs(fftshift(fft(signal2))) * Ts
fft_amp3 = np.abs(fftshift(fft(signal3))) * Ts

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(421)
plt.grid()
plt.xlim(-1 / 10, 1 / 10)
plt.title(r"原信号：$\cos(40\pi t)+\cos(100\pi t)$", loc='left')
plt.xlabel(r'$time(s)$')
plt.plot(t, signal, 'b')

plt.subplot(422)
plt.grid()
plt.xlim(-100, 100)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp, 'b')

plt.subplot(423)
plt.grid()
plt.xlim(-1 / 10, 1 / 10)
plt.title(r"幅度加权不同：$4\cos(40\pi t)+\cos(100\pi t)$", loc='left')
plt.xlabel(r'$time(s)$')
plt.plot(t, signal1, 'r')

plt.subplot(424)
plt.grid()
plt.xlim(-100, 100)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp1, 'r')

plt.subplot(425)
plt.grid()
plt.xlim(-1 / 10, 1 / 10)
plt.title(r"时移不同：$\cos(40\pi t-0.8\pi)+\cos(100\pi t-0.8\pi)$", loc='left')
plt.xlabel(r'$time(s)$')
plt.plot(t, signal2, 'g')

plt.subplot(426)
plt.grid()
plt.xlim(-100, 100)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp2, 'g')

plt.subplot(427)
plt.grid()
plt.xlim(-1 / 10, 1 / 10)
plt.title(r"无失真传输：$3\cos(40\pi t-0.2\pi)+3\cos(100\pi t-0.5\pi)$", loc='left')
plt.xlabel(r'$time(s)$')
plt.ylabel('et')
plt.plot(t, signal3)

plt.subplot(428)
plt.grid()
plt.xlim(-100, 100)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, fft_amp3)

plt.tight_layout()  
plt.show()
exit()
