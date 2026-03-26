import matplotlib.pylab as plt
import numpy as np
from matplotlib import patches
from scipy import signal

wc = 10 * np.pi
N = 4
k = np.power(wc, N)

'''H(s)H(-s)'''
B1 = [1]
A1 = np.append([np.power(1 / 1j / wc, 2 * N)], np.zeros(2 * N - 1))
A1 = np.append(A1, [1])
sys1 = signal.TransferFunction(B1, A1)
poles1 = sys1.poles

'''H(s)'''
B2 = [np.power(wc, N)]
A1_roots = np.roots(A1)
A2 = np.poly(A1_roots[A1_roots.real < 0])
sys2 = signal.TransferFunction(B2, A2)
poles2 = sys2.poles

'''H(s)第2种定义方法'''
B3, A3 = signal.butter(N, wc, 'low', analog=True)
sys3 = signal.TransferFunction(B3, A3)
poles2 = sys3.poles

'''绘图'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(8, 4))

ax1 = plt.subplot(121)
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
plt.title("H(s)H(-s)")
plt.plot(poles1.real, poles1.imag, marker='x', ls='None', markersize=10, color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=wc, fill=False, color='r', ls='--')  # 画个辅助圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

ax1 = plt.subplot(122)
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
plt.title("H(s)")
plt.plot(poles2.real, poles2.imag, marker='x', ls='None', markersize=10, color='none', markeredgecolor='b')
unit_circle = patches.Circle((0, 0), radius=wc, fill=False, color='r', ls='--')  # 画个辅助圆
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

plt.tight_layout()
plt.show()

'''H(s)频谱特性'''
w, Hw_db, phase = sys2.bode()

'''绘图'''
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.grid()
plt.semilogx(w, Hw_db)
plt.semilogx(w, (np.max(Hw_db - 3)) * np.ones_like(w), 'r--')
plt.title('Amplitude response', loc='left')

plt.subplot(122)
plt.grid()
plt.title('Phase response', loc='left')
plt.semilogx(w, phase)

plt.tight_layout()
plt.show()
