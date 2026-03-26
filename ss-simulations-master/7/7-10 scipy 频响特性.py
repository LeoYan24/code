import matplotlib.pylab as plt  # 绘制图形
import numpy as np

w = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
Hw = (1 + np.exp(-1j * w)) / 2

'''绘制零极点和频谱特性'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(8, 4))
plt.subplot(211)
plt.grid()
plt.title('Amplitude response', loc='left')
plt.plot(w, np.abs(Hw))

plt.xticks([-3 * np.pi, -2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, np.pi, 3 * np.pi])
xt = np.linspace(- 3 * np.pi, 3 * np.pi, 7)
labels = map(lambda x: f"{x / np.pi}π", xt)
plt.xticks(xt, labels)

plt.subplot(212)
plt.grid()
plt.title('Phase response', loc='left')
plt.plot(w, np.angle(Hw))

xt = np.linspace(- 3 * np.pi, 3 * np.pi, 7)
labels = map(lambda x: f"{x / np.pi}π", xt)
plt.xticks(xt, labels)

plt.tight_layout()
plt.show()

'''方式2
B = [0.5,0.5]
A = [1,0]
dsys = signal.dlti(B, A, dt=True)
w = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
w, Hw = dsys.freqresp(w=w)\
'''
