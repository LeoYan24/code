import matplotlib.pylab as plt  # 绘制图形
import numpy as np

# 定义心形函数
np.seterr(divide='ignore', invalid='ignore')  # numpy忽略除以零的警告
theta = np.arange(0, np.pi, 0.01)  # 0到pi，即角度取弧度
r = np.abs(np.tan(theta)) ** (np.abs(1 / np.tan(theta)))

# 建立极坐标绘图（projection参数设置为极坐标），方式1
# ax =  plt.figure().add_subplot(projection='polar')
# 建立极坐标绘图，方式2
# ax = plt.subplot(111,projection='polar')
# 建立极坐标绘图，方式3
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
# 绘图
plt.fill(theta, r, c="r")  # 填充
plt.plot(theta, r, c="b")  # 描边
# 设置坐标网格
ax.set_rgrids(np.arange(0, 1.5, 0.5), angle=90)  # 半径网格（刻度）的取值和角度
ax.set_thetagrids(np.arange(0.0, 360.0, 90.0), [r"0", r"$π/2$", r"$π$", r"$3π/2$"])  # 角度指示刻度(使用弧度坐标)
plt.show()

# 其他设置半径网格的方法
# ax.axis([0, np.pi*2, 0, 1])  # 设置弧度和半径的坐标范围
# ax.set_rlim /set_rmax /set_rmin 半径刻度的范围
# ax.set_rlabel_position(90) # 半径刻度的角度（位置）
# ax.set_rticks(np.arange(0, 15, 5)) #半径刻度范围
# 其他设置内容
# ax.set_thetalim(-np.pi / 3, np.pi / 3) #设置圆的范围，参数是弧度 /set_thetamax /set_thetamin
# plt.grid(False)#不显示细网格
# 设置角度网格
# ax.set_thetagrids(np.arange(0.0, 360.0, 90.0)) #角度指示刻度
