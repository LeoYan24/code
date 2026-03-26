import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

t = np.arange(-20,20,0.1)
y1 = t+1
y2 = -0.5*t+1

plt.figure()
plt.plot(t,y1,color = "blue",linewidth = 2)
plt.xlabel('t')
plt.ylabel('y')

plt.legend(title = 'f_6(t)')
plt.show()