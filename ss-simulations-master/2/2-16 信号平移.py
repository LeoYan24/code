import matplotlib.pylab as plt
import numpy as np
from scipy import ndimage

x = [1, 2, 3, 4, 5, 6]
n = [0, 1, 2, 3, 4, 5]
y1 = ndimage.shift(x, 2)  # 右移
y2 = ndimage.shift(x, -1)  # 左移
y3 = np.flip(x)  # 翻转

'''序列图'''
plt.subplot(221)
plt.title("x(n)", loc='left')
plt.grid()
plt.stem(n, x)

plt.subplot(222)
plt.title("$y_1$(n)", loc='left')
plt.grid()
plt.stem(n, y1)

plt.subplot(223)
plt.title("$y_2$(n)", loc='left')
plt.grid()
plt.stem(n, y2)

n1 = [-5, -4, -3, -2, -1, 0]
plt.subplot(224)
plt.title("$y_3$(n)", loc='left')
plt.grid()
plt.stem(n1, y3)

plt.tight_layout()
plt.show()
