import sympy as sy

s = sy.symbols('s')
# 变换前的系数矩阵
A = sy.Matrix([[1, 0], [1, -1]])

B = sy.Matrix([[1], [0]])  # 单列
C = sy.Matrix([[1, -2]])
D = sy.Matrix([[0]])

M = sy.Matrix([[B, A * B]])
rank_M = M.rank()
N = sy.Matrix([C, C * A])
rank_N = N.rank()

print("M = ", M)
print("M rank =", rank_M)
print("N = ", N)
print("N rank =", rank_N)
if rank_M == max(A.shape):
    print("M是可控制的")
else:
    print("M是不可控制的")

if rank_N == max(A.shape):
    print("N是可控制的")
else:
    print("N是不可控制的")

'''
M =  Matrix([[1, 1], [0, 1]])
M rank = 2
N =  Matrix([[1, -2], [-1, 2]])
N rank = 1
M是可控制的
N是不可控制的
'''
