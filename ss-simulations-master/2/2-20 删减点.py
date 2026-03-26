import numpy as np
from matplotlib import pyplot as plt

# 原始区间,绘图和降采样使用
t = np.arange(0, 5)
x = np.array([1, 2, 3, 4, 5])  # 原始信号
print("原始序列：", x)
'''方法1：采用冒号方法，可以做到删n个点，取一个点'''
x1 = x[::2]
print('用冒号方法间隔1个点删1个点：', x1)
x2 = x[::3]
print('用冒号方法间隔间隔2个点取1个点：', x2)
'''方法2：delete方法删减点，间隔2个点删一个'''
# delete方法删减点，只能做到间隔n个点删一个
# indexes为delete的索引，即删除索引所在的位置
# 考虑到原序列有10个样本，如果想删除第2、4、6、8、10个点，则：
indexes = range(0, 5, 2)
x3 = np.delete(x, indexes)
print('用delete方法间隔一个点删一个点：', x3)
'''方法3：降采样方法，理论上只能保持包络线一致'''
from scipy import signal
x4 = signal.resample(x, 3)
print('resample降采样:', x4)
x5 = signal.resample(x, 8, t)
print('resample降采样:', x5)

'''序列图'''
plt.title("$x$(n)", loc='left')
plt.grid()
plt.stem(t, x, 'r--')
plt.stem(x5[1], x5[0])
plt.show()
