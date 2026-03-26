import numpy as np
import matplotlib.pylab as plt
from scipy import signal

f=10
t=np.linspace(0,1,1000)
x=np.sin(2*np.pi*f*t)
T=1/f
delta=0.001

y=x[0:100]
plt.plot(y)
plt.show()

x1 = signal.resample(x, 50)
plt.plot(x1)
plt.show()
