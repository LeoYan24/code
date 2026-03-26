
import lcapy as lc

from lcapy import f
from matplotlib.pyplot import show

'''新建电路'''
omega_0 = 2
cc = lc.Circuit()
cc.add('R1 1 2 1;right')
cc.add('R2 2 3 1;right')
cc.add('C1 2 4_0 1/2;down')
cc.add('C2 3 4 1/3; down')
cc.add('V1 1 4_1 {sin(2 * t)};down') #电源
cc.add('W1 4 4_0;left')
cc.add('W2 4_0 4_1;left')
cc.add('P_in 1 4_1; down')  #定义端口
cc.add('P_out 3 4; down, v={v_{2}}')  #定义端口

'''存自定义格式的网表
cc.save(r'..\data\circuit.cir')
'''
'''电路图'''
cc.draw()
show()
'''（稳态）响应的数值解'''
cc.P_out.v.plot((0, 30))
show()
'''传输函数'''
H1 = cc.transfer('P_in', 'P_out')
print("H1(s)= ", H1)
'''微分方程'''
diffeq = H1.differential_equation()
print("微分方程：",lc.pretty(lc.simplify(diffeq)))
str1 = str(diffeq.lhs)
'''防止lcapy库和sympy有冲突，卸载掉lcapy库，导入sympy库，否则符号t等会有冲突'''
del lc
import sympy as sy
t = sy.symbols('t')  # 定义自变量和函数，对于单输入单输出系统，只需要定义t和y
y = sy.symbols('y', cls=sy.Function)
str2 = str(6 * sy.sin(2*t))
df = sy.Eq(sy.sympify(str1),sy.sympify(str2))
respone = sy.dsolve(df, y(t), ics={y(0): 1, y(t).diff(t).subs(t, 0): 0})  # 求通解（包括特解），调用dsolve函数,返回一个Eq对象
print("全响应:",sy.pretty(respone))
#print(sy.pretty(respone))  # 易读方式式

respone_zs = sy.dsolve(df, y(t), ics={y(0): 0, y(t).diff(t).subs(t, 0): 0})  # 求通解（包括特解），调用dsolve函数,返回一个Eq对象
print("零状态响应:",sy.pretty(respone_zs))

'''响应画图'''
df2 = sy.Eq(df.lhs, 0)
respone_zi = sy.dsolve(df2, y(t), ics={y(0): 1, y(t).diff(t).subs(t, 0): 0})  # 求通解（包括特解），调用dsolve函数,返回一个Eq对象
print("零输入响应:",sy.pretty(respone_zi))

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

t1 = np.arange(0, 30, 0.01)
print(respone_zs.rhs)
f_respone_zs = sy.lambdify(t, respone_zs.rhs, "numpy")
y_zs = f_respone_zs(t1)  # 不能直接用f
f_respone_zi = sy.lambdify(t, respone_zi.rhs, "numpy")
y_zi = f_respone_zi(t1)

plt.plot(t1, y_zi, label='零输入响应')
plt.plot(t1, y_zs, label='零状态响应')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()


'''画出传输函数的零极点图'''
H1.plot()
show()

'''频响特性'''
freq = np.linspace(0, 100, 10000)
H1(f).abs.plot(freq, log_scale=True)
H1(f).dB.plot(freq, log_scale=True)
H1(f).phase.plot(freq, log_scale=True)
show()

'''波特图'''
freq = np.logspace(-2, 2, 10000)
H1.bode_plot(freq)
show()

exit()
'''新建电路
omega_0 = 2
cc = lc.Circuit()
cc.add('R1 1 2 ;right')
cc.add('R2 2 3 ;right')
cc.add('C1 2 4_0 ;down')
cc.add('C2 3 4 ; down')
cc.add('V1 1 4_1 ;down')
cc.add('W1 4 4_0;left')
cc.add('W2 4_0 4_1;left')
cc.add('P_in 1 4_1; down')
cc.add('P_out 3 4; down, v={v_{2}}') '''