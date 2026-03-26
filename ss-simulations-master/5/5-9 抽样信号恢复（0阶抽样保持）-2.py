import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft
from scipy import signal

'''抽样参数'''
T = 1 / 2
Ts = T / 4096
Ts2 = T / 16  # 抽样间隔，零界保持其的宽度
t_length = 10 * T
t = np.arange(0, 10 * T, Ts)
f = fftshift(fftfreq(len(t), Ts))
'''
定义一个升余弦(1+cos(2pi/T* t) t∈(0,T).脉宽=T
第一过零点带宽为（4pi/T）,转为频率是1/T/2
'''
et = (0.5 + 0.5 * np.cos(2 * np.pi / T * t - np.pi)) * (np.heaviside(t, 1) - np.heaviside(t - T, 1))

'''直接定义抽样结果'''
sample_et = np.zeros_like(t)
for i in range(0, int(t_length / Ts2)):
    p = np.zeros_like(t)
    p[int(i * Ts2 / Ts)] = et[int(i * Ts2 / Ts)]
    sample_et += p

SampleEw = fftshift(fft(sample_et)) * Ts

'''抽样信号通过0阶抽样保持'''
ht = np.heaviside(t, 1) - np.heaviside(t - Ts2, 1)
recon_et = np.convolve(sample_et, ht)[:len(t)]  # * sample_interval
RECON_Ew = fftshift(fft(recon_et)) * Ts

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()  
plt.xlim(0, 1)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, sample_et)
plt.plot(t, et, 'r--')

plt.subplot(222)
plt.grid()  
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("抽样信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(SampleEw))

plt.subplot(223)
plt.grid()  
plt.xlim(0, 1)
plt.title("还原信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, recon_et)

plt.subplot(224)
plt.grid()  
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("还原信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(RECON_Ew))

plt.tight_layout()  
plt.show()



'''------------------------------------------------------------------------'''
'''进一步进行信号平滑'''
'''RC低通电路'''
f_l = 1 / Ts2 / 2
a = 2 * np.pi * f_l
lpf = ([a], [1, a])
t, ht = signal.impulse(lpf, T=t)
Hw = fftshift(fft(ht)) * Ts

'''抽样信号通过理想低通'''
RECON_Ew2 = RECON_Ew * Hw  # 恢复的信号（频域）
recon_et2 = ifft(ifftshift(RECON_Ew2 / Ts)).real  # 恢复的信号（时域）

'''绘图'''
plt.subplot(221)
plt.grid()  
plt.xlim(0, 1)
plt.title("还原信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, recon_et)

plt.subplot(222)
plt.grid()  
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("还原信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(RECON_Ew))
plt.plot(f,  np.abs(Hw) * np.max(np.abs(RECON_Ew)), 'r--')

plt.subplot(223)
plt.grid()  
plt.xlim(0, 1)
plt.title("滤波后信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, recon_et2)

plt.subplot(224)
plt.grid()  
plt.xlim(-5 * T / Ts2, 5 * T / Ts2)
plt.title("滤波后信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(RECON_Ew2))

plt.tight_layout()  
plt.show()
