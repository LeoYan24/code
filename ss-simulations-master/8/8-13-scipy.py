import numpy as np
from scipy import linalg

A = np.matrix([[1, 0], [1, -1]])
B = np.matrix([[1], [0]])  # 单列
C = np.matrix([[1, -2]])
D = np.matrix([[0]])
# 对矩阵A特征值分解
eigenvalues, eigenvectors = linalg.eig(A)
P = linalg.inv(eigenvectors)  # 对角线化，变换矩阵
print('P=', P)
# 矩阵变换
Ahat = eigenvalues
print('Ahat=', Ahat)
Bhat = P * B
print('Bhat=', Bhat)
Chat = C * linalg.inv(P)
print('Chat=', Chat)
flag_ctr = 0
for ii in range(1, A.shape[0]):
    if sum(np.abs(Bhat[ii, :])) < 1e-6:
        flag_ctr = 1
if flag_ctr == 0:
    print('系统是可控制的')
else:
    print('系统是不可控制的')
flag_obv = 0
for ii in range(1, A.shape[0]):
    if sum(np.abs(Chat[:, ii])) < 1e-6:
        flag_obv = 1
if flag_obv == 0:
    print('系统是可观察的')
else:
    print('系统是不可观察的')
