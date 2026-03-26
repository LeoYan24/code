import numpy as np
from numpy.fft import fftfreq, fftshift

# todo 确定仿真参数（注意和其他实验保持一致）
'''
对于一阶的LPF和HPF
时域分析时，a = 1/RC，即1/a为时间常数，当t=(3~5)时，视为充放电结束
频域分析时，a = 1/RC，即为低通滤波器的截止（角）频率（半功率点）,截至频率则为：a/2pi
对于其他滤波器，a是一个基准参数，因为t、f等变量是依托a自适应的
设置截止频率时，应尽量和a保持一致
'''
a = 2 * np.pi * 100
# 通用参数
sample_freq = 8000
sample_interval = 1 / sample_freq
# t的长度不能太短，否则频谱图精度不够
t = np.arange(0, 1000 / a, sample_interval)
# 频谱范围
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
# freqresp方法需要用角频率
omega = f * 2 * np.pi

# todo 选择滤波器（注意和其他实验保持一致）
'''一阶低通电路'''
lpf = ([a], [1, a])
'''一阶高通电路'''
hpf = ([1, 0], [1, a])
'''全通电路'''
arf = ([1, -a], [1, a])
'''调节z和p的关系，获得不同的滤波关系（尽量保持在a附近）'''
z = a * 0.5
p = a * 2
filter_4 = ([1, z], [1, p])
'''低通'''
filter_5 = ([0, 1, 0], [a, 3, a])
'''通过高通低通滤波器串联得到带通滤波器（截止频率尽量保持在a附近）'''
fc1 = a * 2  # 上截频
fc2 = a / 2  # 下截频
# 滤波特性（理论值）
# print("下截频(Hz)：",fc1,"上截频(Hz)：",fc2)
bpf = ([fc1, 0], [1, fc1 + fc2, fc1 * fc2])
'''带阻滤波器'''
'''
RLC串联谐振电路
L=100e-3H、C=25e-6F时，谐振频率在100Hz左右（尽量保持在a附近）
调节R，可以获得不同的品质因数，从而获得不同的通频带
'''
R = 10
L = 100e-3
C = 25e-6
w0 = 1 / np.sqrt(L * C)
f0 = w0 / 2 / np.pi
Q = f0 * 2 * np.pi * L / R
# 串联谐振截止频率公式
fc1 = (-w0 / 2 / Q + np.sqrt((w0 / 2 / Q) ** 2 + w0 ** 2)) / 2 / np.pi
fc2 = (w0 / 2 / Q + np.sqrt((w0 / 2 / Q) ** 2 + w0 ** 2)) / 2 / np.pi
# 显示滤波特性（理论值）
# print("谐振频率(Hz)：",f0,"品质因数Q：",Q)
# print("下截频(Hz)：",fc1,"上截频(Hz)：",fc2)
bpf2 = ([1, 0], [L / R, 1, 1 / C / R])

# todo 选择滤波器（所有实验保持一致）
system = lpf
