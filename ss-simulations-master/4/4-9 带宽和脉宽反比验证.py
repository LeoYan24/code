import matplotlib.pylab as plt  # 绘制图形
import numpy as np
# rom scipy.fftpack import fft,fftfreq
# rom scipy import signal
from numpy.fft import fft, fftfreq, fftshift

fs = 1024  # 采样频率
Ts = 1 / fs  # 采样间隔
N = 20
'''定义信号'''

t = np.arange(-N, N, Ts) # 一个对称区间
'''方波'''
tao = 4
f1 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
tao = 2
f2 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
tao = 1
f3 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
'''高斯函数定义1
tao = 4
f1 = 1 / np.sqrt(2 * np.pi) / tao * np.exp(-t ** 2 / (2 * tao ** 2))
tao = 2
f2 = 1 / np.sqrt(2 * np.pi) / tao * np.exp(-t ** 2 / (2 * tao ** 2))
tao = 1
f3 = 1 / np.sqrt(2 * np.pi) / tao * np.exp(-t ** 2 / (2 * tao ** 2))
'''
'''高斯函数定义2
tao = 4
f1 = np.exp(-(t / tao) ** 2)
tao = 2
f2 = np.exp(-(t / tao) ** 2)
tao = 1
f3 = np.exp(-(t / tao) ** 2)
'''
'''升余弦函数定义
tao = 8
f1 = 0.5* (1+ np.cos(np.pi*t / tao))*(np.heaviside(t+tao,1)-np.heaviside(t-tao,1))
tao = 4
f2 = 0.5*(1+ np.cos(np.pi*t / tao))*(np.heaviside(t+tao,1)-np.heaviside(t-tao,1))
tao = 2
f3 = 0.5*(1+ np.cos(np.pi*t / tao))*(np.heaviside(t+tao,1)-np.heaviside(t-tao,1))
'''
# ------------------
'''计算FFT'''
# 注意所有的频轴用的都是一个，因为他们的时间轴和采样密度等是一样的
f = fftshift(fftfreq(len(t), Ts))  # fft的双边频域坐标
f1_amp = fftshift(np.abs(fft(f1)) * Ts)  # 双边幅度谱
f2_amp = fftshift(np.abs(fft(f2)) * Ts)  # 双边幅度谱
f3_amp = fftshift(np.abs(fft(f3)) * Ts)  # 双边幅度谱

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_1 (t)$', loc='left')
plt.plot(t, f1, 'r')

plt.subplot(322)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_1 (2\pi f)|$', loc='left')
plt.plot(f, f1_amp, 'r')

plt.subplot(323)
plt.grid()
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_2 (t)$', loc='left')
plt.plot(t, f2, 'g')

plt.subplot(324)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_2(2\pi f)|$', loc='left')
plt.plot(f, f2_amp, 'g')

plt.subplot(325)
plt.grid()
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_3 (t)$', loc='left')
plt.plot(t, f3, 'b')

plt.subplot(326)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_3 (2\pi f)|$', loc='left')
plt.plot(f, f3_amp, 'b')

plt.tight_layout()  
plt.show()
