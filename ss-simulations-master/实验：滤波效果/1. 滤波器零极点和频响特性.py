import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import filter_define  # 滤波器定义

'''
统一仿真参数
#参见filter_define.py的定义
'''
a = filter_define.a
sample_freq = filter_define.sample_freq
sample_interval = filter_define.sample_interval
t = filter_define.t
f = filter_define.f
system = filter_define.system

'''求h(t)和H(jw)'''
t, ht = signal.impulse(system, T=t)
# freqresp方法需要用角频率
omega, Hw = signal.freqresp(system, f * 2 * np.pi)
Hw_amp = np.abs(Hw)  # 方法不是fft，不用做幅度修正
Hw_ang = np.angle(Hw)
'''得到零极点'''
sys = signal.lti(system[0], system[1])
poles = sys.poles
zeros = sys.zeros
print("零点：", zeros)
print("极点：", poles)
'''寻找半功率点并进行标注'''
'''写工具函数，寻找截止频率
如果得到的半功率点误差太大，
超过理论上的半功率点5%（主要是全通系统），
则说明这个截止频率不存在
'''


def get_fc(arr, threshold):
    if len(arr) > 0:
        id = np.argmin(np.abs(arr - threshold))  # 说明序列为空，无需判断
    else:
        return 0
    if abs(arr[id] - threshold) / threshold > 0.05:
        return 0
    else:
        return id


# 绘制单边谱线
Hw_amp_half = Hw_amp[len(Hw_amp) // 2:]
f_half = f[len(f) // 2:]
# 半功率点的幅度值
half_power = np.max(Hw_amp_half) / np.sqrt(2)
# 寻找幅频特性最大值所在的位置
id1 = np.argmin(np.abs(Hw_amp_half - max(Hw_amp_half)))
'''从两个方向寻找截止频率（带通情况）'''
# 下截频,从0hz到幅频最大值位置寻找半功率点
id2 = get_fc(Hw_amp_half[:id1], half_power)
if id2 != 0: print("截止频率（Hz）：", f_half[id2])
# 上截频，从幅频最大值位置到频率最大值寻找半功率点，加上最大值坐标，得到完整频率序号
id3 = get_fc(Hw_amp_half[id1:], half_power)
if id3 != 0:
    id3 = id1 + id3
    print("截止频率（Hz）：", f_half[id3])

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
'''左侧1/3绘制零极点图，右侧2/3绘制冲激响应和频响特性'''
plt.figure(figsize=(12, 6))
gs1 = gridspec.GridSpec(1, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例
gs2 = gridspec.GridSpec(3, 3, width_ratios=[1, 2, 0])  # 1/3 和 2/3 的比例
# 零极点图（支持二阶极点）
ax1 = plt.subplot(gs1[0])
plt.grid()
# 获得非重复的元素，以及元素的个数
z, cz = np.unique(zeros, return_counts=True)
p, cp = np.unique(poles, return_counts=True)
for i in range(len(p)):
    plt.plot(p[i].real, p[i].imag, 'x', markersize=10, color='none', markeredgecolor='b')
    if cp[i] > 1:
        plt.text(p[i].real - 0.1, p[i].imag + 0.05, cp[i], fontsize=12)
for i in range(len(z)):
    plt.plot(z[i].real, z[i].imag, 'o', markersize=10, color='none', markeredgecolor='b')
    if cz[i] > 1:
        plt.text(z[i].real + 0.05, z[i].imag + 0.05, cz[i], fontsize=12)
# 冲激响应
plt.subplot(gs2[1])
plt.grid()
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)
# 幅频特性
plt.subplot(gs2[4])
plt.grid()
plt.xlim(-5 * a / 2 / np.pi, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
# todo 如果希望绘制单边谱，注意此时幅度要乘以2
plt.xlim(0, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(jf)|$', loc='left')
plt.plot(f, Hw_amp)
# 在半功率点绘制一条虚线(Hw最大值 除以根号2) * np.ones，np.ones的长度和频轴f相同
plt.plot(f, half_power * np.ones(len(f)), ls='--', c='red')
plt.subplot(gs2[7])
plt.grid()
plt.xlim(-5 * a / 2 / np.pi, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
# todo 如果希望绘制单边谱
plt.xlim(0, 5 * a / 2 / np.pi)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$\phi(jf)$', loc='left')
# 由于t不是无限长，因此相位会不太准确
plt.plot(f, Hw_ang)
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)

plt.tight_layout()
plt.show()
