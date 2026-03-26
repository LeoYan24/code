import matplotlib.pylab as plt  # 绘制图形
import numpy as np

# 时间轴
t = np.arange(-2, 2, 0.01)
# 绘制3D图形
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
plt.grid()
for i in range(1, 12, 2):
    # 画一组cos信号幅度,幅度为1/i
    # 依次画图，注意默认的z轴是垂直的轴，所以这里用zdir参数把y轴编程垂直的
    ax.plot(t, (1 / i) * np.cos(i * np.pi * t), i, zdir='y', label='谐波', c='c')

ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_zlabel('z轴')  # 注意直接用plt方式无法设置z轴信息，建议用ax
plt.show()
