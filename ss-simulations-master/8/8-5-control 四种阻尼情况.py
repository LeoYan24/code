# from scipy import signal  # 导入scipy.signal
import control as ct
import matplotlib.pylab as plt  # 绘制图形
import numpy as np  # 导入numpy，设置别名np
from control import matlab

# 参数
L1 = 1
C1 = 1
R1 = 4  # [0, 0.2, 2, 4]# 四种阻尼情况
q0 = [1, 0]  # 起始状态
t = np.arange(0, 20, 0.01)  # 样本
# 输入：单位样值响应
e = np.zeros_like(t)
e[0] = 1
# 输入：单位阶跃输入
# e = np.ones(len(t))
# 建立系统并绘制状态变量曲线
A = [[-R1 / L1, -1 / L1], [1 / C1, 0]]
B = [[1 / L1], [0]]
C = [0, 1]
D = [0]
sys = ct.StateSpace(A, B, C, D)  # 系统的状态空间模型
y, t_out, q = matlab.lsim(sys, e, t, q0)  # 系统仿真求解

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8.0, 4.0))
# 系统状态
plt.subplot(121)
plt.plot(t, (q.T)[0], 'r', label='q_1(t)')
plt.plot(t, (q.T)[1], 'k', ls='--', label='q_2(t)')
plt.legend(['$q_1 (t)$', '$q_2 (t)$'])
plt.xlabel('时间 (s)')
plt.title('状态变量随时间的变化曲线')
plt.subplot(122)  # 图2
plt.plot((q.T)[0], (q.T)[1])
plt.xlabel('$q_1 (t)$')
plt.ylabel('$q_2 (t)$')
plt.title('状态轨迹')
plt.tight_layout()  # 紧凑显示图形
plt.show()
