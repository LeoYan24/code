import sympy as sy

s, t = sy.symbols('s t')
# 系数矩阵
A = sy.Matrix([[1, 2], [0, -1]])
B = sy.Matrix([[0, 1], [1, 0]])
C = sy.Matrix([[1, 1], [0, -1]])
D = sy.Matrix([[1, 0], [1, 0]])

x0 = sy.Matrix([[1], [0]])  # 状态起始值

et = sy.Matrix([[0], [sy.Heaviside(t)]])  # 输入
Es = sy.laplace_transform(et, t, s, legacy_matrix=False, noconds=True)
print(sy.eye(A.shape[0]))

F = (s * sy.eye(A.shape[0]) - A).inv()  # 求预解矩阵
# F = (s * sy.eye(2) - A).inv()
print('特征矩阵（预解矩阵）F:', sy.simplify(F))
Hs = C * F * B + D  # 系统函数
print('系统函数H:', sy.simplify(Hs))
Ys = C * F * x0 + Hs * Es  # 输出的拉普拉斯变换
y = sy.inverse_laplace_transform(Ys, s, t)  # 实际输出
print('输出y(t):', sy.simplify(y))
