import sympy as sy

t = sy.symbols('t')
#Piecewise函数对求导的支持较差
#y = sy.Piecewise((t, ((t > 0) &  (t < 1))), (0, True))
y = t * (sy.Heaviside(t) - sy.Heaviside(t - 1))  # 原始信号
'''
注意Heaviside求导结果会产生DiracDelta函数
不能用后续语句绘图，否则会报错'''
y1 = y.diff(t)#求导
print('求导：', sy.simplify(y1))
y2 = y.integrate(t)#不定积分，在一定程度上可以模拟变上限积分
print('不定积分：', sy.simplify(y2))
y3 = y.integrate(t, (t, 0, 1))#定积分，结果为数值
print('定积分：', y3)
#print( sy.pretty(sy.simplify(y3))) #另一种显示方式


'''绘图'''
p0 = sy.plot(y, (t, -1, 5), title='f(t)', xlabel='t', show=False)
p1 = sy.plot(y4, (t, -1, 5), title='f’(t)', xlabel='t', show=False)
sy.plotting.PlotGrid(2, 1, p0, p1)
