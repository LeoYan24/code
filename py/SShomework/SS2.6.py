import matplotlib.pylab as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

t = np.arange(-1,1,0.00025)
x = 3*np.cos(200*t+np.pi/6)
y = x*x

plt.figure(figsize=(30,5))
plt.subplot(2,1,1)
plt.title('x(t)')
plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x')

plt.subplot(2,1,2)
plt.title('y(t)')
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y')

plt.suptitle('4-2波形图')
plt.tight_layout()
plt.show()