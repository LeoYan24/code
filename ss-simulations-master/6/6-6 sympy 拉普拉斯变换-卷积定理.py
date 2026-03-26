import sympy as sy

t, s = sy.symbols('t s')
xt = sy.exp(-3 * t)
Xs = sy.laplace_transform(xt, t, s, noconds=True)
Hs = (3 * s + 1) / (s ** 2 + 2 * s + 5)
Ys = Xs * Hs
print(sy.simplify(Ys))
yt = sy.inverse_laplace_transform(Ys, s, t)
print(yt)
# sy.plot(yt, (t, 0, 10))  # 画图

# exit()
# 如果希望采用matplotlib画图
import numpy as np
import matplotlib.pylab as plt

Yt_func = sy.lambdify(t, yt, 'numpy')
time = np.arange(0, 10, 0.01)
yt_series = Yt_func(time)

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.grid()  
plt.title("响应信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=12, loc='right')
plt.plot(time, yt_series, 'r')
plt.show()
