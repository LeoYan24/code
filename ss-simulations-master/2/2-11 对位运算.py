import matplotlib.pylab as plt
import numpy as np

t = np.arange(0, 1.0, 0.001)
y1 = np.sin(10 * t) * np.sin(100 * t)
y2 = np.sin(10 * t) + np.sin(100 * t)
'''波形图'''
plt.subplot(211)
plt.plot(t, y1)
plt.subplot(212)
plt.plot(t, y2)
plt.show()
