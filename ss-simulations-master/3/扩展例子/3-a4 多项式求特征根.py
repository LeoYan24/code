import numpy as np

x = np.array([1, 7, 16, 12])
'''
1,numpy求特征根
注意存在计算误差 [-3.         -2.00000005 -1.99999995]
'''
print(np.roots(x))
#
'''
2,sympy求特征根
有两种语法，结果是一样的，没有误差
'''
import sympy as sp

print(sp.roots([1, 7, 16, 12]))

x1 = sp.symbols('x1')
print(sp.roots(x1 ** 3 + 7 * x1 ** 2 + 16 * x1 + 12, x1))
