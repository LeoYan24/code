from sympy import *

s = Symbol('s')
# 变换前的系数矩阵
A = Matrix([[0, 1], [-2, -3]])
B = Matrix([[1], [2]])
P = Matrix([[1, 1], [1, -1]])
# 变换后的系数矩阵
Ahat = P * A * P.inv()
print('Ahat=', Ahat)
Bhat = P * B
print('Bhat=', Bhat)
eigenvalue = A.eigenvals(multiple=True)
# multiple=True表示输出为列表形式，否则为dict形式
print('变换前系统的特征根：', eigenvalue)
eigen_values_hat = Ahat.eigenvals(multiple=True)
print('变换后系统的特征根：', eigen_values_hat)
eigen_polynomial = det(s * eye(2) - A)
print('变换前的特征多项式：', eigen_polynomial)
eigen_polynomial_hat = det(s * eye(2) - Ahat)
print('变换后的特征多项式：', factor(eigen_polynomial_hat))
