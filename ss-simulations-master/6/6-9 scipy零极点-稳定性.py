import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

'''(1)'''
b = [1, 0]
a = [1, 3, 2]
'''(2)
b = [1, 0]
a = [1, 0, 1]
'''
'''(3)
b = [1, 0]
a = [1, 0, -1]
'''
b = [1, 0]
a = [1, 0, 1]

t = np.arange(0, 50, 0.01)
sys = signal.lti(b, a)
p = sys.poles
z = sys.zeros
t, h = sys.impulse(T=t)
# t,h = signal.impulse(sys, t) # 等价的方法

print('零点：', z)
print('极点：', p)

'''根据极点判断系统稳定性'''
if len(p[p.real >= 0]) > 0:
    print('s右半平面存在极点，系统不稳定')
else:
    print('s右半平面不存在极点，系统稳定')

'''绘图对比'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 4))
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例

plt.subplot(gs[0])
plt.grid()
plt.plot(p.real, p.imag, marker='x', ls='None', markersize=10, color='none', markeredgecolor='b')
plt.plot(z.real, z.imag, marker='o', ls='None', markersize=10, color='none', markeredgecolor='b')

plt.subplot(gs[1])
plt.grid()
plt.plot(t, h)
plt.tight_layout()
plt.show()
