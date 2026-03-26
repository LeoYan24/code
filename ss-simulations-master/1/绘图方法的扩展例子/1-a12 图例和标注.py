import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

x1 = np.array([0, 1, 2, 3, 4])
x2 = np.array([1, 2, 4, 2, 3])
x3 = np.array([2, 3, 1, 0, 2])
n = np.array([-2, -1, 0, 1, 2])

fig = plt.figure( figsize=(8, 4),dpi=100)  # 新建绘图 layout=可选{'constrained', 'compressed', 'tight', 'none', LayoutEngine, None}, default: None
# 中文支持
plt.rcParams['font.sans-serif'] = ['SimSun']  # sans-serif表示非衬线字体
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

plt.subplot(121)
plt.title("图例（方式1）")
plt.grid()  # 显示网格
plt.plot(n, x1)
plt.plot(n, x2 , "b-.")
plt.plot(n, 1 * np.ones_like(n), "r--")  # 画一条横虚线，在y=1的位置
plt.legend(labels=['数据1', '数据2', "横虚线"], loc='best')  # 图例，对应画线的顺序


plt.subplot(122)
plt.grid()  # 显示网格
plt.title("图例（方式2）和标注")
l1, = plt.plot(n, x1)
l2, = plt.plot(n,x2)
# 图例
plt.legend(handles=[l1, l2], labels=['x1', 'x2'], loc='best')
# 第一个标注点
plt.annotate('这是x1', (1, 2),
             xytext=(20, 0),  # 标注文本的位置（偏移量）
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线.默认直线箭头

# 第二个标注点
plt.annotate('这是x2', (0, 2), xytext=(25, -25),
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=90,rad=10"))  # 画引导线
# connectionstyle语句定义一个拐直角湾的线，没有这一句默认是直线

plt.tight_layout()
plt.show()
