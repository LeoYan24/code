import matplotlib.pylab as plt  # 绘制图形
import numpy as np

# 绘图参数，支持中文
ax = plt.figure(figsize=(16, 9))  # 指定图像比例
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

# Fs: 抽样频率
Fs = 8000
# T: 抽样间隔
T = 1 / Fs
# N: 输入序列的长度
N = 80
n = np.arange(0, N)
t = n * T
# 正弦波的频率
f = 200
# 正弦波叠加噪声
x = np.sin(f * 2 * np.pi * t) + 0.2 * np.random.randn(N)
print(x.size)
# 第1个滤波器，滑动平均
h1 = 0.5 * np.array([1, 1])
# 第2个滤波器，差分
h2 = 0.5 * np.array([1, -1])

# 利用卷积求响应
# t = np.convolve(et,ht,mode='same') * sample_interval
y1 = np.convolve(x, h1)
y2 = np.convolve(x, h2)
ny = np.arange(0, y1.size)
print(ny.size)
plt.subplot(311)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xlim([-0, N])
plt.stem(n, x)

plt.subplot(312)
plt.xlabel('n')
plt.ylabel('$y_1$[n]')
plt.xlim([-0, N])
plt.stem(ny, y1)

plt.subplot(313)
plt.xlabel('n')
plt.ylabel('$y_2$[n]')
plt.xlim([-0, N])
plt.stem(ny, y2)

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
