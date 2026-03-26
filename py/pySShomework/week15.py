import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# Define system coefficients
b = np.array([0.25,-0.7,1])
a = np.array([1, -0.7,0.25])

# 1. Pole-Zero Plot
z, p, k = signal.tf2zpk(b, a)

plt.figure(figsize=(6, 6))
# Draw unit circle
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k--', label='单位圆')

# Plot zeros and poles
plt.scatter(np.real(z), np.imag(z), s=50, marker='o', facecolors='none', edgecolors='b', label='零点')
plt.scatter(np.real(p), np.imag(p), s=50, marker='x', color='r', label='极点')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend(loc='upper right')
plt.title('零极点图')
plt.xlabel('实部')
plt.ylabel('虚部')
plt.axis('equal')

# 2. Frequency Response
w, h = signal.freqz(b, a)

plt.figure(figsize=(10, 8))

# Magnitude Response
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('幅频特性')
plt.ylabel('幅度 (dB)')
plt.xlabel('频率 (rad/sample)')
plt.grid(True)

# Phase Response
plt.subplot(2, 1, 2)
angles = np.unwrap(np.angle(h))
plt.plot(w, angles)
plt.title('相频特性')
plt.ylabel('相位 (radians)')
plt.xlabel('频率 (rad/sample)')
plt.grid(True)

plt.tight_layout()
plt.show()
