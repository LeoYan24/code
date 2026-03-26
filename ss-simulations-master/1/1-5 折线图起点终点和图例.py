import matplotlib.pylab as plt  # 绘制图形

'''结论：matplotlib画折线图的方式和x轴数据的排列顺序有关'''
x = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 调整横坐标顺序，相应（根据实际情况）调整y轴顺序
x1 = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
y1 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.plot(x, y, "b-o", fillstyle='none')
plt.annotate('起点', (1, 1), xytext=(-25, 25),
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线

plt.annotate('终点', (-1, 10), xytext=(25, -25),
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线

plt.subplot(2, 1, 2)
plt.plot(x1, y1, "b-o", fillstyle='none')
plt.annotate('起点', (-5, 6), xytext=(20, 25),
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线

plt.annotate('终点', (5, 5), xytext=(-25, 25),
             textcoords='offset points', arrowprops=dict(arrowstyle="->"))  # 画引导线

plt.show()
