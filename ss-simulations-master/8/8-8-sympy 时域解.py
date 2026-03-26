import sympy as sy

s, t = sy.symbols('s t')
A = sy.Matrix([[-1, -4], [1, -1]])
B = sy.Matrix([[0, 1], [1, 0]])
C = sy.Matrix([[1, 1], [0, -1]])
D = sy.Matrix([[1, 0], [1, 0]])

F = sy.exp(t * A)  # 求解矩阵指数函数
# F = simplify(F) #简化完了反而复杂
print('F=', sy.exp_polar(F))
'''状态方程求解'''
# 输入
et = sy.Matrix([[sy.Heaviside(t)], [sy.exp(-t) * sy.Heaviside(t)]])
Es = sy.laplace_transform(et, t, s, legacy_matrix=False, noconds=True)
# 状态起始值
x0 = sy.Matrix([[2], [1]])
# 状态的零状态解
# 如果不加入legacy_matrix=False，则输出为元组
# 输出值不是表达式，还包含收敛条件，例如(1/s, 0, True)
# 加入noconds=True，不输出收敛条件
xzi = F * x0  # 状态的零输入解
Fs = sy.laplace_transform(F * B, t, s, legacy_matrix=False, noconds=True)
xzs = sy.inverse_laplace_transform(Fs * Es, s, t)
# 状态的完全解
x = xzi + xzs
print('x=', sy.exp_polar(x))

'''输出方程求解'''
yzi = C * F * x0  # 输出的零输入响应
h = C * F * B + D * sy.DiracDelta(t)  # 冲激响应
# 利用拉普拉斯变换求输出的零状态响应
Hs = sy.laplace_transform(h, t, s, legacy_matrix=False, noconds=True)
yzs = sy.inverse_laplace_transform(Hs * Es, s, t)
y = yzi + yzs  # 输出的完全解
print('y=', sy.exp_polar(y))

'''转为numpy画图'''
import numpy as np

f1 = sy.lambdify(t, y[0], "numpy")
f2 = sy.lambdify(t, y[1], "numpy")
t_np = np.arange(0, 5, 0.01)  # 区别sympy定义的t
f1_np = f1(t_np)
f2_np = f2(t_np)

'''绘图'''
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (8.0, 4.0)
plt.grid()  
plt.xlabel('时间 (s)')
plt.xlim(0, 5)
plt.ylim(-0.5, 5)
plt.plot(t_np, f1_np.real, c='red', label='y1(t)')
plt.plot(t_np, f2_np.real, c='blue', ls='--', label='y2(t)')
plt.legend(['y1(t)', 'y2(t)'])
plt.show()

'''
# 绘制输出的sympy波形图
# 如果需要显示中文，则需要加入下面两行
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块
p1 = plot(y[0], (t, 0, 5), ylim=(-0.5, 5), ylabel='y1(t)', xlabel='t',
          line_color='blue', show=False)
p2 = plot(y[1], (t, 0, 5), ylim=(-0.5, 5), ylabel='y2(t)', xlabel='t',
          line_color='green', show=False)
# PlotGrid实际还没有提供正式接口，所以调用方式是实例化该类，在做显示
p = plotting.PlotGrid(1, 2, p1, p2, size=(6, 3))
'''
