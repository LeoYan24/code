import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal

B = [1, 0, 0, 0]
A = [1, -3, 3, -1]

dsys = signal.dlti(B, A, dt=True)
'''离散冲激响应'''
w, Hw = dsys.freqresp()

'''离散冲激响应'''
n, h = dsys.impulse(n=10)
'''零极点'''
poles = dsys.poles
zeros = dsys.zeros
poles = np.around(poles, decimals=5)

print(poles, zeros)
'''根据极点判断系统稳定性'''
if len([np.abs(poles) >= 1]) > 0:
    print('存在单位圆外（上）的极点:%s，系统不稳定' % (poles[np.abs(poles) >= 1]))
else:
    print('系统稳定')

'''获得非重复的元素，以及元素的个数'''
z, cz = np.unique(zeros, return_counts=True)  # [-0.5  0. ] [1 2]
p, cp = np.unique(poles, return_counts=True)

'''绘制零极点图'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

plt.figure(figsize=(12, 4))
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例

ax1 = plt.subplot(gs[0])
plt.grid()
for i in range(len(p)):
    plt.plot(p[i].real, p[i].imag, 'x', markersize=10, color='none', markeredgecolor='b')
    if cp[i] > 1:
        plt.text(p[i].real - 0.1, p[i].imag + 0.05, cp[i], fontsize=12)

for i in range(len(z)):
    plt.plot(z[i].real, z[i].imag, 'o', markersize=10, color='none', markeredgecolor='b')
    if cz[i] > 1:
        plt.text(z[i].real + 0.05, z[i].imag + 0.05, cz[i], fontsize=12)

unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

plt.subplot(gs[1])
plt.grid()
plt.stem(n, h[0])

plt.tight_layout()
plt.show()
