import sympy as sy
t = sy.symbols('t')
r = sy.symbols('r', cls=sy.Function)
'''1，先假定右边只有一个冲激项，此时响应中必然不含冲激项，解齐次方程：'''
diffeq = sy.Eq(r(t).diff(t, 2) + 4 * r(t).diff(t) + 3 * r(t), 0)
'''2，根据齐次解法，次高阶导数项的初值为1'''
h_hat = sy.dsolve(diffeq, r(t), ics={r(0): 0, r(t).diff(t).subs(t, 0): 1})
'''3,原式不带u(t)，需要乘一下u(t),才能获得正确的导数'''
h_hat = h_hat.rhs * sy.Heaviside(t)
'''4，对h_hat进行线性组合，得到真实的h(t)'''
h = h_hat.diff(t) + 2 * h_hat
print(h)
