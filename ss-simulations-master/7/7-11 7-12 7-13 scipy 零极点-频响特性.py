import matplotlib.gridspec as gridspec
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal

'''例7-11系统定义'''
a1 = 0.5  # -0.5 0 0.5
B = [1, 0]
A = [1, -a1]

'''例7-12系统定义
B=[1,0,0]
r=0.9 #0.98 0.9
phai=np.pi/4 #np.pi/4 0 3*np.pi/4
p1=r*np.exp(1j*phai)
p2=np.conj(p1)
A=np.poly([p1, p2])
'''

'''例7-13系统定义
B = [0.25, -1 * np.sqrt(3) / 2, 1]
A = [1, -1 * np.sqrt(3) / 2, 0.25]
'''
'''定义系统'''
dsys = signal.dlti(B, A, dt=1)
'''方式1：离散频谱特性'''
w, Hw = dsys.freqresp()
HWamp = np.abs(Hw)
phase = np.unwrap(np.angle(Hw))

'''方式2：频谱特性(db坐标)
w, HWamp, phase = dsys.bode()
'''

'''零极点'''
poles = dsys.poles
zeros = dsys.zeros
'''获得非重复的元素，以及元素的个数'''
z, cz = np.unique(zeros, return_counts=True)  # [-0.5  0. ] [1 2]
p, cp = np.unique(poles, return_counts=True)

'''绘制零极点和频谱特性'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(12, 4))

gs1 = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例
gs2 = gridspec.GridSpec(2, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例

ax1 = plt.subplot(gs1[0])
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
