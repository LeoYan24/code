import numpy as np
import matplotlib.pylab as plt
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置（非衬线）中文字体为宋体
plt.rcParams['font.size'] = 12  # 设置字体大小
plt.rcParams['axes.unicode_minus'] = False  # 解决设置中文字体下，图像中的负号'-'显示为方块的问题

t = np.linspace(-3,3,600)
y1 = np.exp(-2*t)
y2 = np.exp(-3*t)
y3 = np.heaviside(t,1)

Y = np.convolve(y1*y3,y2*y3,mode='same')
print(Y)

plt.plot(t,Y)
plt.xlabel('时间')
plt.ylabel('幅度')
plt.legend(labels=['$e^{-2t}u(t)*e^{-2t}u(t)$'])
plt.show()
'''
plt.plot(t,y1,color='red')
plt.plot(t,y2,color='yellow')
plt.xlabel('时间')
plt.ylabel('幅度')
plt.legend(labels=['$e^{-3t}$', '$e^{-2t}$'])
plt.show()
'''