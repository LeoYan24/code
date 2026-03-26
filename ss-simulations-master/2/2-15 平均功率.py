import numpy as np

n = np.arange(-20, 21)
x = np.exp(1j * np.pi * n / 8)
e = np.sum(x * np.conj(x)).real
p = e / len(x)
print(e, p)
