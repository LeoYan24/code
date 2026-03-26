import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fftshift, fft, ifftshift, ifft
from scipy import signal

import filter_define  # 滤波器定义

'''
统一仿真参数
#参见filter_define.py的定义
'''
a = filter_define.a
sample_freq = filter_define.sample_freq
sample_interval = filter_define.sample_interval
t = filter_define.t
f = filter_define.f
system = filter_define.system

'''求h(t)和H(jw)'''
omega, Hw = signal.freqresp(system, f * 2 * np.pi)

# todo，定义一个扫频信号，时长为t，在时间max(t)位置达到最大频率
omega_start = int(a * 0.01)  # 起始角频率
omega_end = int(a * 10)  # 结束角频率
et = signal.chirp(t, omega_start / 2 / np.pi,
                  1000 / a,
                  omega_end / 2 / np.pi)

# 激励信号频谱
Ew = fftshift(fft(et)) * sample_interval
Ew_amp = np.abs(Ew)
'''
在频域求响应
注意：此时的Hw是用freqresp直接求出的，相当于fft方法修正了幅度，且进行了fftshift
'''
Rw = Ew * Hw  # 注意此时的Ew和Hw都进行过幅度修正（* sample_interval），因此Rw也是相当于经过幅度修正的
Rw_amp = np.abs(Rw)
rt = ifft(ifftshift(Rw / sample_interval)).real  # 先反向修正幅度，再反向修正坐标分布,最后取real，避免误差造成的告警

'''绘图'''
plt.figure()
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(211)
plt.grid()
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)
plt.plot(t, rt)
plt.legend(["输入信号", "输出信号"])

plt.subplot(212)
plt.grid()
plt.xlim(0, omega_end / 2 / np.pi)  # 显示正半频轴
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Ew_amp)
plt.plot(f, Rw_amp)
plt.legend(["输入信号幅度谱", "输出信号幅度谱"])

plt.tight_layout()
plt.show()

# todo 尝试播放信号
import sounddevice as sd

sd.play(et, sample_freq, blocking=True)
sd.play(rt, sample_freq, blocking=True)
