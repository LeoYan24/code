import matplotlib.pylab as plt  # 绘制图形
import numpy as np

N = 15
n = np.arange(0, N + 1)
A = [[-1, 3], [-2, 4]]
B = [[11, 0], [0, 6]]  # 单列
C = [[1, -1]]
D = [0, 1]
# 定义激励信号
e = np.empty((2, N + 1))
e[0] = np.append([1], np.zeros(N))
e[1] = np.ones(N + 1)
# 定义状态变量
q = np.empty((2, N + 1))
q[:, 0] = [0, 0]  # 初值
print(q)
# 定义输出
y = np.empty((N + 1, 1))
for i in range(0, N):  # 迭代取值
    q[:, i + 1] = (A @ (q[:, i]).T + B @ (e[:, i]).T).T
    y[i, :] = C @ (q[:, i]).T + D @ (e[:, i]).T
# y的最后一个输出在循环外计算
y[N, :] = C @ (q[:, N]).T + D @ (e[:, N]).T

'''如果以矩阵方式计算
y = np.empty((N + 1, 1))
for i in range(0, N):# 迭代取值
    q[:, i + 1] = (A * np.matrix(q[:, i]).T
                   + B * np.matrix(e[:, i]).T).T
    y[i, :] = C * np.matrix(q[:, i]).T + D * np.matrix(e[:, i]).T
# y的最后一个输出在循环外计算
y[N, :] = C * np.matrix(q[:, N]).T + D * np.matrix(e[:, N]).T
'''
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中负号'-'显示为方块的问题
plt.rcParams['figure.figsize'] = (9.0, 3.0)  # 图像大小
plt.subplot(131)  # 图1
plt.stem(n, y)  # 计算值
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('输出')
plt.subplot(132)  # 图2
plt.stem(n, q[0, :])
# plt.stem(n, q_ideal[0, :].T)#理论值
plt.xlabel('n')
plt.ylabel('q1(n)')
plt.title('状态变量1')
plt.subplot(133)  # 图3
plt.stem(n, q[1, :])
# plt.stem(n, q_ideal[1, :].T)#理论值
plt.xlabel('n')
plt.ylabel('q2(n)')
plt.title('状态变量2')
plt.tight_layout()  # 紧凑显示图形
plt.show()
