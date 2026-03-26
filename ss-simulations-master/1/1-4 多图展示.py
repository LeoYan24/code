import matplotlib.pyplot as plt

x = [1, 2, 4, 2, 3]  # 示例数据-1
n = [-2, -1, 0, 1, 2]  # 绘图的横坐标，

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 2, 1)
plt.title("折线图")
plt.grid()
plt.plot(n, x)

plt.subplot(2, 2, 2)
plt.title("茎叶图")
plt.grid()
plt.stem(n, x)

plt.subplot(2, 2, 3)
plt.title("散点图")
plt.grid()
plt.scatter(n, x)

plt.subplot(2, 2, 4)
plt.title("柱状图")
plt.grid()
plt.bar(n, x)

plt.suptitle("多图效果举例")  # 设置总的标题
plt.tight_layout()  # 紧凑布局，防止标题和图重叠，酌情使用
plt.show()
