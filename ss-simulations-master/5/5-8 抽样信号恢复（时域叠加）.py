import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift

'''信号参数'''
T = 1 / 4
Ts = T / 1000
t_length = 10 * T
t = np.arange(-t_length / 2, t_length / 2, Ts)
'''
定义一个升余弦(1+cos(2pi/T* t) t∈(0,T).脉宽=T
第一过零点带宽为（4pi/T）,转为频率是1/T/2
'''
et = (0.5 + 0.5 * np.cos(2 * np.pi / T * t - np.pi)) * (np.heaviside(t, 1) - np.heaviside(t - T, 1))
'''抽样参数'''
Ts2 = T / 8
pulses = []
for i in range(0, int(t_length / Ts2)):
    p = np.zeros_like(t)
    p[int(i * Ts2 / Ts)] = et[int(i * Ts2 / Ts)]
    pulses.append(p)

'''定义理想低通的冲激响应'''
f_l = 1 / Ts2 / 2
ht = 2 * f_l * np.sinc(2 * f_l * t) * Ts2
results = []
result = np.zeros_like(t)
for i in range(0, int(t_length / Ts2)):
    results.append(np.convolve(pulses[i], ht, mode='same'))
    result = result + results[i]

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(221)
plt.grid()  
plt.xlim(0, T)
plt.title("原信号")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)

plt.subplot(222)
plt.grid()  
plt.xlim(0, 0.25)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
for i in range(0, int(t_length / Ts2)):
    plt.plot(t, pulses[i])
plt.plot(t, et, 'r--')


plt.subplot(223)
plt.grid()  
plt.xlim(0, 0.25)
plt.title("单个抽样脉冲卷积$h(t)$（未叠加）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
for i in range(0, int(t_length / Ts2)):
    plt.plot(t, results[i])
plt.plot(t, et, 'r--')

plt.subplot(224)
plt.grid()  
plt.xlim(0, 0.25)
plt.ylim(-0.2, 1.1)
plt.title("内插信号叠加恢复为原信号")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, result)

plt.tight_layout()  
plt.show()
