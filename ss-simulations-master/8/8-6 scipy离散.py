import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# 序列范围
N = 15
n = np.arange(0, N + 1)
n2 = np.arange(1, N + 1)
# 系统参数
A = [[-1, 3], [-2, 4]]
B = [[11, 0], [0, 6]]  # 单列
C = [[1, -1]]
D = [0, 1]
sys = signal.StateSpace(A, B, C, D, dt=True)
# 定义激励信号
e = np.empty((2, N + 1))
e[0] = np.append([1], np.zeros(N))
e[1] = np.ones(N + 1)
q0 = [0, 0]
n, y, q = signal.dlsim(sys, e.T, n, q0)
'''理论解和误差计算'''
y_ideal = np.append([1], 12 - 6 * np.arange(1, N + 1))
q_ideal = np.empty((2, N + 1))
q_ideal[0] = np.append([0], 7 * np.power(2, n2) - 18 * n2 + 15 * np.ones(N))
q_ideal[1] = np.append([0], 7 * np.power(2, n2) - 12 * n2 + 4 * np.ones(N))
x_rms = np.sqrt(np.mean(np.power(q.T - q_ideal, 2), axis=1))
print('状态变量的方均根值：', x_rms)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中负号'-'显示为方块的问题
plt.rcParams['figure.figsize'] = (9.0, 3.0)  # 图像大小
plt.subplot(131)  # 图1
# plt.stem(n, y_ideal)#理论值
plt.stem(n, y)  # 计算值
plt.ylabel('y(n)')
plt.title('输出')
plt.subplot(132)  # 图2
plt.stem(n, q[:, 0])
# plt.stem(n, q_ideal[0, :].T)#理论值
plt.ylabel('q1(n)')
plt.title('状态变量1')
plt.subplot(133)  # 图3
plt.stem(n, q[:, 1])
# plt.stem(n, q_ideal[1, :].T)#理论值
plt.ylabel('q2(n)')
plt.title('状态变量2')
plt.tight_layout()  # 紧凑显示图形
plt.show()
