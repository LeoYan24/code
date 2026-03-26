import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft
from scipy import signal

'''
时域分析时，a = 1/RC，即1/a为时间常数，当t=(3~5)时，视为充放电结束
频域分析时，a = 1/RC，即为低通滤波器的截止（角）频率（半功率点）,截至频率则为：a/2pi
'''
a = 2 * np.pi * 100
sample_freq = 8000
sample_interval = 1 / sample_freq
'''统一画图坐标t、f和Omega'''
t = np.arange(0, 1000 / a, sample_interval)  # t的长度不能太短，否则频谱图精度不够
# 频谱范围
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
# freqresp方法需要用角频率
omega = f * 2 * np.pi

'''低通电路'''
lpf = ([a], [1, a])
'''高通电路'''
hpf = ([1, 0], [1, a])
'''求h(t)和H(jw)'''
t, ht = signal.impulse(hpf, T=t)
omega, Hw = signal.freqresp(hpf, omega)
Hw_amp = np.abs(Hw)  # 方法不是fft，不用做幅度修正
Hw_ang = np.angle(Hw)

'''绘图'''
plt.figure()
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(311)
plt.grid()  # 显示网格
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(312)
plt.grid()  # 显示网格
plt.xlim(-5 * a / 2 / np.pi, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(jf)|$', loc='left')
plt.plot(f, Hw_amp)
# 在半功率点绘制一条虚线(Hw最大值 除以根号2) * np.ones，np.ones的长度和频轴f相同
plt.plot(f, np.max(Hw_amp) / np.sqrt(2) * np.ones(len(f)), ls='--', c='red')
# 在-1/rc画一条竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
# 标注半功率点，首先指定要标注的点
xdata, ydata = a / 2 / np.pi, np.max(Hw_amp) / np.sqrt(2)

# 进行标注
plt.annotate('半功率点', (xdata, ydata),
             xytext=(10, 35),  # 标注文本的位置
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线

plt.subplot(313)
plt.grid()  # 显示网格
plt.xlim(-5 * a / 2 / np.pi, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$\phi(jf)$', loc='left')
# 由于t不是无限长，因此相位会不太准确
plt.plot(f, Hw_ang)
# 在半功率点画竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)

plt.tight_layout()
plt.show()

'''-------进一步查看滤波特性（响应能力）-------'''
# 定义一个信号
et = np.sin(0.5 * a * t) + np.sin(10 * a * t)
# 激励信号频谱
Ew = fftshift(fft(et)) * sample_interval
Ew_amp = np.abs(Ew)
'''
在频域求响应
注意：此时的Hw是用freqresp直接求出的，相当于fft方法修正了幅度，且进行了fftshift，因此需要先进行反向处理
'''
Rw = Ew * Hw  # 注意此时的Ew和Hw都进行过幅度修正（* sample_interval），因此Rw也是相当于经过幅度修正的
Rw_amp = np.abs(Rw)
rt = ifft(ifftshift(Rw / sample_interval)).real  # 先反向修正幅度，再反向修正坐标分布,最后取real，避免误差造成的告警

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$e(t)$', loc='left')
plt.plot(t, et)

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|E(j\omega)|$', loc='left')
plt.plot(f, Ew_amp)

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(j\omega)|$', loc='left')
plt.plot(f, Hw_amp)
# 在-1/rc画一条竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
plt.axvline(x=-a / 2 / np.pi, ls='--', c='r')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 2 * (2 * np.pi) / (0.5 * a))  # 根据信号的周期来卡范围，np.sin(0.5 * a * t)周期的2倍即可
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$r(t)$', loc='left')
plt.plot(t, rt)  # 注意截短

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-1.1 * (10 * a) / (2 * np.pi), 1.1 * (10 * a) / (2 * np.pi))  # 显示范围够用即可，np.sin(10 * a * t)的角频率能够显示即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|R(j\omega)|$', loc='left')
plt.plot(f, Rw_amp)

plt.tight_layout()
plt.show()
