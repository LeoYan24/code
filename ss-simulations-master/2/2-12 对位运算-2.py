import matplotlib.pylab as plt
import numpy as np

n1 = np.arange(0, 7)
x1 = (n1 - 3) * np.heaviside(n1 - 3, 1)
n2 = np.arange(3, 10)
x2 = -(n2 - 4) * np.heaviside(n2 - 4, 1)
'''方法1.只在公共区间求和'''
n = np.arange(3, 7)
y = x1[3:] + x2[:-3]
'''波形图'''
plt.plot(n1, x1, 'r')
plt.plot(n2, x2, 'g')
plt.axvline(3, ls='--')  # 给出有效区间辅助线
plt.axvline(6, ls='--')  # 给出有效区间辅助线
plt.legend(labels=['x1', 'x2', "x1+x2"], loc='best')  # 图例
plt.show()

'''方法2.扩展x1和x2到相同范围再求和'''
x1_1 = np.hstack([x1, [4, 5, 6]])
x2_1 = np.hstack([np.zeros(3), x2])
y = x1_1 + x2_1
n = np.arange(0, 10)
'''波形图'''
plt.plot(n1, x1, 'r')
plt.plot(n2, x2, 'g')
plt.plot(n, y, 'b')
plt.legend(labels=['x1', 'x2', "x1+x2"], loc='best')  # 图例
plt.show()
