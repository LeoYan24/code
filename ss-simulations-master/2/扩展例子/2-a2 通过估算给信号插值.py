import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(-10.0, 10.0, 0.01)  # 采样点：取-10.0到10.0，间隔为0.01
# 原始信号
y = np.piecewise(t, [t >= 0, t >= 2, t >= 3], [1, lambda x: 3 - x, 0, 0])  # lambda中的x是局部变量

'''通过前后值进行估算进行信号插值'''
'''
方法1：利用scipy的interp1d方法
构造一个插值时间轴，表示在原有的时间轴上增加密度
'''
t1 = np.arange(-10.0, 10.0, 0.005)
from scipy import interpolate

# f是一个插值函数
f = interpolate.interp1d(t, y, kind='linear', fill_value="extrapolate")  # kind可选#'linear','nearest'等
'''
如果下一句报错ValueError: A value in x_new is below the interpolation range.
在使用上述插值函数进行预测的时候，所给的x的取值超出了【生成该函数时候所使用的X】的取值范围，
函数给不出预测值，因此报错。
解决方法：加入参数：fill_value="extrapolate"，主要作用是预测序列两侧的值
'''
# 用上面生成f函数来进行实际的插值，注意参数是一个和源信号区间相同但密度更大的区间
y7 = f(t1)
print('scipy插值长度:', len(y7))
# 效果是由2000个点变成了4000个点，此时如果画图，需要重新构建一个画图时间轴
t2 = np.arange(-20.0, 20.0, 0.01)


'''方法2：利用numpy的库'''
y8 = np.interp(t1, t, y)
print('numpy插值长度:', len(y8))
