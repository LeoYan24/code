

import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft

fs = 4096  # 采样频率
Ts = 1 / fs  # 采样间隔

f0 = 100 #正弦信号频率
t = np.arange(0, 10  , Ts)
f = fftshift(fftfreq(len(t), Ts))

ft1 = np.ones_like(t)
Fw1 = fftshift(fft(ft1))
Fw_amp1 = np.abs(Fw1 * Ts )
Fw_ang1 = np.angle(Fw1)

ft2 = np.sin(2 * f0 * np.pi * t)
Fw2 = fftshift(fft(ft2))
Fw_amp2 = np.abs(Fw2 * Ts )
Fw_ang2 = np.angle(Fw2)

ft3 = 0.5 * np.sign(np.sin(2 * f0 * np.pi * t)) + 0.5
Fw3 = fftshift(fft(ft3))
Fw_amp3 = np.abs(Fw3 * Ts )
Fw_ang3 = np.angle(Fw3)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()
plt.title("直流信号")
plt.xlim(0, 2 /f0)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ft1)

plt.subplot(322)
plt.grid()
plt.xlim(-5 * f0, 5 * f0)
plt.title("幅度谱")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Fw_amp1)

plt.subplot(323)
plt.grid()
plt.title("正弦信号")
plt.xlim(0, 2 /f0)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ft2)

plt.subplot(324)
plt.grid()
plt.xlim(-5 * f0, 5 * f0)
plt.title("幅度谱")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Fw_amp2)

plt.subplot(325)
plt.grid()
plt.title("周期方波信号")
plt.xlim(0, 2 /f0)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ft3)

plt.subplot(326)
plt.grid()
plt.xlim(-5 * f0, 5 * f0)
plt.title("幅度谱")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Fw_amp3)

plt.tight_layout()
plt.show()

