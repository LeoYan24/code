import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t = np.arange(0, 3, 0.01)
e = np.heaviside(t, 1)  # 定义输入信号
x0 = [1]  # 定义初始条件
system = ([0, 2], [1, 2])  # 定义系统
# 零输入响应
t, y_zi, _ = signal.lsim(system, U=np.zeros_like(t), T=t, X0=x0)
# 零状态响应
t, y_zs, _ = signal.lsim(system, U=e, T=t, X0=[0])
# 全响应
t, y, _ = signal.lsim(system, U=e, T=t, X0=x0)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(t, y_zi, "r-.", )
plt.plot(t, y_zs, "b--")
plt.plot(t, y)
plt.legend(labels=['零输入响应', '零状态响应', '全响应'], loc='best')
plt.show()
