import numpy as np
from scipy import linalg

# 将A、B定义为矩阵
A = np.matrix([[0, 1], [-2, -3]])
B = np.matrix([[1], [2]])
# linalg.eig的输出格式和matlab不同，不是矩阵格式
eigenvalues, eigenvectors = linalg.eig(A)
P = linalg.inv(eigenvectors)
print('P=', P)
Ahat = np.diag(eigenvalues)  # 转为对角矩阵
print('Ahat=', Ahat)
Bhat = P * B
print('Bhat=', Bhat)

exit()

# 将A、B定义为矩阵
A = np.matrix([[0, 1], [-2, -3]])
B = np.matrix([[1], [2]])
P = np.matrix([[1, 1], [1, -1]])

Ahat = P * A * linalg.inv(P)
Bhat = P * B
eigenvalues, eigenvectors = linalg.eig(A)

import sympy as sy

s = sy.Symbol('s')
sy.det(s * sy.eye(2) - A)
exit()
# linalg.eig的输出格式和matlab不同，不是矩阵格式
eigenvalues, eigenvectors = linalg.eig(A)  # ?代码可能被不小心改了
# eigvals方法只输出eigenvalues
print('eigenvalues=', eigenvalues)
print('eigenvectors=', eigenvectors)
P = linalg.inv(eigenvectors)
print('P=', P)
Ahat = np.diag(eigenvalues)  # 转为对角矩阵
print('Ahat=', Ahat)
Bhat = P * B
print('Bhat=', Bhat)

