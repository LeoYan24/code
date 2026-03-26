'''
方式1，采用sympy库
'''
import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3')

# 语法1：
result = sp.solve([x1 - 2 * x2 + 3 * x3 - 1,
                   2 * x1 + 3 * x2 + x3 - 2,
                   3 * x1 - x2 - x3 - 4],
                  [x1, x2, x3])
print(result, type(result))  # 输出类型为字典类型
print("-----------------------")
# 语法2：
result = sp.solve([x1 + x2 - 21 / 50 - 1, -x1 - 6 * x2 + 3 / 25], [x1, x2])
print(result)
print("-----------------------")
# 语法3：解一元高次方程
result = sp.solve([x1 ** 3 + 7 * x1 ** 2 + 16 * x1 + 12], [x1])
print(result)
print("-----------------------")
'''
方式2，采用numpy库的solve函数
'''
import numpy as np
from numpy.linalg import solve

# 2,解线性方程组
a = np.array([[1, -2, 3], [2, 3, 1], [3, -1, -1]])  # 同语法1的题目
b = np.array([1, 2, 4])
# 求解
x = solve(a, b)
print(x)
