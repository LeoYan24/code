import numpy as np
from scipy import signal

print("单根情况")
r, p, k = signal.residue([0, 0, 1], [1, 3, 2])
print(r, p, k)

print("共轭复数根")
roots = np.roots([1, 2, 5])
roots = np.append(roots, [-3])
A = np.poly(roots)
print(A)
r, p, k = signal.residue([3, 0, 1], A)
print(r, p, k)
print("共轭复数根,方式2")
A = np.convolve([1, 2, 5], [1, 3])  # full
print(A)
r, p, k = signal.residue([3, 0, 1], A)
print(r, p, k)

print("分子的阶次大于分母")
r, p, k = signal.residue([1, 5, 9, 7], [1, 3, 2])
print(r, p, k)

print("重根 ")
r, p, k = signal.residue([4, 4, 4], [1, 3, 2, 0, 0])
print(r, p, k)

print("invres逆运算")
b, a = signal.invres([1, -1], [-1, -2], [])
print(b, a)

# 时移性无法体现
