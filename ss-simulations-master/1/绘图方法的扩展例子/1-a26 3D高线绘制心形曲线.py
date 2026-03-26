import matplotlib.pyplot as plt
import numpy as np

# 定义计算和绘图边界
l1, l2 = -1.5, 1.5


# 定义3D曲线函数
def surfaceFunc(x, y, z):
    # 3D心形曲线
    return (x ** 2 + (9 / 4) * y ** 2 + z ** 2 - 1) ** 3 - x ** 2 * z ** 3 - (9 / 80) * y ** 2 * z ** 3
    # 球体
    # return x**2+y**2+z**2-1


# 表面稀疏覆盖
A = np.linspace(l1, l2, 100)  # 相当于轮廓线的精度
A1, A2 = np.meshgrid(A, A)  # 形成2D网格
B = np.linspace(l1, l2, 25)  # 切片数量

# 设置3D绘图
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# 固定几个z切片（B决定数量），画XY平面的轮廓
for z in B:
    X, Y = A1, A2
    Z = surfaceFunc(X, Y, z)  # Z的形状和X,Y一致（100，100）
    ax.contour(X, Y, Z + z, [z], zdir='z', colors='r')
    '''
    #contour 等高线
    X,Y,Z是值（都是二维数组），如果指定：zdir='z'，
    levels：确定轮廓线的数量和位置，可以为正整数或数组，用数组时就是标明画指定Z轴值的等高线，没有[z]，则生成多个等高线
    Z轴值写为Z+z，但后续levels参数，制定了至绘制Z+z=z的等高线，也就是Z=0的情况，即surfaceFunc方程为0的解，
    结算过程相当于是穷尽X，Y的组合与当前z，带入方程找到合适的解，
    所以X，Y的容量越丰富（A中的采样点多），则当前等高线越精确，z的数量越多（B中采样点多）就会循环画出更多的等高线
    '''

# 画XZ平面的轮廓
for y in B:
    X, Z = A1, A2
    Y = surfaceFunc(X, y, Z)
    ax.contour(X, Y + y, Z, [y], zdir='y', colors='r')

# 画YZ平面的轮廓
for x in B:
    Y, Z = A1, A2
    X = surfaceFunc(x, Y, Z)
    ax.contour(X + x, Y, Z, [x], zdir='x', colors='r')

# 保持横纵轴的比例
ax.set_aspect('equal')
# 设置画图范围，否则范围可能会很不合适
ax.set_zlim3d(l1, l2)
ax.set_xlim3d(l1, l2)
ax.set_ylim3d(l1, l2)
# 隐藏所有刻度线
ax.axis('off')
# 展示
plt.show()

'''

#配合colormap，设置颜色变化范围
from matplotlib import colors
from matplotlib import cm
norm = colors.Normalize(vmin=l1, vmax=l2)
#cmap=cm.coolwarm,vmin = l1, vmax =l2)

#中文字体
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
#辅助的信息，非必要
ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_zlabel('z轴')
'''
