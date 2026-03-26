import matplotlib.pylab as plt
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft

# 公共参数
E = 1
tao = 1
fs = 4096  # 采样频率
Ts = 1 / fs  # 采样间隔
# 注意，arange的区间对称性问题，下面的定义方式保证了区间是对称的，或者可以使用linespace函数
# 如果区间不对称，可能导致频域结果出现额外的相位差
t = np.arange(-10 * tao, 10 * tao + Ts, Ts)
# 频轴，范围为正负sample_freq/2
f = fftshift(fftfreq(len(t), Ts))
# 定义时域信号：门函数
ft = E * np.heaviside(t + tao / 2, 1) - E * np.heaviside(t - tao / 2, 1)

'''
fft
1，由于时间轴为对称区间，所以先对其进行fftshift，再做fft
2，fft出来的结果需要再做一次fftshfit，才能对应到之前定义的f轴上
'''
ft1 = fftshift(ft)
Fw = fftshift(fft(ft1))
# 模值为：
Fw_amp = np.abs(Fw * Ts)
# 对于门函数频谱，可以直接用Fw或Fw取实部，可以更好的展示Sa函数的样子
# Fw_amp = Fw.real * Ts
Fw_ang = np.angle(Fw)
'''
ifft
1，由于Fw之前做过fftshift，所以这里在ifft之前做一次ifftshift
2，由于计算Fw的ft，先进行过fftshift，因此ifft的结果，也需要在进行一次ifftshift
'''
ft2 = ifft(ifftshift(Fw)).real
ft2 = ifftshift(ft2)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(221)
plt.grid()
plt.title("原信号")
plt.xlim(-3 * tao, 3 * tao)
plt.plot(t, ft)

plt.subplot(222)
plt.grid()
plt.xlim(-3 / tao, 3 / tao)
plt.title("幅度谱")
plt.plot(f, Fw_amp)

plt.subplot(223)
plt.grid()
plt.title("反变换得到的时域信号")
plt.xlim(-3 * tao, 3 * tao)
plt.plot(t, ft2)

plt.subplot(224)
plt.grid()
plt.xlim(-3 / tao, 3 / tao)
plt.title("相位谱")
plt.plot(f, Fw_ang)
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-np.pi * 1.1, np.pi * 1.1)  # 如果y坐标设置的过多，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()
