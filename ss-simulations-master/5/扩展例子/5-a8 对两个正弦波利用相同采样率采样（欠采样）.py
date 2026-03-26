import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftshift, fftfreq
from scipy import signal

'''演示参数'''
# 定义两段正弦的频率
f1 = 10
f2 = 30
t_length = 5  # 信号的实际时间长度
'''抽样参数
这里应使用较大，且较为“整”的采样频率，如2000、4000等
否则在get_SamplePulse函数的取整操作时会产生误差。
'''
sample_freq = 4000
sample_interval = 1 / sample_freq  # 模拟连续信号的采样间隔
'''定义时间轴'''
t = np.arange(-0, t_length, sample_interval)
'''定义信号'''
sig1 = np.cos(2 * np.pi * f1 * t)
sig2 = np.cos(2 * np.pi * f2 * t)
'''定义抽样脉冲pulse'''
fs = 40
ts = 1 / fs


def get_SamplePulse(ts):
    # 定义一个周期,注意unit_impulse要求参数为整数
    p1 = signal.unit_impulse(int(ts * sample_freq))
    # 循环拼接为一个长序列，再截断
    p = np.array([])
    while len(p) < len(t):
        p = np.append(p, p1)
    return p[:len(t)]


'''原信号乘以抽样脉冲，得到两个抽样后的信号'''
ss_1 = sig1 * get_SamplePulse(ts)
ss_2 = sig2 * get_SamplePulse(ts)

plt.figure(figsize=(16, 9), dpi=100)  # 新建绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title(r"信号1：$cos{(20\pi)}$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, sig1)

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title(r"信号2：$cos{(60\pi)}$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, sig2)

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title(r"对信号1的抽样，抽样频率为$40$Hz", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_1)
plt.plot(t, sig1, 'r--')

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title(r"对信号2的抽样，抽样频率为$40$Hz", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_2)
plt.plot(t, sig2, 'r--')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title(r"去掉包络线", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_1)

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_2)

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
