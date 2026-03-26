import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 4, 2, 3])  # 示例数据-1
x2 = np.array([0, 1, 2, 3, 4])  # 示例数据-2
n = np.array([-2, -1, 0, 1, 2])  # 绘图的横坐标，

fig = plt.figure()  # 新建绘图
'''
rcParams的可调节内容
https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams'''
# 中文支持
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.grid()  # 显示网格
plt.title("辅助线")
plt.xlim(0, 5)  # 限定x轴范围
plt.ylim(0, 5)  # 限定y轴范围
plt.xlabel("横坐标标签", loc='right')
plt.ylabel("纵坐标标签", loc='top')
# 横竖线,xmax、ymax指定的是数值指定的是比例（可以针对ylim、xlim设定）
plt.axhline(1, xmin=0, xmax=0.8, ls='--', c='b')
plt.axvline(1, ymin=0, ymax=0.8, ls='--', c='b')
# 横竖线,xmax、ymax指定的是数值指定的是数值
plt.hlines(2, xmin=0, xmax=2, ls='--', colors='r')
plt.vlines(2, ymin=0, ymax=2, ls='--', colors='r')
# 斜线，经过（2，2），斜率1
plt.axline((2, 2), slope=1, color="black", ls='--')

plt.show()
