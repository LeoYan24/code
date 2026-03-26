from sympy import *

# 定义函数和自变量
t = Symbol('t')
# 原始信号
y_n2tp3 = (t + 1) * (Heaviside(t + 1) - Heaviside(t)) + (Heaviside(t) - Heaviside(t - 1))
'''
思路1：由于subs不支持反向变换，所以尝试手动变换
'''
y_2tp3 = y_n2tp3.subs(t, -1 * t) # t -> -t
y_tp3 = y_2tp3.subs(t, 0.5 * t ) #2t->t
y_t = y_tp3.subs(t, t - 3) # t -> t-3
#y5 = y.subs(-2 * t + 3, t)  # 结果不对,不支持反向变换，结果不太可控


p0 = plot(y_n2tp3, (t, -4, 4), title='f(-2t+3)', xlabel='t', show=False)
p1 = plot(y_2tp3, (t, -4, 4), title='f(2t+3)', xlabel='t', show=False)
p2 = plot(y_tp3, (t, -4, 4), title='f(t+3)', xlabel='t', show=False)
p3 = plot(y_t, (t, -4, 4), title='f(t)', xlabel='t', show=False)
plotting.PlotGrid(2, 2, p0, p1, p2, p3)
