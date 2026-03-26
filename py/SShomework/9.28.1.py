import sympy as sy
t = sy.symbols('t')
r = (1.5-4*sy.exp(-t)+2.5*sy.exp(-2*t))*sy.Heaviside(t)+5*sy.exp(-t)-4*sy.exp(-2*t)
r_n = (-4*sy.exp(-t)+2.5*sy.exp(-2*t))*sy.Heaviside(t)+5*sy.exp(-t)-4*sy.exp(-2*t)
r_f = 1.5*sy.Heaviside(t)
p1 = sy.plot(r,(t,-1,5),title='response',xlabel='t',ylabel='r(t)',show=False)
p2 = sy.plot(r_n,(t,-1,5),title='natural response',xlabel='t',ylabel='r(t)',show=False)
p3 = sy.plot(r_f,(t,-1,5),title='forced response',xlabel='t',ylabel='r(t)',show=False)
sy.plotting.PlotGrid(3,1,p1,p2,p3)