import matplotlib.pyplot as plt
import numpy as np
# 注意画圆在patches
from matplotlib import patches
from scipy import signal

t1 = np.arange(0, 20, 0.001)

# todo 带入不同的参数值，分析过阻尼、欠阻尼、无阻尼、临界阻尼情况
# L=1;C=1;R=0;
#L = 1;C = 1;R = 0.2;
#L=1;C=1;R=2;
L=1;C=1;R=3;

# 求特征根
x = np.array([1, R / L, 1 / L / C])
rts = np.roots(x)

#todo 记录特征根
print(rts)
# 直接求冲激响应的数值解
#todo 如何定义系统
system = ([1 / L / C], [1, R / L, 1 / L / C])
t, h = signal.impulse(system, T=t1)
# 直接求阶跃响应的数值解
t, g = signal.step(system, T=t1)

'''图的初始化'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(12, 5))
# 第一个子图，显示特征根(极点)的变化
ax1 = plt.subplot(121)
#画圆
unit_circle = patches.Circle((0, 0), radius=np.sqrt(1/L/C), fill=False, color='black', ls='--')
ax1.add_patch(unit_circle)
plt.scatter([rts[0].real, rts[1].real], [ rts[0].imag,rts[1].imag], marker='x', c='r')
#todo 可选，标注R值或其他参数
#plt.text(0.01, 0.01,r"$R=$%.2f" % R)
ax1.grid()
ax1.axis('scaled')  # 保持坐标系统正圆
#根据根号下1/LC和特征根的最小值，自动确定坐标范围（并扩大1.1倍）
ax1.axis([min(min(rts),-np.sqrt(1/L/C))*1.1, np.sqrt(1/L/C) *1.1, -np.sqrt(1/L/C) *1.1, np.sqrt(1/L/C) *1.1])  # 坐标范围

# 第二个子图，显示响应的阻尼变化
ax2 = plt.subplot(122)
plt.grid()
plt.plot(t, h)
plt.plot(t, g)
plt.legend(["冲激响应", "阶跃响应"])
plt.show()
