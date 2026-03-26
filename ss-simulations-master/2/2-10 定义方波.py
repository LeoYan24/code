import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t = np.arange(-2, 2, 0.01)
'''方法1'''
x = 0.5 + 0.5 * signal.square(2 * np.pi * 0.5 * (t + 0.4), duty=0.4)
'''方法2'''
x = 0.5 + 0.5 * np.sign(np.cos(2 * np.pi * 0.5 * t))
'''波形图'''
plt.grid()
plt.plot(t, x)
plt.show()
