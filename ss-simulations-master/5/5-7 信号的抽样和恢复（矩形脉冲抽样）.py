import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft
from scipy import signal

'''抽样参数'''
# 定义抽样周期
T = 1 / 4  # cos信号周期 T
fs = 1000 / T
Ts = 1 / fs
'''
定义t、f
所定义信号、抽样脉冲的实际样本点个数为: t_length * Ts
'''
t = np.arange(0, 20 * T, Ts)
f = fftshift(fftfreq(len(t), Ts))

'''情况1：定义一个频域有限信号sin函数（原信号）'''
et1 = np.cos(2 * np.pi / T * t + 0.125 * np.pi)
'''情况2：定义一个升余弦(1+cos(2pi/T* t) t∈(0,T)'''
et2 = (0.5 + 0.5 * np.cos(2 * np.pi / T * t - np.pi)) * (np.heaviside(t, 1) - np.heaviside(t - T, 1))
'''情况3：定义一个带高频噪音的信号'''
et3 = np.cos(2 * np.pi / T * t + 0.125 * np.pi) + 0.2 * np.cos(2 * np.pi / T * 6 * t + 0.125 * np.pi)
'''选择一种情况'''
et = et1

'''定义抽样脉冲pulse'''
Ts2 = T /8  #T/8 T/4  T/1.5
w1 = 2 * np.pi / Ts2
tao = 0.5 * Ts2
GatePulse = 0.5 * signal.square(w1 * t, duty=tao / Ts2) + 0.5

'''时域相乘得到抽样信号'''
sampled_et = et * GatePulse

'''计算FFT'''
Ew = fftshift(fft(et)) * Ts
PULSEw = fftshift(fft(GatePulse)) * Ts
SampledEw = fftshift(fft(sampled_et)) * Ts

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(321)
plt.grid()
plt.xlim(0, 3 * T)
plt.title("原信号")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)

plt.subplot(322)
plt.grid()
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("原信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(Ew))

plt.subplot(323)
plt.grid()
plt.xlim(0, 3 * T)
plt.title("抽样脉冲")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, GatePulse)

plt.subplot(324)
plt.grid()
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("抽样脉冲（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(PULSEw))

ax = plt.subplot(325)
plt.grid()
plt.xlim(0, 3 * T)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
ax.plot(t, sampled_et)

plt.subplot(326)
plt.grid()
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("抽样信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(SampledEw))

plt.tight_layout()  
plt.show()

'''------------------------------------------------------------------------'''
'''抽样信号恢复'''
'''从频域定义理想低通'''
f_l = 1 / Ts2 / 2  # lpf截止频率应该大于1/T，且小于（1/Ts2 - 1/T）
Hw2_amp = Ts2 / tao * (np.heaviside(f + f_l, 1) - np.heaviside(f - f_l, 1))  # 注意滤波器的高度要求
'''抽样信号通过理想低通'''
RECON_Ew = SampledEw * Hw2_amp  # 恢复的信号（频域）
recon_et = ifft(ifftshift(RECON_Ew / Ts)).real  # 恢复的信号（时域）

'''绘图'''
plt.subplot(221)
plt.grid()
plt.xlim(0, 1)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, sampled_et)

plt.subplot(222)
plt.grid()
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("抽样信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(SampledEw))
# 修正了低通高度使得显示更美观,但不能用来解读数值
plt.plot(f, tao / Ts2 * Hw2_amp * np.max(np.abs(SampledEw)), 'r--')

plt.subplot(223)
plt.grid()
plt.xlim(0, 1)
plt.title("抽样信号还原（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, recon_et)

plt.subplot(224)
plt.grid()
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("抽样信号还原（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(RECON_Ew))

plt.tight_layout()
plt.show()
