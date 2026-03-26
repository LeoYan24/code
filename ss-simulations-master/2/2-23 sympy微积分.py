import sympy as sy

t = sy.symbols('t')
y = t * (sy.Heaviside(t) - sy.Heaviside(t - 1))  # 原始信号
y1 = y.subs(t, -2 * t + 3)
print('波形变换 f(-2t+3)：', sy.simplify(y1))
'''注意y求导结果会产生DiracDelta函数
不能用后续语句绘图，否则会报错'''
y2 = y.diff(t)#求导
print('求导：', sy.simplify(y2))
y3 = y.integrate(t)#积分
print('不定积分：', sy.simplify(y3))
#print( sy.pretty(sy.simplify(y3))) #另一种显示方式
y4 = y.integrate(t, (t, 0, 1))#定积分，结果为数值
print('定积分：', y4)

'''绘图'''
p0 = sy.plot(y, (t, -1, 2), title='f(t)', xlabel='t', show=False)
p1 = sy.plot(y1, (t, -1, 2), title='f(-2t+3)', xlabel='t', show=False)
p2 = sy.plot(y3, (t, -1, 2), title='f’(t)', xlabel='t', show=False)
sy.plotting.PlotGrid(3, 1, p0, p1, p2)
