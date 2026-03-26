import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches
from scipy import signal

fc = 10
wc = fc * 2 * np.pi
N = 3 #阶数
k = np.power(wc, N) #增益
'''(1)butter函数输出ba'''
#注意函数中使用fc而非wc，后续画辅助圆也是用fc
b, a = signal.butter(N, fc, 'low', analog=True)
z, p, k = signal.tf2zpk(b * np.power(wc, N) , a)
sys = signal.lti(b , a )
omega, mag, phase = sys.bode()

'''(2)butter函数输出zpk
z, p, k= signal.butter(N, fc, 'low', analog=True, output='zpk')
omega, Hw = signal.freqs_zpk(z, p, k)
mag = 20 * np.log10(np.abs(Hw))
phase = np.angle(Hw)
'''
f = omega / 2 / np.pi

# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')
plt.semilogx(f, mag)  # Bode magnitude plot
# 在半功率点绘制一条虚线,长度和频轴f相同
plt.semilogx(f, -3 * np.ones_like(f), 'r--')

plt.subplot(212)
plt.title(r'相位响应', loc='left')
plt.grid()
plt.semilogx(f, phase)  # Bode phase plot
# plt.ylim(-3.2,3.2)
plt.tight_layout()
plt.show()

# 零极点手动画图
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
poles = plt.plot(p.real, p.imag, 'x', c='b')
# zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')
# 画个辅助圆
ax1 = plt.subplot()
unit_circle = patches.Circle((0, 0), radius=fc, fill=False, color='r', ls='--')
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

plt.tight_layout()
plt.show()


