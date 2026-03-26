import numpy as np

t = np.arange(0, 5)  # 原始区间
x = np.array([1, 2, 3, 4, 5])  # 原始信号
print("原始序列：", x)

print("-----------1：利用dstack+flatten方法补零--------------")
# 注意利用dstack的参数是个元组，用小括号括起来
x1 = np.dstack((x, np.zeros_like(x))).flatten()  # 注意dstack的参数是元组
print('元素之间插入一个0：', x1)
x2 = np.dstack((x, np.zeros_like(x), np.zeros_like(x))).flatten()
print('元素之间插入两个0：', x2)

print("-----------2：利用insert方法补零--------------")
'''
注意，利用insert函数中的第二个参数，是一个整数序列n，标明的是补零的位置
可以思考：如果需要将0补在原有数值之前，position应该怎么写
'''
position = np.arange(1, 6)
x1 = np.insert(x, position, 0)
print('x补一个零：', x1)

position = np.arange(1, 11,2) #间隔2个位置插入0
x2 = np.insert(x1, position, 0)  # 再次补零，相当于补3个零
print('x再次补零，相当于补2个零：', x2)

print("----------3：利用Flatten方法补零,比较繁琐--------------")
# 把x变为只有一行的二维数组形式
x_2D =[x]
#或者：x_2D = np.matrix(x)
#或者：x_2D = x.reshape(1, len(t))
print('把x变为只有一行的二维数组形式：', x_2D)
#这种append方法，是在矩阵中插入一个新行“ np.zeros...” ，这个新行也是一个只有一行的二维数组
x_matrix = np.append(x_2D, [np.zeros_like(t)], axis=0)
print('x补一次零，成为两行的二维数组\n', x_matrix)
x1 = x_matrix.flatten('F')
print('补零之后压平到一维数组：', x1)

# 再补一次零
x_matrix2 = np.append(x_matrix, [np.zeros_like(t)], axis=0)
print('x补两次零得到三行的2维数组\n', x_matrix2)
x2 = x_matrix2.flatten('F')
print('x补两次零之后压平到一维数组：', x2)
