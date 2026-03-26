from sympy import *
from sympy import plotting 
t = Symbol('t')
y = sin(2*pi*t)*(Heaviside(t)-Heaviside(t-1))
rv = y.subs(t,-t)
y_e = (y+rv)/2
y_o = (y-rv)/2

p0 = plot(y, (t, -4, 4), title='oringinal signal', xlabel='t', show=False)
p1 = plot(rv, (t, -4, 4), title='reversed signal', xlabel='t', show=False)
p2 = plot(y_e, (t, -4, 4), title='even part', xlabel='t', show=False)
p3 = plot(y_o,(t,-4,4),title = 'odd part', xlabel='t',show=False)

plotting.PlotGrid(2,2,p0,p1,p2,p3)
