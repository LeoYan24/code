from sympy import *

s = Symbol('s')
A = Matrix([[-1, -2, -1], [0, -3, 0], [0, 0, -2]])  # 3*3矩阵
B = Matrix([[2], [1], [1]])  # 1*3
C = Matrix([[1, -1, 0]])  # 3*1
D = Matrix([0])
eigen_polynomial = factor(det(s * eye(A.shape[0]) - A))
print('特征方程为eigen_polynomial=', eigen_polynomial, '=0')
F = (s * eye(A.shape[0]) - A).inv()  # 特征矩阵
H = C * F * B + D
print('系统转移函数矩阵为：', simplify(H))
