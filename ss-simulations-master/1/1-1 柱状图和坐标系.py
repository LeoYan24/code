import matplotlib.pyplot as plt

x = [1, 2, 4, 2, 3]
n = [1, 2, 3, 4, 5]
'''绘图'''
plt.figure()  # 新建绘图，无参数非必须
plt.bar(n, x)  # 折线图
plt.grid()  # 显示网格线
plt.title('Line chart')  # 显示标题
plt.xlabel('n')  # x轴标签
plt.ylabel('x')  # y轴标签
plt.xlim(0, 5)  # 限定x轴范围
plt.ylim(0, 5)  # 限定y轴范围
plt.show()  # 显示图像
