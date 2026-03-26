import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-20, 21)
#n = np.arange(0, 20)
x = np.heaviside(n, 1) - np.heaviside(n - 10, 1)
h = np.heaviside(n, 1) - np.heaviside(n - 5, 1)
y = np.convolve(x, h, mode='same')
#y = np.convolve(x, h)

'''绘图'''
plt.subplot(3, 1, 1)
plt.xlim(-20, 20)
plt.stem(n, x)

plt.subplot(3, 1, 2)
plt.xlim(-20, 20)
plt.stem(n, h)

plt.subplot(3, 1, 3)
plt.xlim(-20, 20)
#对应same模式
plt.stem(n, y)
#对应full模式
#plt.stem(np.arange(0, len(y)), y)
plt.tight_layout()
plt.show()
