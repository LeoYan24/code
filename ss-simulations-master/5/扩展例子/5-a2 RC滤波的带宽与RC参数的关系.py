import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔

'''定义t、f'''
t = np.arange(0, 10, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))

'''绘图'''
ax = plt.figure(figsize=(16, 9), dpi=100)  # 新建绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 演示三种RC：10、30、50
for i in range(1, 6, 2):
    '''
    非理想的低通
    前面加入系数1/rc，使得频域最大值为1，方便找画功率点
    '''
    rc = i * 0.1
    ht = 1 / rc * 2 * np.pi * np.exp(-1 / rc * 2 * np.pi * t)
    Hw_amp = fftshift(np.abs(fft(ht)) * sample_interval)  # 双边幅度谱

    plt.subplot(3, 2, i)
    plt.grid()  # 显示网格
    plt.xlim(0, 0.5)
    plt.title(r"$LPF$的$h(t)$（$RC=%.1f $）" % rc)
    plt.xlabel(r'$\rm{(s)}$', loc='right')
    plt.plot(t, ht)

    plt.subplot(3, 2, i + 1)
    plt.grid()  # 显示网格
    plt.xlim(-20, 20)
    plt.title("LPF的|$(H(jf)$|（截止频率为$%.2f$）" % (1 / rc))
    plt.xlabel(r'$\rm{(rad/s)}$', loc='right')
    plt.plot(f, Hw_amp)
    # 在半功率点绘制一条虚线
    plt.plot(f, abs(np.sqrt(2)) / 2 * np.ones(len(f)), ls='--', c='red')
    # 在-1/rc画一条竖线
    plt.axvline(x=1 / rc, ls='--', c='green')

plt.suptitle("低通滤波器效果（FFT计算画图）")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"实际LPF带宽和RC的关系.jpg" , dpi=200)
exit()
