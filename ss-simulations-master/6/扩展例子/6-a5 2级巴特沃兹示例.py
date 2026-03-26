import sympy as sy

'''首先调用sympy库，计算极点'''
t, s = sy.symbols('t s')
C1, C2, R1, R2 = sy.symbols('C1 C2 R1 R2')
poles = sy.roots(C1 * C2 * R1 * R2 * s ** 2 + C1 * (R1 + R2) * s + 1, s)
print(poles)
print(sy.pretty(poles))

'''调用scipy做后续分析，可以验证，两组参数的极点的模值都是一样，大概502左右'''
import numpy as np
from matplotlib import patches
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''一个有源低通系统'''
C1 = 1e-6
C2 = 1.17e-6
R1 = R2 = 1840

'''计算一组极点模值，后续绘制零级点时画圆'''
print(abs(-(R1 + R2) / (2 * C2 * R1 * R2) - np.sqrt(
    (C1 * (C1 * R1 ** 2 + 2 * C1 * R1 * R2 + C1 * R2 ** 2 - 4 * C2 * R1 * R2)) + 0j) / (2 * C1 * C2 * R1 * R2)))
r = abs(-(R1 + R2) / (2 * C2 * R1 * R2) - np.sqrt(
    (C1 * (C1 * R1 ** 2 + 2 * C1 * R1 * R2 + C1 * R2 ** 2 - 4 * C2 * R1 * R2)) + 0j) / (2 * C1 * C2 * R1 * R2))

'''定义系统：第一级'''
b1 = [1]
a1 = [C1 * C2 * R1 * R2, C1 * R1 + C1 * R2, 1]
sys1 = signal.lti(b1, a1)
omega, mag1, phase1 = sys1.bode(w=np.logspace(0, 4, 1000))
'''定义系统：第二级'''
C1 = 1e-6
C2 = 6.83e-6
R1 = R2 = 761.3
'''计算一组极点模值，后续绘制零级点时画圆，和之前计算的略有误差'''
print(abs(-(R1 + R2) / (2 * C2 * R1 * R2) - np.sqrt(
    (C1 * (C1 * R1 ** 2 + 2 * C1 * R1 * R2 + C1 * R2 ** 2 - 4 * C2 * R1 * R2)) + 0j) / (2 * C1 * C2 * R1 * R2)))
'''定义系统：第二级'''
b2 = [1]
a2 = [C1 * C2 * R1 * R2, C1 * R1 + C1 * R2, 1]
sys2 = signal.lti(b2, a2)
omega, mag2, phase2 = sys2.bode(w=np.logspace(0, 4, 1000))
'''串联之后的幅频和相频'''
mag = mag1 + mag2
phase = phase1 + phase2
f = omega / 2 / np.pi
'''画频谱图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')

plt.semilogx(f, mag1, "r--")  # Bode magnitude plot
plt.semilogx(f, mag2, 'b--')  # Bode magnitude plot
plt.semilogx(f, mag, 'g')  # Bode magnitude plot
plt.legend(['第一级', '第二级', '串联'])
plt.subplot(212)
plt.title(r'相位响应', loc='left')
plt.grid()
plt.semilogx(f, phase)  # Bode phase plot
plt.tight_layout()
plt.show()

# 零极点
p1 = sys1.poles
z1 = sys1.zeros
p2 = sys2.poles
z2 = sys2.zeros
# 手动画图
_, ax1 = plt.subplots()
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
ax1.plot(p1.real, p1.imag, 'x', c='r')
ax1.plot(z1.real, z1.imag, 'o', color='none', markeredgecolor='r')
ax1.plot(p2.real, p2.imag, 'x', c='b')
ax1.plot(z2.real, z2.imag, 'o', color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=r, fill=False, color='r', ls='--')  # 画个辅助圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

plt.tight_layout()
plt.show()

