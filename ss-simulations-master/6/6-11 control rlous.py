import control as ct
import matplotlib.pylab as plt
import numpy as np

B = [1, 40, 600, 4000, 10000]
A = [1, -1, 123, 50, 2500]
n = np.arange(0, 500)
k = np.power(1.05, n) - 1

# 考虑K>=0时
sys = ct.tf(B, A)
result = ct.root_locus_map(sys, gains=k)
rt1 = result.loci.T
# result.plot(xlim=[-10, 0], ylim=[-15, 15])
# plt.show()

# 考虑K<=0时
sys = ct.tf(-1 * np.array(B), A)
result = ct.root_locus_map(sys, gains=k)
rt2 = result.loci.T
# result.plot(xlim=[-20, 20], ylim=[-15, 15])
# plt.show()

'''自行绘图'''
plt.subplot(2, 1, 1)
plt.grid()
plt.xlim(-15, 2)
plt.plot(np.real(rt1[0]), np.imag(rt1[0]), marker='o', color='none', markeredgecolor='b')
plt.plot(np.real(rt1[1]), np.imag(rt1[1]), marker='o', color='none', markeredgecolor='r')
plt.plot(np.real(rt1[2]), np.imag(rt1[2]), marker='o', color='none', markeredgecolor='g')
plt.plot(np.real(rt1[3]), np.imag(rt1[3]), marker='o', color='none', markeredgecolor='black')
plt.title('K > 0')

plt.subplot(2, 1, 2)
plt.grid()
plt.xlim(-15, 2)
plt.plot(np.real(rt2[0]), np.imag(rt2[0]), marker='o', color='none', markeredgecolor='b')
plt.plot(np.real(rt2[1]), np.imag(rt2[1]), marker='o', color='none', markeredgecolor='r')
plt.plot(np.real(rt2[2]), np.imag(rt2[2]), marker='o', color='none', markeredgecolor='g')
plt.plot(np.real(rt2[3]), np.imag(rt2[3]), marker='o', color='none', markeredgecolor='black')
plt.title('K < 0')

plt.tight_layout()
plt.show()

condition = (np.real(rt1) > -15) & (np.real(rt1) < 0) & (np.imag(rt1) < 5) & (np.imag(rt1) > -5)
all_satisfy_line = np.all(condition, axis=0)
filtered_rt = rt1[:, all_satisfy_line]
filtered_k = result.gains[all_satisfy_line]

print(len(result.gains), rt1.shape, len(rt1[0]))
print(len(filtered_k), filtered_rt.shape, len(filtered_rt[0]))

'''自行绘图'''
plt.grid()
plt.plot(np.real(filtered_rt[0]), np.imag(filtered_rt[0]), marker='o', color='none', markeredgecolor='b')
plt.plot(np.real(filtered_rt[1]), np.imag(filtered_rt[1]), marker='o', color='none', markeredgecolor='r')
plt.plot(np.real(filtered_rt[2]), np.imag(filtered_rt[2]), marker='o', color='none', markeredgecolor='g')
plt.plot(np.real(filtered_rt[3]), np.imag(filtered_rt[3]), marker='o', color='none', markeredgecolor='black')
plt.show()

'''自行绘图'''
plt.grid()
plt.plot(filtered_k)
plt.show()
