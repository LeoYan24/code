import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

wn = 1
zeta = 0  # 取值范围：0 0.25 1 2
B = [1]
A = [1, 2 * zeta * wn, wn ** 2]
sys = signal.TransferFunction(B, A)
w, Hw_db, phase = sys.bode()
p = sys.poles
z = sys.zeros

'''绘图'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(12, 3))
plt.subplot(131)
plt.grid()
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.plot(p.real, p.imag, marker='x', ls='None', markersize=10, color='none', markeredgecolor='b')
plt.plot(z.real, z.imag, marker='o', ls='None', markersize=10, color='none', markeredgecolor='b')
plt.title('zeros & poles', loc='left')

plt.subplot(132)
plt.grid()
plt.semilogx(w, Hw_db)
plt.semilogx(w, (np.max(Hw_db - 3)) * np.ones_like(w), 'r--')
plt.title('Amplitude response', loc='left')

plt.subplot(133)
plt.grid()
plt.title('Phase response', loc='left')
plt.semilogx(w, phase)

plt.tight_layout()
plt.show()
