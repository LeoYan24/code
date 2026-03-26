import numpy as np

n = np.arange(0, 10)
x = np.heaviside(n, 1)
z = np.cumsum(x)
print(z)

