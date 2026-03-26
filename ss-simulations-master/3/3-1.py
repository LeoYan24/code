import matplotlib.pylab as plt  # 绘制图形
import numpy as np

n = np.arange(0, 20)
x1 = np.sin(0.25 * np.pi * n)
x2 = np.sin(0.125 * np.pi * n)
# 信号分别经过系统，再叠加
y1 = x1 ** 2 + x2 ** 2
# 信号先叠加，再经过系统
y2 = (x1 + x2) ** 2

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(211)
plt.title("信号分别经过系统，再叠加", loc='left')
plt.grid()
plt.stem(n, y1)

plt.subplot(212)
plt.grid()
plt.title("信号先叠加，再经过系统", loc='left')
plt.stem(n, y2)

plt.tight_layout()
plt.show()
