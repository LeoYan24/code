from sympy import *

# 定义函数和自变量
t = Symbol('t')
# 原始信号
y = (t + 1) * (Heaviside(t + 1) - Heaviside(t)) + (Heaviside(t) - Heaviside(t - 1))

'''思路1：利用subs函数进行变量替换'''
y1 = y.subs(t, -2 * t+3)

'''
思路2：设tao = -2t+3，定义y(tao)，然后直接对t画图
这种方法不是很直观
'''
tao = Symbol('tao')
tao = -2 * t + 3
y_tao = ((tao + 1) * (Heaviside(tao + 1) - Heaviside(tao)) + \
           (Heaviside(tao) - Heaviside(tao - 1)))



#y5 = y.subs(t - 1, t)  # 结果不对,不支持反向变换，结果不太可控

p0 = plot(y, (t, -4, 4), title='f(t)', xlabel='t', show=False)
p1 = plot(y1, (t, -4, 4), title='f(-2t+3)', xlabel='t', show=False)
p2 = plot(y_tao, (t, -4, 4), title='f(-2t+3)', xlabel='t', show=False)

plotting.PlotGrid(3, 1, p0, p1, p2)
