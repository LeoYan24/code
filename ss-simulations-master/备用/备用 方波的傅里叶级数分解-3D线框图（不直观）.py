import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

'''谐波个数'''
n = 20
'''定义方波参数'''
T1 = 1
w1 = 2 * np.pi / T1
tao = 0.5
'''x轴：时间范围'''
t = np.arange(-2 * T1, 2 * T1, 0.01)
'''y轴：谐波'''
N = np.arange(1, n + 1)
'''定义一个周期方波'''
Gate = 0.5 * signal.square(w1 * (t + tao / 2), duty=tao / T1) + 0.5  # 周期方波，duty为占空比
'''叠加谐波的函数'''


def harmonic(n, t):
    c0 = tao / T1 * np.ones_like(t)
    sum_f_cn = c0
    for i in range(1, n + 1):
        Cn = 2 * tao / T1 * np.sinc(i * tao / T1)
        sum_f_cn = sum_f_cn + Cn * np.cos(i * w1 * t)
    return sum_f_cn


'''z轴：计算任意谐波分量,并叠加到2维数组'''
Z = []
for i in range(1, n + 1):
    Z.append(harmonic(i, t))
'''绘制3D图形'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

'''绘制'''
X, Y = np.meshgrid(t, N)
Z = np.array(Z)
# 表面图
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
# 线框图
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=10)
ax.set_xlabel('时间轴')
plt.ylabel('谐波（频率分量）')  # 对比ax、plt两种语法风格
ax.set_zlabel('振幅')  # 注意直接用plt无法设置z轴信息
ax.set_zlim(-2, 2)  # 设置Z轴范围
ax.set_title('方波的傅里叶级数分解')  # 等价于plt.title
plt.grid()
plt.show()
