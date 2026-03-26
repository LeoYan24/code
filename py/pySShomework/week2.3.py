import sympy as sy

t = sy.symbols('t')
y1 = sy.Heaviside(t)
y2 = sy.sin(t)**4/(1+sy.exp(-t))
y3 = sy.atan(2*t)/(t*(1+t**2))
y4 = 1/(t*(sy.exp(t)-sy.exp(-t)))-0.5

print('differentiations:\n')
print('y1\'=',sy.simplify(y1.diff(t)),'\n')
print('y2\'=',sy.simplify(y2.diff(t)),'\n')
print('y3\'=',sy.simplify(y3.diff(t)),'\n')

print('Intgrations:\n')
print('int(y1)=',sy.simplify(y1.integrate(t)),'\n')
print('int(y2)=',sy.simplify(sy.integrate(y2,(t,-sy.pi/2,sy.pi/2))),'\n')
print('int(y3)=',sy.simplify(y3.integrate(t)),'\n')
print('int(y4)=',sy.simplify(sy.integrate(y4,(t,0,sy.oo))),'\n')