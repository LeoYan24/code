import matplotlib.gridspec as gridspec
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from matplotlib import patches

t = np.arange(0, 2 * np.pi, 0.01)

plt.rcParams['font.sans-serif'] = ['SimSun']  # sans-serif表示非衬线字体
plt.rcParams['axes.unicode_minus'] = False

''' 
layout=可选{'constrained', 'compressed', 'tight', 'none', LayoutEngine, None}
default: None
对应不同的填充方式，比如边框大
'''
fig = plt.figure( layout='constrained', figsize=(12, 4),dpi=100)

gs1 = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例
gs2 = gridspec.GridSpec(2, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例

ax1 = plt.subplot(gs1[0])
ax1.grid()  # 显示网格
ax1.set_title("1行布局，占1/3行，标号为0", loc='center')
draw_circle = patches.Circle((0, 0), radius=1, fill=False, color='r')
ax1.add_patch(draw_circle)
ax1.axis('scaled')
ax1.axis([-1.1, 1.1, -1.1, 1.1])

plt.subplot(gs2[1])
plt.title("2行布局，占2/3行，标号为1", loc='center')
plt.grid()
plt.plot(t,np.sin(t))

plt.subplot(gs2[4])
plt.title("2行布局，占2/3行，标号为4", loc='center')
plt.grid()
plt.plot(t,np.cos(t))

plt.tight_layout()
plt.show()
