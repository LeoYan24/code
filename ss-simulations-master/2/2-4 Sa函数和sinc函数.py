import matplotlib.pylab as plt
import numpy as np

t = np.arange(-10, 10, 0.01)
np.seterr(divide='ignore', invalid='ignore')
x1 = np.sin(t) / t  # Sa函数
x2 = np.sinc(t)  # sinc函数
'''波形图'''
plt.plot(t, x1, c="r", ls="--")
plt.plot(t, x2)
plt.grid()
plt.legend(labels=['Sa(t)', 'sinc(t)'])
plt.show()
