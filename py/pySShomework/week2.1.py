import sympy as sy
import matplotlib.pylab as plt

t = sy.symbols('t', real=True)
x1 = sy.sin(2*sy.pi*t)*sy.Heaviside(t)
x2 = sy.sin(2*sy.pi*(t-0.5))*sy.Heaviside(t)
x3 = sy.sin(2*sy.pi*t)*sy.Heaviside(t-1)
x4 = sy.sin(2*sy.pi*(t-0.5))*sy.Heaviside(t-1)

plt.rcParams['axes.unicode_minus'] = False
p1 = sy.plot(x1, (t,-5,5),xlabel='t', ylabel='x1(t)', show=False)
p2 = sy.plot(x2, (t,-5,5),xlabel='t', ylabel='x2(t)', show=False)
p3 = sy.plot(x3, (t,-5,5),xlabel='t', ylabel='x3(t)', show=False)
p4 = sy.plot(x4, (t,-5,5),xlabel='t', ylabel='x4(t)', show=False)


grid = sy.plotting.PlotGrid(2, 2, p1, p2, p3, p4)
fig = grid._backend.fig
fig.tight_layout(pad=3.0)
plt.show()