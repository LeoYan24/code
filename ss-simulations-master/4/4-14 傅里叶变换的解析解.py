import sympy as sy

t, f, w = sy.symbols('t f w')
# 单边指数信号
ft1 = sy.exp(-1 * t) * sy.Heaviside(t)
# 矩形脉冲
ft2 = sy.Heaviside(t + 0.5) - sy.Heaviside(t - 0.5)
# 当前操作的函数
ft = ft2
'''
#该方法可能无法正确求出一些函数的谱线，比如谱线中存在冲激形式
例如：
ft = sin(2*t)+sin(4*t)
ft = sign(t)
ft = Heaviside(t)
'''
Ff = sy.fourier_transform(ft, t, f)

print(Ff)  # 频谱表达式
print(sy.Abs(Ff))  # 幅度表达式
print(sy.arg(Ff))  # 相位表达式

'''绘图'''
p1 = sy.plot(ft, (t, -5, 5), title='f(t)', xlabel='t', line_color='orange', show=False)
p3 = sy.plot(sy.Abs(Ff), (f, -5, 5), title='Amplitude spectrum', xlabel='f', show=False)
p4 = sy.plot(sy.arg(Ff), (f, -5, 5), title='Phase spectrum', xlabel='f', show=False)
p = sy.plotting.PlotGrid(3, 1, p1, p3, p4)

'''
sympy.integrals.transforms.fourier_transform
注意，该方法的频域变量是频率，不是角频率
如果要转化为角频率，则执行变量转换，f = w/2pi：
FW = Ff.subs(f, w / (2 * sy.pi))
'''
