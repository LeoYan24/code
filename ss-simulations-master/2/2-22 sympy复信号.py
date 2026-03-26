import matplotlib.pylab as plt  # 绘制图形
import sympy as sy

t = sy.symbols('t', real=True)
y = sy.exp((-0.5 + 2 * sy.pi * sy.I) * t)  # 定义一个复指数信号
print(y.as_real_imag())  # 把e指数显示为实部+虚部的形式
print(sy.re(y), sy.im(y))  # y的实部和虚部
print(sy.Abs(y), sy.arg(y))  # y的模值和相位(弧度)
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
p1 = sy.plot(sy.re(y), (t, 0, 10), title='实部', xlabel='t', ylabel='y(t)', show=False)
p2 = sy.plot(sy.im(y), (t, 0, 10), title='虚部', xlabel='t', ylabel='yflip(t)', show=False)
p3 = sy.plot(sy.Abs(y), (t, 0, 10), title='模值', xlabel='t', ylabel='y_odd(t)', show=False)
p4 = sy.plot(sy.arg(y), (t, 0, 10), title='相位', xlabel='t', ylabel='y_even(t)', show=False)
sy.plotting.PlotGrid(2, 2, p1, p2, p3, p4)
