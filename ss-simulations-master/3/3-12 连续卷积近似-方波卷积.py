import matplotlib.pyplot as plt
import numpy as np
fs = 4096  # 采样频率
dt = 1 / fs  # 采样间隔
t = np.arange(0, 20, dt)
e = np.heaviside(t, 1) - np.heaviside(t - 10, 1)
h = np.heaviside(t, 1) - np.heaviside(t - 5, 1)
r1 = np.convolve(e, h, mode='same') * dt    #same 模式
r2 = np.convolve(e, h, mode='full') * dt    #full模式
r2 = r2[:len(t)]  # 把full模式后面的零裁切掉,以便适配t的长度

'''绘图'''
plt.subplot(2, 2, 1)
plt.title("e(t)", loc='left')
plt.plot(t, e, c='r')
plt.grid()

plt.subplot(2, 2, 2)
plt.title("h(t)", loc='left')
plt.plot(t, h, c='g')
plt.grid()

plt.subplot(2, 2, 3)
plt.title("r(t)-same mode", loc='left')
plt.plot(t, r1, c='purple')
plt.grid()

plt.subplot(2, 2, 4)
plt.title("r(t)-full mode", loc='left')
plt.plot(t, r2, c='purple')
plt.grid()
plt.tight_layout()
plt.show()
