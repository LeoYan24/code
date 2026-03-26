import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal

'''例7-14系统'''
# 根据极点得到A
p = [0.8 * np.exp(1j * np.pi / 4), 0.8 * np.exp(-1j * np.pi / 4)]
A = np.poly(p)
# 根据零点得到三种B
z_min = [0.8, 0.4]
z_mix = [1 / z_min[0], z_min[1]]
z_max = [1 / z_min[0], 1 / z_min[1]]

B_min = np.poly(z_min)
B_mix = np.poly(z_mix)
B_max = np.poly(z_max)
'''定义系统'''
dsys_min = signal.dlti(B_min, A, dt=True)
dsys_mix = signal.dlti(B_mix, A, dt=True)
dsys_max = signal.dlti(B_max, A, dt=True)

'''切换系统，求三个系统的频响特性'''
w, Hw1 = dsys_min.freqresp()
w, Hw2 = dsys_mix.freqresp()
w, Hw3 = dsys_max.freqresp()

'''零极点'''
p1 = dsys_min.poles
z1 = dsys_min.zeros
p2 = dsys_mix.poles
z2 = dsys_mix.zeros
p3 = dsys_max.poles
z3 = dsys_max.zeros

'''绘制零极点图'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(12, 3))
ax1 = plt.subplot(131)
plt.grid()
plt.title("min phase", fontsize=16)
plt.plot(p1.real, p1.imag, 'x', markersize=10, color='none', markeredgecolor='b')
plt.plot(z1.real, z1.imag, 'o', markersize=10, color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆
ax1.axis([-1.1, 2.8, -1.1, 1.1])

ax2 = plt.subplot(132)
plt.grid()
plt.title("mix phase", fontsize=16)
plt.plot(p2.real, p2.imag, 'x', markersize=10, color='none', markeredgecolor='b')
plt.plot(z2.real, z2.imag, 'o', markersize=10, color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
ax2.add_patch(unit_circle)
ax2.axis('scaled')  # 保持坐标系统正圆
ax2.axis([-1.1, 2.8, -1.1, 1.1])

ax3 = plt.subplot(133)
plt.grid()
plt.title("max phase", fontsize=16)
plt.plot(p3.real, p3.imag, 'x', markersize=10, color='none', markeredgecolor='b')
plt.plot(z3.real, z3.imag, 'o', markersize=10, color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
ax3.add_patch(unit_circle)
ax3.axis('scaled')  # 保持坐标系统正圆
ax3.axis([-1.1, 2.8, -1.1, 1.1])

plt.tight_layout()
plt.show()

'''绘制零极点和频谱特性'''
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.grid()
plt.title('Amplitude response', loc='left', fontsize=14)
l1, = plt.plot(w, np.abs(Hw1) / np.max(np.abs(Hw1)))
l2, = plt.plot(w, np.abs(Hw2) / np.max(np.abs(Hw2)), ls='--')
l3, = plt.plot(w, np.abs(Hw3) / np.max(np.abs(Hw3)), ls='-.')
plt.legend(handles=[l1, l2, l3], labels=['min phase', 'mix phase', 'max phase'], loc='best', fontsize=14)
xt = np.linspace(0, np.pi, 5)
labels = map(lambda x: f"{x / np.pi}π", xt)
plt.xticks(xt, labels)

plt.subplot(122)
plt.grid()
plt.title('Phase response', loc='left', fontsize=14)
l1, = plt.plot(w, np.unwrap(np.angle(Hw1)))
l2, = plt.plot(w, np.unwrap(np.angle(Hw2)), ls='--')
l3, = plt.plot(w, np.unwrap(np.angle(Hw3)), ls='-.')
plt.legend(handles=[l1, l2, l3], labels=['min phase', 'mix phase', 'max phase'], loc='best', fontsize=14)
xt = np.linspace(0, np.pi, 5)
labels = map(lambda x: f"{x / np.pi}π", xt)
plt.xticks(xt, labels)

plt.tight_layout()
plt.show()
