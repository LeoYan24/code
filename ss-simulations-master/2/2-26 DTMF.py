import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

fs = 24000  # 采样率，44100是CD等音频设备的常用采样率
length = 1  # 时长s
t = np.arange(fs * length)  # 自然数列，相当于定义了n
'''DTMF的频率组合，该结构为一个字典结构'''
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
    low_df = 2 * np.pi * num[numstr][0] / fs
    high_df = 2 * np.pi * num[numstr][1] / fs
    discrete_sin1 = np.sin(low_df * t)  # 生成低频部分正弦波
    discrete_sin2 = np.sin(high_df * t)  # 生成高频部分正弦波
    DTMFsin = discrete_sin1 + discrete_sin2  # 组合
    return discrete_sin1, discrete_sin2, DTMFsin

numstr = '2'
sin1, sin2, DTMFsin = getNumWave(numstr)  # 以数字2为例，生成相应的波形
sd.play(DTMFsin, fs, blocking=True)  # 播放

'''绘图'''
len = 200  # 折线图长度,如果过多则无法清晰显示出正弦信息
plt.subplot(221)
plt.grid()
plt.plot(t[:len], sin1[:len], c='blue', label=str(num[numstr][0]) + 'Hz')
plt.legend(loc='lower right')  # 图例

plt.subplot(222)
plt.grid()
plt.plot(t[:len], sin2[:len], c='red', label=str(num[numstr][1]) + 'Hz')
plt.legend(loc='lower right')  # 图例

plt.subplot(212)
plt.plot(t[:len * 4], DTMFsin[:len * 4], c='purple')  # 波形合成之后的图
plt.grid()
plt.show()
