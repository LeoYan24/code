import time
import matplotlib.pylab as plt
import numpy as np
from numpy.fft import fft, ifft, fftshift, ifftshift
from scipy import signal

fs = 4096  # 采样频率
Ts = 1 / fs  # 采样间隔
t = np.arange(-10, 10, Ts)
# 定义两个方波信号
ft1 = ft2 = np.heaviside(t + 0.5, 1) - np.heaviside(t - 0.5, 1)

'''进行时域卷积，并统计运算时间'''
start_time = time.time()
rt1 = np.convolve(ft1, ft2, mode='same') * Ts
end_time = time.time()
print('直接卷积开销:', end_time - start_time)

'''计算信号的fft，做乘积再做反变换，并统计运算时间'''
start_time = time.time()
Fw1 = fft(fftshift(ft1)) * Ts
Fw2 = fft(fftshift(ft2)) * Ts
Rw = Fw1 * Fw2
rt2 = np.real(ifftshift(ifft(Rw / Ts)))  # 反向归一化
end_time = time.time()
print('频域计算开销:', end_time - start_time)

'''计算信号的fft，做乘积再做反变换，并统计运算时间'''
start_time = time.time()
rt3 = signal.fftconvolve(ft1, ft2, mode='same') * Ts
end_time = time.time()
print('fftconvolve计算开销:', end_time - start_time)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(311)
plt.grid()
plt.xlim(-2, 5)
plt.title(r'时域直接卷积结果', loc='left')
plt.plot(t, rt1)

plt.subplot(312)
plt.grid()
plt.xlim(-2, 5)
plt.title(r'频域计算结果', loc='left')
plt.plot(t, rt2)

plt.subplot(313)
plt.grid()
plt.xlim(-2, 5)
plt.title(r'fftconvolve计算结果', loc='left')
plt.plot(t, rt3)

plt.tight_layout()  
plt.show()
exit()
