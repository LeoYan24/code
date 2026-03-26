import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(0, 10, 0.1)

'''定义分段函数 方法1'''
x1 = np.piecewise(t, [t >= 0, t >= 1, t >= 2, t >= 3],
                  [lambda t: t, 1, lambda t: 3 - t, 0, 0])

'''定义分段函数 方法2'''
def cut(x):
    if 0 <= x < 1:
        y = x
    elif 1 <= x < 2:
        y = 1
    elif 2 <= x < 3:
        y = 3 - x
    else:
        y = 0
    return y

x2 = np.array([cut(i) for i in t])

'''定义分段函数 方法3'''
t1 = np.arange(0, 1, 0.1)
x3_1 = t1
t2 = np.arange(1, 2, 0.1)
x3_2 = np.ones_like(t1)
t3 = np.arange(2, 3, 0.1)
x3_3 = 3 - t3
x3_4 = np.zeros(len(t) - len(t1) - len(t2) - len(t3))
x3 = np.hstack([x3_1, x3_2, x3_3, x3_4])

'''波形图'''
plt.figure()
plt.plot(t, x3)  # 可自行选择绘制x1或x2、x3
plt.grid()
plt.show()
