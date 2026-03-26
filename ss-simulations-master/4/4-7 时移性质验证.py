import matplotlib.pylab as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift
from scipy.ndimage import shift

fs = 2048  # 采样频率
Ts = 1 / fs  # 采样间隔

'''定义信号'''
t = np.arange(0, 20, Ts)
f1 = np.exp(-2 * t)
'''
信号平移
使用scipy的shift函数，注意参数为正时为右移
平移的数值是 平移的时间距离 * 单位距离采样点的个数
'''
f2 = shift(f1, 2 * fs)
f3 = shift(f1, 4 * fs)

'''计算FFT'''
# 注意所有的频轴用的都是同一个
f = fftshift(fftfreq(len(t), Ts))  # fft的双边频域坐标
fw1 = fftshift(fft(f1))
fw2 = fftshift(fft(f2))
fw3 = fftshift(fft(f3))
# 幅度谱
f1_amp = np.abs(fw1) * Ts
f2_amp = np.abs(fw2) * Ts
f3_amp = np.abs(fw3) * Ts
# 相位谱
f1_ang = np.angle(fw1)
f2_ang = np.angle(fw2)
f3_ang = np.angle(fw3)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(331)
plt.grid()
plt.xlim(0, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f (t)$', loc='left')
plt.plot(t, f1)

plt.subplot(332)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f1_amp)

plt.subplot(333)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱', loc='left')
plt.plot(f, f1_ang)

plt.subplot(334)
plt.grid()
plt.xlim(0, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f(t-2)$', loc='left')
plt.plot(t, f2, 'r')

plt.subplot(335)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f2_amp, 'r')

plt.subplot(336)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱', loc='left')
plt.plot(f, f2_ang, 'r')

plt.subplot(337)
plt.grid()
plt.xlim(0, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f (t-4)$', loc='left')
plt.plot(t, f3, 'g')

plt.subplot(338)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f3_amp, 'g')

plt.subplot(339)
plt.grid()
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱', loc='left')
plt.plot(f, f3_ang, 'g')

plt.tight_layout()  
plt.show()
