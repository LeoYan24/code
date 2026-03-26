import lcapy as lc
import sympy as sy

'''
1, 代码中大部分的lc可以和sy混用，除了lc.expr
2, 代码开头对于z的定义，以及把sympy的z转为lcapy
的z（通过lc.expr完成）目前看是必须这样做的，否则无
法进行正常的矩阵运算，如果把自定义的z改为lcapy.discretetime
的z，后续计算H这种语句很难调通
'''
z = sy.symbols('z')

A = lc.Matrix([[-1, 3], [-2, 4]])
B = lc.Matrix([[11, 0], [0, 6]])
C = lc.Matrix([[1, -1]])
D = lc.Matrix([[0, 1]])

x0 = lc.Matrix([[0], [0]])  # 初始状态
E = lc.Matrix([[1], [z / (z - 1)]])  # 激励的z域形式
F = (z * lc.eye(A.shape[0]) - A).inv()  # 求预解矩阵

H = C * F * B + D  # 系统函数
print('H= ', sy.simplify(H))

X = F * z * x0 + F * B * E
print('X= ', X)

Y = C * F * x0 + (C * F * B + D) * E
print('Y= ', Y)

Xz0 = lc.expr(str(X[0]))
Xz1 = lc.expr(str(X[1]))
Yz = lc.expr(str(Y[0]))

print('x0= ', Xz0.IZT())
print('x1= ', Xz1.IZT())
print('y= ', Yz.IZT())
