import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

B = [0.5, 0.5]
A = [1, 0]
dsys = signal.dlti(B, A, dt=True)
w, Hw = dsys.freqresp()
HWamp = np.abs(Hw)
phase = np.unwrap(np.angle(Hw))


'''绘制零极点和频谱特性'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(8, 4))
plt.subplot(211)
plt.grid()
plt.title('Amplitude response', loc='left')
plt.plot(w, HWamp)


plt.subplot(212)
plt.grid()
plt.title('Phase response', loc='left')
plt.plot(w, phase)

plt.tight_layout()
plt.show()
