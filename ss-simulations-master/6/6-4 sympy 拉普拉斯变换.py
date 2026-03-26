import sympy as sy

t, s = sy.symbols('t s')

xt = sy.DiracDelta(t)
Xs = sy.laplace_transform(xt, t, s)
print('(1)', Xs)

xt = sy.exp(-2 * t) + 1
Xs = sy.laplace_transform(xt, t, s, noconds=True)
print('(2)', Xs)

xt = sy.exp(-3 * t) * sy.cos(100 * t)
Xs = sy.laplace_transform(xt, t, s)
print('(3)', Xs)

xt = t ** 2 * sy.exp(-2 * t)
Xs = sy.laplace_transform(xt, t, s)
print('(4)', Xs)

xt = sy.DiracDelta(t).diff(t)
Xs = sy.laplace_transform(xt, t, s)
print('(5)', Xs)

xt = sy.exp(t ** 2)
Xs = sy.laplace_transform(xt, t, s)
print('(6)', Xs)

