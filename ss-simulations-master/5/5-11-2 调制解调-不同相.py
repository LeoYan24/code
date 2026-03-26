import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft

fs = 4096  # 采样频率
Ts = 1 / fs  # 采样间隔
fm = 10  # 信号频率
fc = 40  # 载波频率

'''定义时间和频率轴'''
t = np.arange(0, 1, Ts)# 定义总区间
f = fftshift(fftfreq(len(t), Ts))# 定义频域长度区间
'''定义信号'''
sig = np.cos(2 * np.pi * fm * t)  # 采集的信号
carrier = np.cos(2 * np.pi * fc * t) # 调制载波
'''调制过程'''
mod_sig = sig * carrier
'''解调过程'''
# 定义多种具有相位差的本地载波
carrier2_0 = np.cos(2 * np.pi * 40 * t + np.pi * 0.125)
carrier2_1 = np.cos(2 * np.pi * 40 * t + np.pi * 0.25)
carrier2_2 = np.cos(2 * np.pi * 40 * t + np.pi * 0.5)
carrier2_3 = np.cos(2 * np.pi * 40 * t + np.pi * 0.75)
carrier2_4 = np.cos(2 * np.pi * 40 * t + np.pi)
# 已调信号乘以本地载波,再作FFT
sig0_fft = fftshift(fft(mod_sig * carrier2_0)) * Ts
sig1_fft = fftshift(fft(mod_sig * carrier2_1)) * Ts
sig2_fft = fftshift(fft(mod_sig * carrier2_2)) * Ts
sig3_fft = fftshift(fft(mod_sig * carrier2_3)) * Ts
sig4_fft = fftshift(fft(mod_sig * carrier2_4)) * Ts

'''在频域定义一个低通，并进行滤波'''
LPF_HW = 2 * np.heaviside(f + fm * 1.5, 1) - 2 * np.heaviside(f - fm * 1.5, 1)
# 反变换得到信号
RW0 = sig0_fft * LPF_HW
rt0 = ifft(ifftshift(sig0_fft * LPF_HW / Ts)).real
rt1 = ifft(ifftshift(sig1_fft * LPF_HW / Ts)).real
rt2 = ifft(ifftshift(sig2_fft * LPF_HW / Ts)).real
rt3 = ifft(ifftshift(sig3_fft * LPF_HW / Ts)).real
rt4 = ifft(ifftshift(sig4_fft * LPF_HW / Ts)).real

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()
plt.xlim(0, 0.5)
plt.title("调制信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, sig, "r--")

plt.subplot(322)
plt.grid()
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.125\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, rt0)
plt.plot(t, sig, "r--")

plt.subplot(323)
plt.grid()
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.25\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, rt1)
plt.plot(t, sig, "r--")

plt.subplot(324)
plt.grid()
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.5\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, rt2)
plt.plot(t, sig, "r--")

plt.subplot(325)
plt.grid()
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.75\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, rt3)
plt.plot(t, sig, "r--")

plt.subplot(326)
plt.grid()
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, rt4)
plt.plot(t, sig, "r--")

plt.tight_layout()
plt.show()

