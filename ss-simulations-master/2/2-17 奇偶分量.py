import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''注意：如果区间不是对称的，例如在（1，10）之间，则需要手动创建新坐标轴'''
t = np.linspace(-10.0, 10.0, 200)  # 采样点：取-10.0到10.0，间隔为0.1
y = np.piecewise(t, [t >= 1, t >= 2, t >= 3], [1, lambda x: 3 - x, 0, 0])
'''翻转方法1'''
# y2 =  y1[::-1]
'''翻转方法2，要求numpy版本在1.12版以上'''
y_flip = np.flip(y)
'''计算奇偶分量'''
y_even = 0.5 * (y + y_flip)
y_odd = 0.5 * (y - y_flip)

'''波形图'''
plt.subplot(221)
plt.grid()
plt.title("f(t)")
plt.plot(t, y)

plt.subplot(222)
plt.grid()
plt.title("f(-t)")
plt.plot(t, y_flip)

plt.subplot(223)
plt.grid()
plt.title("f_even")
plt.plot(t, y_even)

plt.subplot(224)
plt.grid()
plt.title("f_odd")
plt.plot(t, y_odd)

plt.tight_layout()
plt.show()
