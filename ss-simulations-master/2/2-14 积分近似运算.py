import numpy as np
import matplotlib.pylab as plt

delta = 0.01
t = np.arange(0, 10, delta)
x = np.heaviside(t, 1)
z = np.cumsum(x) * delta
print(z)
'''波形图'''
plt.grid()
plt.plot(t, z)
plt.show()