import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft

tao = 0.001  # 对应频谱带宽（第一过零点）为1000Hz
Ts = tao / 100
fs = 1 / Ts
'''定义t、f'''
t = np.arange(-10, 10, Ts)
f = fftshift(fftfreq(len(t), Ts))
'''定义信号'''
# 定义一个方波信号,高度可变，Ew最大值为1
et = 1 / tao * (np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1))
# 信号频谱
Ew = fftshift(fft(fftshift(et))) * Ts
Ew_amp = np.abs(Ew)

'''画图'''
plt.figure()
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
j = 0
for i in [1, 4, 7]:
    # 通过不同的低通
    Hw = np.heaviside(f + i / tao, 1) - np.heaviside(f - i / tao, 1)
    Rw = Ew * Hw
    rt = ifftshift(ifft(ifftshift(Rw / Ts))).real

    plt.subplot(3, 1, j + 1)
    plt.grid()
    plt.xlim(- 2 * tao, 2 * tao)
    plt.title('低通截止频率：$f_c = %.0fHz$' % (i / tao), loc='left')
    plt.xlabel(r'$time\rm{(s)}$', loc='right')
    plt.plot(t, rt)
    j += 1

plt.tight_layout()
plt.show()
