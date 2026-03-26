import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

plt.rcParams['font.sans-serif'] = ['SimSun']  # sans-serif表示非衬线字体
plt.rcParams['axes.unicode_minus'] = False

'''
注意使用”plt“和”ax1“的两种绘图风格，
二者语法有些差异，比如：
ax1.set_title("画圆，以及调整边框")
plt.title("图例和标注")
利用plt方式时，可以用 ax = plt.gca()，来获得当前的axes

基于ax1进行绘图操作，在多子图的情况下逻辑更清晰一些，比如本例
直接用plt进行操作，更简单，参见其他大多数示例
'''

'''注意画圆需要获得所谓‘绘图区域’，也就是代码中的ax1
如果只用一个子图：
fig, ax1 = plt.subplots()
如果使用多个子图
fig = plt.figure()
ax1 = plt.subplot(2, 2, 1)
画圆方式：先生成圆，再添加（add_artist或add_patch）到当前的绘图区域ax1
此外，如果不将xy轴设置为正圆，则绘图结果可能是椭圆
'''
_, ax1 = plt.subplots(figsize=(8, 6), dpi=100)
ax1.grid()  # 显示网格
ax1.set_title("画圆，以及调整边框和刻度", loc='center')
# 画圆方式1
draw_circle1 = plt.Circle((0, 0), radius=0.8, fill=False, color='black', ls='--')
ax1.add_artist(draw_circle1)
# 画圆方式2
draw_circle2 = patches.Circle((0, 0), radius=1.2, fill=False, color='r', ls='--')
ax1.add_patch(draw_circle2)
# 保持xy轴成正方形，使得圆为正圆
ax1.set_aspect(1)
# ax1.axis('scaled')#另一种设置方法
# 设置坐标范
ax1.axis([-2, 2, -1.5, 1.5])
'''调整边框的位置和效果，一般也基于ax1进行'''
ax1.spines['bottom'].set_position(('data', 0))  # 把底边框（轴）绑定到y=0处
ax1.spines['left'].set_position(('data', 0))  # 把左边框（轴）绑定到x=0处
ax1.spines['right'].set_visible(False)  # 隐藏右边框
ax1.spines['top'].set_visible(False)  # 隐藏上边框
ax1.xaxis.set_ticklabels([])  # 把x轴刻度标签设置为空，即隐藏刻度
ax1.yaxis.set_ticklabels([])  # 把y轴刻度标签设置为空，即隐藏刻度
plt.show()
