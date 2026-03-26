import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal

'''例7-6'''
A = [1, 0, 0, 0, 0, 0, 0]
B = np.ones(7) / 7
'''例7-7'''
B = [1, 0.5, 0, 0]
A = [1, -1.25, 0.75, -0.125]

dsys = signal.dlti(B, A, dt=1)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
# 零极点
poles = dsys.poles
zeros = dsys.zeros
'''获得非重复的元素，以及元素的个数'''
z, cz = np.unique(zeros, return_counts=True)  # [-0.5  0. ] [1 2]
p, cp = np.unique(poles, return_counts=True)
fig, ax1 = plt.subplots()
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
for i in range(len(p)):
    plt.plot(p[i].real, p[i].imag, 'x', markersize=10, color='none', markeredgecolor='b')
    if cp[i] > 1:
        plt.text(p[i].real + 0.05, p[i].imag + 0.05, cp[i], fontsize=12)

for i in range(len(z)):
    plt.plot(z[i].real, z[i].imag, 'o', markersize=10, color='none', markeredgecolor='b')
    if cz[i] > 1:
        plt.text(z[i].real + 0.05, z[i].imag + 0.05, cz[i], fontsize=12)

unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')  # 画个单位圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆
plt.show()
