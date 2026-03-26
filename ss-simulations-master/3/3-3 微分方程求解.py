import sympy as sy
from matplotlib import pyplot as plt

t = sy.symbols('t')  # 定义自变量和函数，对于单输入单输出系统，只需要定义t和y
e, r = sy.symbols('e r', cls=sy.Function)
e = 2 * sy.exp(-1 * t)  # 激励信号
diffeq = sy.Eq(6*r(t) + 5*sy.Derivative(r(t), t) + sy.Derivative(r(t), (t, 2)), e)

print(diffeq)
full_respone = sy.dsolve(diffeq, r(t), ics={r(0): 2, r(t).diff(t).subs(t, 0): -1})
print("全响应:",full_respone)
print(sy.pretty(full_respone))  # 易读方式

zsr = sy.dsolve(diffeq, r(t), ics={r(0): 0, r(t).diff(t).subs(t, 0): 0})
print("零状态响应:",zsr)
print(sy.pretty(zsr))

diffeq2 = sy.Eq(diffeq.lhs, 0)
zir = sy.dsolve(diffeq2, r(t), ics={r(0): 2, r(t).diff(t).subs(t, 0): -1})
print("零输入响应:",zir)
print(sy.pretty(zir))

print(full_respone.rhs)
exit()
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
p0 = sy.plot(sy.sin(2 * t), (t,0,10),title='激励信号',ylabel='', xlabel='t', show=False)
p1 = sy.plot(full_respone.rhs, (t,0,10),title='全响应',ylabel='', xlabel='t', show=False)
p2 = sy.plot(zir.rhs,  (t,0,10),title='零输入响应', ylabel='',xlabel='t', show=False)
p3 = sy.plot(zsr.rhs,  (t,0,10),title='零状态响应', ylabel='',xlabel='t', show=False)
sy.plotting.PlotGrid(4, 1, p0, p1, p2, p3)