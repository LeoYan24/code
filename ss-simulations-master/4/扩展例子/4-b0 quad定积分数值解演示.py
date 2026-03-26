import matplotlib.pylab as plt
import numpy as np
from scipy import integrate

T = 2
fx = lambda x: np.exp(-2*x)
fx_quad = integrate.quad(fx, 0, T)
print(fx_quad[0])

