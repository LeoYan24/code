import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''
该方法可用于直接演示，优势是语法简单，
原理就是打开交互模式（ion），不断清空旧图（clf）画新图（plot）
但无法保存，也就无法把图存到ppt里
此外，该方法在循环播放等方面也需要额外工作
'''
# 绘图参数，支持中文和非交互式（连续动画效果）
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
figure = plt.subplots()
# 打开交互模式
plt.ion()
# 定义t区间
t = np.arange(-1, 1, 0.01)
# 循环画图，形成动画
for phi in np.arange(0, 10, 0.1):
    # 产生余弦载波
    f1 = np.cos(10 * t + phi)
    # 绘图
    plt.plot(t, f1, 'b')
    plt.show()  # 或者用plt.draw()和show效果相同
    # 停顿0.2秒
    plt.pause(0.2)
    plt.clf()  # clf清理当前的figure
