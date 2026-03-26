import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# 时间轴
t = np.arange(-10, 10, 0.01)
n = np.arange(-10, 10, 0.5)
'''
初始化:注意这里设置的所有空值，都必须再动画中更新，否则会报错
反之，这里如果设置的初值(非空)，后续动画中可以不更新
'''

plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False
# 多个子图的情况
fig = plt.figure()

'''子图1'''
ax1 = plt.subplot(311)
ax1.axis([-1, 1, -1, 1])  # 坐标范围
ax1.set_title('散点的动画')
# 散点1
scat1 = ax1.scatter([], [], marker='o', c='None', edgecolors='r')
# 散点2(方式2)
scat2, = ax1.plot([], [], 'x', c='b')

'''子图2'''
ax2 = plt.subplot(312)
ax2.set_title('辅助线和文本的动画')
# 一段文本
tx1 = ax2.text(np.nan, np.nan, "")
# 竖线和横线
# 注意axvline的x参数需要输入一个float值，np.NaN是一个float型的空值，但None不行
axv = ax2.axvline(x=np.nan, ls='--', c='red')  # 竖线
axh = ax2.axhline(y=np.nan, ls='--', c='red')  # 横线
ax2.axis([-1, 1, -1, 1])  # 坐标范围
'''子图3'''
ax3 = plt.subplot(313)
ax3.grid()
ax3.set_title('圆的动画')
ax3.axis([-20, 20, -5, 5])  # 坐标范围，先x后y
# 一段文本
# 一个圆
ax3.axis('scaled')  # 保持坐标系统正圆
draw_circle = plt.Circle((0, 0), radius=np.nan, fill=False, color='black', ls='--')
ax3.add_artist(draw_circle)


def animate(i):
    """图1：更新散点"""
    '''图1：更新散点
    scatter采用set_offsets方式更新数据
    更新格式为元组+数组：([x1,y1],[x2,y2],[x3,y3]……)
    有时候需要自己构造一下这种数据格式'''
    plist = np.append([n], [np.sin(10 * n - i)], axis=0).T  # 把n和f3合并为二维数组，再转置
    scat1.set_offsets(plist)
    '''用plot方式画散点，更新方式更简单一些 '''
    scat2.set_data(n, np.cos(10 * n - i))
    '''图2：更新文字'''
    x = i * 0.1 - 1
    y = i * 0.05 - 0.5
    tx1.set_text(r"当前坐标：(%.2f,%.2f)" % (x, y))
    tx1.set_position((x, y))
    '''图2：更新辅助线'''
    axv.set_data(x * np.ones(int(2 / 0.01)), np.arange(-1, 1, 0.01))
    axh.set_data(np.arange(-1, 1, 0.01), y * np.ones(int(2 / 0.01)))
    '''方式2：制作辅助线段
        注意这axv.set_data（画竖线），第一个参数是x坐标位置，第二个参数是线占y轴范围的比例（不是y的数值），比如20%到80%，
        所以调起来很麻烦，需要根据轴的范围将数值映射为比例，例如：
        (x - 0.1 + 1)和(x + 0.1 + 1)是竖线的上下限相对于坐标轴下限-1的距离，距离除以轴的范围2，则是得到起止点在轴的比例位置
        axh.set_data同理
        这里做了0.2长的横线段和0.6长的纵线段（和画面显示比例有关），根据xy轴的范围手算起止点在画面的比例 '''
    '''
    x_range = np.arange((x - 0.1 + 1) / 2, (x + 0.1 + 1) / 2, 0.01)
    y_range = np.arange((y - 0.3 + 1) / 2, (y + 0.3 + 1) / 2, 0.01)
    axv.set_data(x * np.ones_like(y_range), y_range)
    axh.set_data(x_range, y * np.ones_like(x_range))
    '''
    '''图3：更新圆的半径，对于patch类的绘图，直接更新属性即可'''
    draw_circle.radius = 1 + i * 0.1
    ax3.set_title(r'圆的动画，$r=%.2f$' % (1 + i * 0.1))  # 更新title

    return


ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=300)
plt.tight_layout()
ani.save("../../data/a-tau-2.gif", writer='pillow')
plt.show()
