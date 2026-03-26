import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifft, ifftshift
from scipy import signal

fc = 1000
a = 2 * np.pi * fc
fs = fc * 100
Ts = 1 / fs
t = np.arange(0.0, 100 / a, Ts)
f = fftshift(fftfreq(len(t), Ts))

'''低通电路'''
lpf = ([a], [1, a])
'''高通电路'''
hpf = ([1, 0], [1, a])
'''选一个系统'''
sys = hpf
t, ht = signal.impulse(sys, T=t)
Hw = fftshift(fft(ht)) * Ts
# 如果系统的是高通，则需要解决impulse方法无法给出h(t)冲激项的问题
if sys == hpf:
    Hw = (np.ones(len(f)) + Hw)
'''得到幅度谱和相位谱'''
Hw_amp = np.abs(Hw)
Hw_ang = np.angle(Hw)
print(f[int(len(Hw) / 2) - 5:int(len(Hw) / 2) + 5])
print(Hw[int(len(Hw) / 2) - 5:int(len(Hw) / 2) + 5])
print(Hw_ang[int(len(Hw) / 2) - 5:int(len(Hw) / 2) + 5])

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(121)
plt.grid()
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(222)
plt.grid()
plt.xlim(-2 * fc, 2 * fc)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(2\pi f)|$', loc='left')
plt.plot(f, Hw_amp)
# 在半功率点绘制一条虚线
plt.plot(f, abs(np.max(Hw_amp)) / np.sqrt(2) * np.ones(len(f)), ls='--', c='red')
# 在-1/rc画一条竖线
plt.axvline(x=a, ls='--', c='green')

plt.subplot(224)
plt.grid()
plt.xlim(-2 * fc, 2 * fc)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$\phi(2\pi f)$', loc='left')
plt.plot(f, Hw_ang)

plt.tight_layout()
plt.show()

'''-------进一步查看滤波特性（响应能力）-------'''
#单个正弦波
et = np.sin(0.5 * a * t)
Ew = fftshift(fft(et)) * Ts  # 激励信号频谱
Rw = Ew * Hw  # 注意此时的Ew和Hw都进行过幅度修正（* Ts），因此Rw也是相当于经过幅度修正的
rt = ifft(ifftshift(Rw / Ts)).real  # 先反向修正幅度，再反向修正坐标分布,最后取real，避免误差造成的告警
'''绘图'''
plt.grid()
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.ylim(-2,2)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et, "r--")
plt.plot(t, rt)
plt.legend(['e(t)', 'r(t)'])
plt.show()

'''-------进一步查看滤波特性（响应能力）-------'''
#一个低频正弦波加一个高频正弦波
et = np.sin(0.5 * a * t) + np.sin(10 * a * t)
Ew = fftshift(fft(et)) * Ts  # 激励信号频谱
Rw = Ew * Hw  # 注意此时的Ew和Hw都进行过幅度修正（* Ts），因此Rw也是相当于经过幅度修正的
rt = ifft(ifftshift(Rw / Ts)).real  # 先反向修正幅度，再反向修正坐标分布,最后取real，避免误差造成的告警
'''绘图'''
plt.subplot(321)
plt.grid()
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.ylim(-2,2)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$e(t)$', loc='left')
plt.plot(t, et)

plt.subplot(322)
plt.grid()
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|E(2\pi f)|$', loc='left')
plt.plot(f, np.abs(Ew))

plt.subplot(323)
plt.grid()
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(324)
plt.grid()
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(2\pi f)|$', loc='left')
plt.plot(f, Hw_amp)
# 在-1/rc画一条竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
plt.axvline(x=-a / 2 / np.pi, ls='--', c='r')

plt.subplot(325)
plt.grid()
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.ylim(-2,2)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$r(t)$', loc='left')
plt.plot(t, rt)  # 注意截短

plt.subplot(326)
plt.grid()
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|R(2\pi f)|$', loc='left')
plt.plot(f, np.abs(Rw))

plt.tight_layout()
plt.show()
