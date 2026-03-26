import matplotlib.pylab as plt
import numpy as np
import sympy as sy

# 定义sympy自变量和表达式
t = sy.symbols('t')
y_sy = sy.Piecewise((t, sy.And(t > 0, t < 5)), (0, True))
# 将sympy表达式转为numpy方法
f_sy = sy.lambdify(t, y_sy, "numpy")
# 定义一个numpy时间轴，并利用转换的方法生成函数序列
t_1 = np.arange(0, 10, 0.01)
y_np = f_sy(t_1)
'''绘图'''
plt.plot(t_1, y_np)
plt.show()
