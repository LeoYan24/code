import matplotlib.pylab as plt
import numpy as np
import scipy.signal

#10 bit convolution
def conv(lst1,lst2):
    c=[0 for n in range(0,11)]
    for i in range (0,11):
        for j in range(0,i+1):
            c[i]=c[i]+lst1[i-j]*lst2[j]
    return c

n = np.linspace(0,10,11)
h = np.heaviside(n,1)-np.heaviside(n-6,1)
x = n*h
'''
plt.subplot(2,1,1)
plt.title('h[n]')
plt.grid()
plt.stem(n,h)

plt.subplot(2,1,2)
plt.title('x[n]')
plt.grid()
plt.stem(n,x)

plt.tight_layout()
plt.show()
'''
y=conv(h,x)
plt.stem(n,y)
plt.title('y[n]')
plt.grid();
plt.show()
