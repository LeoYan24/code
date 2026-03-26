import matplotlib.pylab as plt
import numpy as np
'''定义函数'''
n = np.arange(0, 10)
x1= np.power(2, n)  #2的n次方
x2= np.power(n, 2)  #n的2次方
'''序列图'''
plt.subplot(211)
plt.stem(n, x1)
plt.subplot(212)
plt.stem(n, x2)
plt.show()
