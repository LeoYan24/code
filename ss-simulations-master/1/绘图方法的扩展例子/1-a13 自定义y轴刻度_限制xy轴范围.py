import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimSun']  # sans-serif表示非衬线字体
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10
'''公式字体风格——stix'''
plt.rcParams['mathtext.fontset'] = 'stix'

plt.figure()
plt.grid()  # 显示网格
plt.title("将$y$轴刻度设置为$\pm\pi$的倍数，隐藏$x$轴刻度", loc='center')
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)  # 范围为-π到π之间，这是y轴刻度
labels = map(lambda x: f"${x / np.pi}π$", y)  # 利用map函数制作一个文本列表，显示1π、2π、3π这种字符串
plt.yticks(y, labels, fontsize=14)
'''上面三局等价于下面语句，但如果刻度较多就不好用了
plt.yticks([- np.pi, - np.pi / 2, 0, np.pi / 2, np.pi], [r"$-π$", r"$-π/2$", r"$0$", r"$π/2$", r"$π$"],fontsize = 14)
'''
# 显示示例数据
t = np.arange(-5, 5, 0.01)
plt.plot(t, np.arctan(t))
plt.ylim(-1.1 * np.pi, 1.1 * np.pi)  # 设置y轴范围
plt.xlim(-3, 3)  # 设置x轴范围
plt.xticks(fontsize=14)  # 放大x轴刻度字体
plt.show()
