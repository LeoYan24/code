import matplotlib.gridspec as gridspec
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
'''例7-13系统'''
B = [1, -1 / 4]
A = [1, 0]
'''定义系统'''
dsys = signal.dlti(B, A, dt=1)
dsys_inv = signal.dlti(A, B, dt=1)
'''单位样值响应'''
n, hn = dsys.impulse()
n, hn_inv = dsys_inv.impulse()
'''绘制冲激响应'''
plt.subplot(211)
plt.stem(np.squeeze(hn)[:10])#或者hn_inv[0][:10]
plt.subplot(212)
plt.stem(np.squeeze(hn_inv)[:10])
plt.tight_layout()
plt.show()

'''绘制零极点和频谱特性'''
def plot_sys(dsys):
    '''零极点'''
    p = dsys.poles
    z = dsys.zeros
    '''频响'''
    w, Hw = dsys.freqresp()
    HWamp = np.abs(Hw)
    phase = np.unwrap(np.angle(Hw))

    plt.figure(figsize=(12, 4))
    gs1 = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例
    gs2 = gridspec.GridSpec(2, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例

    ax1 = plt.subplot(gs1[0])
    plt.grid()
    plt.plot(p.real, p.imag, 'x', markersize=10, color='none', markeredgecolor='b')
    plt.plot(z.real, z.imag, 'o', markersize=10, color='none', markeredgecolor='b')
    unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
    ax1.add_patch(unit_circle)
    ax1.axis('scaled')  # 保持坐标系统正圆

    plt.subplot(gs2[1])
    plt.grid()
    plt.title('Amplitude response', loc='left')
    plt.plot(w, HWamp)
    xt = np.linspace(0, np.pi, 5)
    labels = map(lambda x: f"{x / np.pi}π", xt)
    plt.xticks(xt, labels)

    plt.subplot(gs2[4])
    plt.grid()
    plt.title('Phase response', loc='left')
    plt.plot(w, phase)
    xt = np.linspace(0, np.pi, 5)
    labels = map(lambda x: f"{x / np.pi}π", xt)
    plt.xticks(xt, labels)

    plt.tight_layout()
    plt.show()

'''切换系统，求两个系统的频响特性'''
plot_sys(dsys)
plot_sys(dsys_inv)

