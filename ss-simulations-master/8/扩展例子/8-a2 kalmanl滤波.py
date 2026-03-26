from math import sqrt

import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import sparse, linalg

# 抽样时间点的个数
N = 120
# 室内温度的理论值
CON = 25
# 期望的温度
x_expect = CON * np.ones((1, N))  # 长度？
# 房间各时刻真实温度值
x = np.zeros((1, N)).astype(float)
# Kalman滤波处理的状态，也叫估计值
xkf = np.zeros((1, N))
# 温度计测量值
Z = np.zeros((1, N))
# 状态的方均误差
P = np.zeros((1, N))
# 房间温度的初始值
x[0, 0] = 25.1
# 状态的方均误差的初始值的
P[0, 0] = 0.01
# 初始测量值，可以作为滤波器的初始估计状态
Z[0, 0] = 24.9
xkf[0, 0] = Z[0, 0]
# 过程噪声的平均功率（方差）
Q = 0.01
# 测量噪声的平均功率（方差）
R = 0.25
# 过程噪声的幅值（平均功率的平方根）
# Matlab中randn是正态分布，均值为0，方差为1，
# 数据范围在正负3的概率99.6#
# python中np.random.randn应该是一致的
w = sqrt(Q) * np.random.randn(1, N)
# 测量噪声的幅值（平均功率的平方根）
v = sqrt(R) * np.random.randn(1, N)
# 状态转移矩阵
F = np.matrix([[1.0]])  # matrix支持.T转置方法
# 噪声驱动矩阵
G = np.matrix([[1.0]])
# 转换矩阵
C = np.matrix([[1.0]])
# 本系统状态为一维
I = sparse.eye(1)
# 模拟房间温度和测量过程，并滤波
for i in range(1, N):
    # 状态方程，模拟房间真实温度
    # 这个真实值是不知道的，但是它是客观存在的
    x[:, i] = F[0] * x[:, i - 1] + G[0] * w[:, i - 1]
    # 观测方程，模拟温度计的测量值
    Z[:, i] = C[0] * x[:, i] + v[:, i]
    # 有了n时刻的观测值Z(n)和n - 1时刻的状态，那么就可以进行滤波了
    # 卡尔曼滤波算法
    # 第1步：预测状态
    X_pre = F[0] * xkf[:, i - 1]
    # 第2步：预测状态的均方误差
    P_pre = F[0] * P[:, i - 1] * F.T + Q
    # 第3步：测量误差的平均功率
    S = C * P_pre * C.T + R
    # 第4步：更新卡尔曼滤波增益
    K = P_pre * C.T * linalg.inv(S)
    # 第5步：更新测量残差
    e = Z[:, i] - C * X_pre
    # 第6步：更新后状态的估计
    xkf[:, i] = X_pre + K * e
    # 第7步：更新后状态的均方误差
    P[:, i] = (I - K * C) * P_pre
# 滤波算法性能评估
# 测量值与真实值之间的偏差
Err_Messure = Z - x
# Kalman估计与真实值之间的偏差
Err_Kalman = xkf - x
n = np.arange(0, N)

print(x_expect[0, :])
# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中负号'-'显示为方块的问题
plt.rcParams['figure.figsize'] = (6.0, 3.0)  # 图像大小
plt.subplot(211)  # 图1
plt.plot(n, x_expect[0, :], 'm-')
plt.plot(n, x[0, :], '-r.')  # fmt = '[marker][line][color]'
plt.plot(n, Z[0, :], '-ko', fillstyle='none')  # ,alpha=0.5
plt.plot(n, xkf[0, :], 'b-*')
plt.xlabel('抽样时间 (分钟)')
plt.ylabel('温度值 (℃)')
plt.legend(['期望值', '真实值', '观测值', 'Kalman滤波值'])
plt.subplot(212)  # 图2
plt.plot(n, Err_Messure[0, :], '-b.')
plt.plot(n, Err_Kalman[0, :], '-k*')
plt.legend('测量偏差', 'Kalman滤波偏差')
# plt.stem(n, q_ideal[0, :].T)#理论值
plt.xlabel('抽样时间 (分钟)')
plt.ylabel('温度偏差值 (℃)')

plt.show()
exit()
