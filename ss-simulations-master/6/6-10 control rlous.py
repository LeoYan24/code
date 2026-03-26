import control as ct
import matplotlib.pylab as plt
import numpy as np

'''
B=[1]
A = np.convolve([1, -1],[1,2])
sys = ct.tf(B,A)
k=np.arange(-100,100,0.1)
ct.root_locus_plot(sys,gains =k)
plt.show()
'''

B = [1]
A = np.convolve([1, -1], [1, 2])

sys = ct.tf(B, A)
result = ct.root_locus_map(sys)
result.plot()
plt.show()
rt = result.loci.T
print(rt.shape)

'''绘图，自行画根轨迹'''

plt.figure()
plt.grid()
plt.plot(np.real(rt[1]), np.imag(rt[1]), 'x', color='none', markeredgecolor='b')
plt.plot(np.real(rt[0]), np.imag(rt[0]), 'o', color='none', markeredgecolor='r')
plt.show()
