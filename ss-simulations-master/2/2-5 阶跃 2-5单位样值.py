import matplotlib.pylab as plt
import numpy as np

'''定义连续信号'''
t = np.arange(-10, 10, 0.01)
x1 = np.heaviside(t, 1 / 2)
'''定义离散信号'''
n = np.arange(-10, 10)
x2 = np.heaviside(n, 1)

'''波形图'''
plt.subplot(211)
plt.plot(t, x1)
plt.subplot(212)
plt.stem(n, x2)
plt.show()

'''定义全1信号'''
t = np.arange(0, 10.0, 0.01)
x=np.ones_like(t)
'''波形图（略）'''

'''单位样值-1'''
t = np.arange(0, 10, 1)
x1 = np.zeros_like(t)
x1[0]=1
