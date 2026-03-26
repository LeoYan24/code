import numpy as np
import matplotlib.pylab as plt
from numpy.fft import fftfreq, fftshift, fft, ifft, ifftshift

# 公共参数
a = 1 / 2    # 时间常数
fs = 4096    # 采样频率
Ts = 1 / fs  # 采样间隔v
t = np.arange(0, 10 / a, Ts)  # 时间轴
ft = np.exp(-a * t)  # 定义时域信号
f = fftshift(fftfreq(len(t), Ts))  # 频轴
Fw = fftshift(fft(ft))  # 频谱函数
Fw_amp = np.abs(Fw * Ts)  # 幅度谱
Fw_ang = (np.angle(Fw))  # 相位谱
ft2 = ifft(ifftshift(Fw)).real  # 反变换

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(221)
plt.grid()
plt.title("原信号")
plt.xlim(0, 3 / a)
plt.plot(t, ft)

plt.subplot(222)
plt.grid()
plt.xlim(-3 * a, 3 * a)
plt.title("幅度谱")
plt.plot(f, Fw_amp)

plt.subplot(223)
plt.grid()
plt.title("反变换得到的时域信号")
plt.xlim(0, 3 / a)
plt.plot(t, ft2)

plt.subplot(224)
plt.grid()
plt.xlim(-3 * a, 3 * a)
plt.title("相位谱")
plt.plot(f, Fw_ang)
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
plt.rcParams['mathtext.fontset'] = 'stix'
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-np.pi * 1.1, np.pi * 1.1)

plt.tight_layout()
plt.show()
