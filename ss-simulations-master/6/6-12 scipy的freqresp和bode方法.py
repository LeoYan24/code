import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# 参数
fc = 100
wc = 2 * np.pi * fc
# 定义系统
tf1 = signal.TransferFunction([wc], [1, wc])
tf2 = signal.TransferFunction([1, 0], [1, wc])
tf3 = signal.TransferFunction(np.convolve(tf1.num, [2 * wc]),
                              np.convolve(tf1.den, [1, 2 * wc]))
tf4 = signal.TransferFunction(np.convolve([2 * wc], tf2.num),
                              np.convolve([1, 2 * wc], tf2.den))

'''#选择一个系统进行分析'''
sys = tf1
w, Hw = sys.freqresp()
p = sys.poles
z = sys.zeros

'''绘图'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.grid()
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.plot(p.real, p.imag, marker='x', ls='None', markersize=10, color='none', markeredgecolor='b')
plt.plot(z.real, z.imag, marker='o', ls='None', markersize=10, color='none', markeredgecolor='b')
plt.title('zeros & poles', loc='left')

plt.subplot(132)
plt.grid()
Hw_dB = 20 * np.log10(np.abs(Hw))
plt.semilogx(w, Hw_dB)
plt.semilogx(w, (np.max(Hw_dB - 3)) * np.ones_like(w), 'r--')
plt.title('Amplitude response', loc='left')

plt.subplot(133)
plt.grid()
plt.title('Phase response', loc='left')
plt.semilogx(w, np.angle(Hw))

plt.tight_layout()
plt.show()

'''波特图'''
w, Hw_db, phase = sys.bode(w=np.logspace(-1, 4, 1000))

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
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
