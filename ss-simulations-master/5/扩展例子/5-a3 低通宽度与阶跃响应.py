import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft

# 演示参数
sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
'''
改为较小的脉冲宽度，会使得门函数带宽增大
此时通过较窄的低通，可能使得输出图形失真严重，难以被检测
'''
tao = 0.2  # 0.2或1  # 门宽度,实际门宽度
'''定义t、f'''
t = np.arange(-10, 10, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))
'''定义信号'''
# 定义一个方波信号,高度可变，Ew最大值为1
et = 1 / tao * (np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1))
# 信号频谱
Ew = fftshift(fft(fftshift(et))) * sample_interval
Ew_amp = np.abs(Ew)

'''画图'''
plt.figure(figsize=(16, 9), dpi=100)
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(3, 3, 4)
plt.grid()  # 显示网格
plt.xlim(- 2, 2)
plt.title("原信号$G_{%.1f}(t)$" % tao, loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et, color='green')

for i in range(1, 8, 3):
    # 通过不同的低通
    Hw = np.heaviside(f + (i + 1), 1) - \
         np.heaviside(f - (i + 1), 1)
    Rw = Ew * Hw
    rt = ifftshift(ifft(ifftshift(Rw / sample_interval))).real

    # 绘图
    plt.subplot(3, 3, i + 1)  # i+1就是截止频率
    plt.grid()  # 显示网格
    plt.xlim(- 10, 10)
    plt.title('低通截止频率：$f_c = %dHz$' % (i + 1), loc='left')
    plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
    plt.plot(f, Ew_amp, color='green')
    plt.plot(f, Hw, "r--")

    plt.subplot(3, 3, i + 2)
    plt.grid()  # 显示网格
    plt.xlim(- 2, 2)
    plt.title("响应（时域）")
    plt.xlabel(r'$time\rm{(s)}$', loc='right')
    plt.plot(t, rt)
    plt.plot(t, et, 'g--')

plt.suptitle("低通滤波器带宽与阶跃响应")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
