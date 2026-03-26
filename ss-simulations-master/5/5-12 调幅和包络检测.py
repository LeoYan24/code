import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift
from scipy import signal

fs = 1000  # 采样频率
Ts = 1 / fs  # 采样间隔
'''定义时间和频率轴'''
# 定义总区间
t = np.arange(0, 10, Ts)
# 定义频域长度区间
f = fftshift(fftfreq(len(t), Ts))
# 叠加直流分量后的原信号（np.cos(2*np.pi*t)）
et = np.cos(2 * np.pi * t)
dc = 2 * np.ones_like(t)
# 构造载波
carrier = np.cos(20 * np.pi * t)
# 调制
mod_sig = (dc + et) * carrier
# 包络检测(基于希尔伯特-黄变换)
rt_sig = np.abs(signal.hilbert(mod_sig))
# 减去直流信号
rt = rt_sig - dc
# 原信号频谱
sig_fft_amp = fftshift(np.abs(fft(et)) * Ts)
# 调制信号频谱
mod_sig_fft_amp = fftshift(np.abs(fft(mod_sig)) * Ts)
# 减去直流信号后的还原信号频谱
rt_fft_amp = fftshift(np.abs(fft(rt)) * Ts)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(3, 2, 1)
plt.xlim(0, 2)
plt.plot(t, et)
plt.title("调制信号")

plt.subplot(3, 2, 2)
plt.plot(f, sig_fft_amp)
plt.title("原信号频谱")
plt.xlim(-30, 30)

plt.subplot(3, 2, 3)
plt.xlim(0, 2)
plt.plot(t, rt_sig, 'r--')
plt.plot(t, mod_sig)
plt.title("调幅信号")

plt.subplot(3, 2, 4)
plt.xlim(-30, 30)
plt.plot(f, mod_sig_fft_amp)
plt.title("调幅信号频谱")

plt.subplot(3, 2, 5)
plt.plot(t, rt)
plt.xlim(0, 2)
plt.title("包络检测后去除直流")

plt.subplot(3, 2, 6)
plt.xlim(-30, 30)
plt.plot(f, rt_fft_amp)
plt.title("还原信号频谱")

plt.tight_layout()
plt.show()
