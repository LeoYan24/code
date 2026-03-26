from sympy import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

'''
原本问题是一个RLC串联电路的分析，参见 1.0题目.png
'''
# 问题1：特征根
x = symbols('x')
R, L, C = symbols('R L C')
# todo 带入不同的参数值，分析过阻尼、欠阻尼、无阻尼、临界阻尼情况
# L=1;C=1;R=0;
L = 1;C = 1;R = 0.2;
# L=1;C=1;R=2;
# L=1;C=1;R=3;
# todo 查看此时系统的特征根（不同阻尼情况）
rts = roots(x ** 2 + R / L * x + 1 / L / C, x)
print(pretty(rts))

'''
求出冲激响应，（利用齐次解法——了参见配图），并画图
'''
t = symbols('t')
h = symbols('r', cls=Function)
diffeq = Eq(h(t).diff(t, 2) + R / L * h(t).diff(t) + 1 / L / C * h(t), 0)
respone = dsolve(diffeq, h(t), ics={h(0): 0, h(t).diff(t).subs(t, 0): 1})
h = respone.rhs * Heaviside(t) / L / C #根据方程结构修正h(t)
print("h(t)=", h)
#简易绘图
plot(h, (t, 0, 30),title="冲激响应")

'''
求出阶跃响应，并画图
'''
#方法1，直接解方程
g = symbols('r', cls=Function)
diffeq = Eq(g(t).diff(t, 2) + R / L * g(t).diff(t) + 1 / L / C * g(t), 1)
respone = dsolve(diffeq, g(t), ics={g(0): 0, g(t).diff(t).subs(t, 0): 0})
g = respone.rhs * Heaviside(t) / L / C #根据方程结构修正h(t)
print("g(t)=", g)
#方法2，用冲击响应做-oo到t的积分
g2 = h.integrate((t,0,t))
#对比两种方法的输出
print(g)
print(g2)
#绘制阶跃响应
plot(g, (t, 0, 30),title="阶跃响应")

'''
#对比两种阶跃响应方法的输出结果
p0 = plot(g, (t, 0, 30),title="阶跃响应（方法1）",show=False)
p1 = plot(g2, (t, 0, 30),title="阶跃响应（方法2）",show=False)
plotting.PlotGrid(1, 2, p0, p1)
'''