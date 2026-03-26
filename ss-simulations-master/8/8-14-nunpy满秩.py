import numpy as np

# 变换前的系数矩阵
A = np.array([[1, 0], [1, -1]])
B = np.array([[1], [0]])  # 单列
C = np.array([1, -2])
D = np.array([0])

M = np.hstack((B, A @ B))  # 按列组合
print("M = ", M)
rank_M = np.linalg.matrix_rank(M)

N = np.array([C, C @ A])  # 横向组合
rank_N = np.linalg.matrix_rank(N)

print("M rank =", rank_M)
print("N = ", N)
print("N rank =", rank_N)
if rank_M == np.max(A.shape):
    print("M是可控制的")
else:
    print("M是不可控制的")

if rank_N == max(A.shape):
    print("N是可控制的")
else:
    print("N是不可控制的")

