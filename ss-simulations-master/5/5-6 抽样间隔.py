import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''抽样参数'''
T = 1 / 4  # cos信号周期 T
f = 1 / T
t_length = 10
fs = 100 * f
Ts = 1 / fs
'''定义原信号 '''
t = np.arange(-0, t_length, Ts)
sig1 = np.power(0.5, t) * np.cos(2 * np.pi / T * t + 0.125 * np.pi)


def TimeDomainSampling(fs):
    time = np.arange(-0, t_length, 1 / fs)
    sig = np.power(0.5, time) * np.cos(2 * np.pi / T * time + 0.125 * np.pi)
    return sig, time


'''2倍奈奎斯特频率抽样 '''
fs2 = 4 * f
sig2, t2 = TimeDomainSampling(fs2)
'''1倍奈奎斯特频率抽样 '''
fs3 = 2 * f
sig3, t3 = TimeDomainSampling(fs3)
'''不满足奈奎斯特频率抽样 '''
fs4 = 1.5 * f
sig4, t4 = TimeDomainSampling(fs4)

'''绘图'''
ax = plt.figure(figsize=(8, 5))  # 新建绘图，设置绘图大小
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(311)
plt.grid()
plt.xlim(0, 1)
plt.title(r"抽样频率为4倍信号频率", loc='center')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.stem(t2, sig2)
plt.plot(t, sig1, 'r--')

plt.subplot(312)
plt.grid()
plt.xlim(0, 1)
plt.title(r"抽样频率为2倍信号频率", loc='center')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.stem(t3, sig3)
plt.plot(t, sig1, 'r--')

plt.subplot(313)
plt.grid()
plt.xlim(0, 1)
plt.title(r"抽样频率为1.5倍信号频率", loc='center')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.stem(t4, sig4)
plt.plot(t, sig1, 'r--')

plt.tight_layout()  
plt.show()

