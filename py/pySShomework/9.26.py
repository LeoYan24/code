import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0,5,500)
y = np.piecewise(x,
                 [(x<1)|((x>2)&(x<3))|(x>4),(x>=1)&(x<=2),(x>=3)&(x<=4)],
                 [lambda x:0,lambda x:x-1,lambda x:x-4])
plt.figure()
plt.plot(x,y)
plt.title('piecewise function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()