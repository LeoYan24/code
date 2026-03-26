import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''手动构建“连续”信号'''
t = np.arange(-5, 5 + 0.001, 0.001)
xt = np.heaviside(t, 1) - np.heaviside(t - 1, 1)
ht = np.sin(t) * (np.heaviside(t, 1) - np.heaviside(t - np.pi, 1))
rt1 = (1 - np.cos(t)) * (np.heaviside(t, 1) - np.heaviside(t - 1, 1))
rt2 = (np.cos(t - 1) - np.cos(t)) * (np.heaviside(t - 1, 1) \
                                     - np.heaviside(t - np.pi, 1))
rt3 = (np.cos(t - 1) + 1) * (np.heaviside(t - np.pi, 1) \
                             - np.heaviside(t - np.pi - 1, 1))
rt = rt1 + rt2 + rt3
'''构建抽样信号，进行卷积近似运算'''
dt = 0.2  # 抽样间隔
n = np.arange(-5, 5 + dt, dt)
en = np.heaviside(n, 1) - np.heaviside(n - 1, 1)
hn = np.sin(n) * (np.heaviside(n, 1) - np.heaviside(n - np.pi, 1))
rn = np.convolve(en, hn, mode='same') * dt

'''将理论值绘制为折线图、实际值绘制为柱状图'''
'''绘图'''
plt.subplot(3, 1, 1)
plt.xlim(-1, 5)
plt.ylabel('e(t)')
plt.plot(t, xt, 'r',linewidth=3)
plt.bar(n, en, edgecolor='black', color='c', width=dt)

plt.subplot(3, 1, 2)
plt.xlim(-1, 5)
plt.ylabel('h(t)')
plt.plot(t, ht, 'r',linewidth=3)
plt.bar(n, hn, edgecolor='black', color='c', width=dt)

plt.subplot(3, 1, 3)  # 画布位置3
plt.xlim(-1, 5)
plt.ylabel('r(t)')
plt.plot(t, rt, 'r',linewidth=3)
plt.bar(n, rn, edgecolor='black', color='c', width=dt)

plt.tight_layout()
plt.show()
