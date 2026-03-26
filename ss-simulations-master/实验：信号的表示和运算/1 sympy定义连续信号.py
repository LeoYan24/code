import matplotlib.pylab as plt
import sympy as sy

t = sy.symbols('t')  # 定义自变量
f1 = sy.sin(2 * sy.pi * t)  # 正弦信号
f2 = sy.cos(2 * sy.pi * t)  # 余弦信号
f3 = sy.sinc(t)  # Sa函数
f4 = sy.Heaviside(t)  # 阶跃信号
# todo 根据需求定义各类分段函数
f5 = sy.Piecewise((t, ((t > 0) &  (t < 5))), (0, True))
'''注意DiracDelta函数不能用后续语句绘图，否则会报错'''
f6 = sy.DiracDelta(t)  # 冲激信号
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
p0 = sy.plot(f1,f2, (t, -2, 2), title='正余弦函数', xlabel='t',
             show=False)
p1 = sy.plot(f3, (t, -10, 10), title='Sa函数', xlabel='t',
             show=False)
p2 = sy.plot(f4, (t, -10, 10), title='阶跃函数', xlabel='t',
             show=False)
p3 = sy.plot(f5, (t, -10, 10), title='分段函数', xlabel='t',
             show=False)
sy.plotting.PlotGrid(2, 2, p0, p1, p2, p3)
