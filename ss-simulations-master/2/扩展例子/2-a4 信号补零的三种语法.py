import numpy as np

'''
信号插值
即时间轴的区间不变，但采样间隔缩小，采样的密度增加,例如：
从：t = np.arange(-5, 5, 1)  
变为：t2 = np.arange(-5, 5, 0.5) 
此时y的数值点不够了，则需要进行插值(interpolation)。
如果变为：t3 = np.arange(-5, 5, 2)
则此时y的数值太多了，需要均匀删减一些点(downsampling)
'''

# 原始区间
t = np.arange(-5, 5, 1)
# 新区间（t->0.5t，需要信号补点）
t_ip = np.arange(-5, 5, 0.5)
# 新区间（t->2t，需要信号删减点）
t_ds = np.arange(-5, 5, 2)
print("三个区间的采样点数量：", len(t), len(t_ip), len(t_ds))
# 原始信号
y = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print("原始序列：", y)

'''
在原序列中插入零值（即信号与系统教材中的情况）
注意这里采用的两种方法，都需要手动构造新的时间轴
'''
print("-----------1：利用insert方法补零--------------")
# 方法1,利用insert函数，但补零的数量受到一定的限制
# 注意，如果t = np.arange(-5.0, 5.0, 1)，即t中数值存在非整数，则insert方法会报错
y_ip = np.insert(y, t, 0)  # 补一个零
print('y补一个零：', y_ip)
y_ip2 = np.insert(y_ip, t, 0)  # 再次补零，相当于补3个零
print('y再次补零，相当于补三个零：', y_ip2)

print("-----------2：利用Flatten方法补零--------------")
# 方法2：利用Flatten方法补零
# 把y变为只有一行的二重数组形式
y_F01 = y.reshape(1, len(t))
# 或者: y_matrix = [y]
print('把y变为只有一行的二维数组形式：', y_F01)
y_matrix = np.append(y_F01, np.zeros(len(t)).reshape(1, len(t)), axis=0)
print('y补一次零，成为两行的二维数组\n', y_matrix)
y_ip = y_matrix.flatten('F')
print('补零之后压平到一维数组：', y_ip)
# 再补一次零
y_F02 = np.append(y_F01, [np.zeros(len(t))], axis=0)
print('y补两次零得到三行的2维数组\n', y_F02)
y_ip2 = y_F02.flatten('F')
print('y补两次零之后压平到一维数组：', y_ip2)

# 其他补零的方法
print("-----------3：利用dstack+flatten方法补零--------------")
# 注意参数是个元组，用小括号括起来
y_matrix = np.dstack((y, np.zeros_like(y)))
print('dstack方法效果：', y_matrix)
y_ip = np.dstack((y, np.zeros_like(y))).flatten()
print('dstack+flatten方式：', y_ip)


'''删减点'''
print("-----------6：删减点--------------")
print("原始序列：", y)
# 方法1：采用冒号方法，可以做到删n个点，取一个点
y_ds = y[::2]
print('用冒号方法间隔一个点删一个点：', y_ds)
y_ds2 = y[::3]
print('用冒号方法间隔间隔两个点取一个点（即间隔1个点删2个）：', y_ds2)

# 方法2：delete方法删减点，但只能做到间隔n个点删一个
# indexes为delete的索引，即删除索引所在的位置
# 考虑到原序列有10个样本，如果想删除第2、4、6、8、10个点，则：
indexes = range(0, 10, 2)
y_ds = np.delete(y, indexes)
print('用delete方法间隔一个点删一个点：', y_ds)
# 想间隔两个点删除一个点，则：
indexes = range(0, 10, 3)
y_ds2 = np.delete(y, indexes)
print('用delete方法间隔间隔两个点取一个点（即间隔2个点删1个）：', y_ds2)

print("-----------7：降采样--------------")
# 方法3：降采样方法，序列改动较大，理论上只能保持包络线一致
from scipy import signal

y_ds = signal.resample(y, len(t_ds))  # 降采样方法
print('重采样', y_ds)  # [2.         3.         4.         1.38196601 4.61803399]
y_ds2 = signal.resample(y, 8)  # 10个点减到8个点
print('重采样', y_ds2)  # [1.         2.62361808 3.         5.37638192 1.         2.62361808    3.         5.37638192]
