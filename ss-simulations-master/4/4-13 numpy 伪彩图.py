import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifft, ifftshift

# 参数
fs = 8000  # 采样率，44100是CD等音频设备的常用采样率
length = 1  # 时长s

'''定义时间和频率轴'''
t = np.arange(0, length, 1 / fs) #单段信号区间
'''DTMF的频率组合'''
num = {
    '1': [697, 1209],
    '2': [697, 1336],
    '3': [697, 1477],
    'A': [697, 1633],
    '4': [770, 1209],
    '5': [770, 1336],
    '6': [770, 1477],
    'B': [770, 1633],
    '7': [852, 1209],
    '8': [852, 1336],
    '9': [852, 1477],
    'C': [852, 1633],
    '*': [941, 1209],
    '0': [941, 1336],
    '#': [941, 1477],
    'D': [941, 1633],
}
# 函数：生成对应的sin和合并后的波形
def getNumWave(numstr):
    # 注意这和之前定义方式有所不同，这里定义的是模拟角频率
    sin1 = np.sin(2 * np.pi * num[numstr][0] * t)  # 生成低频部分正弦波
    sin2 = np.sin(2 * np.pi * num[numstr][1] * t)  # 生成高频部分正弦波
    DTMFsin = sin1 + sin2  # 组合一下
    return DTMFsin
'''定义信号'''
sig1 = getNumWave('1')
sig2 = getNumWave('5')
sig3 = getNumWave('9')
sig = np.hstack((sig1, sig2, sig3))
'''时频图'''

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 14  # 设置字体大小
plt.figure(figsize=(8, 6))
plt.ylim(0, 2000)
# 保存specgram返回的结果，用于创建colorbar
spec, freqs, t, im = plt.specgram(sig, Fs=fs)
# 添加colorbar
plt.colorbar(im, label="功率/频率 (dB/Hz)")
#plt.title("DTMF信号频谱图")
plt.xlabel("时间 (秒)")
plt.ylabel("频率 (Hz)")
plt.tight_layout()
plt.show()

