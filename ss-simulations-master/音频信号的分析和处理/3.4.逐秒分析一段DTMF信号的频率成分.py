import wave

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from numpy.fft import fftfreq, fftshift, fft

f = wave.open('../data/dtmf1.wav', 'rb')
# 一次性返回所有格式信息，元组：(声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型)
params = f.getparams()
'''
# 参数读取方式1：一次性返回所有参数(元组),
(声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩方法名称)
_wave_params(nchannels=2, sampwidth=2, framerate=4800, nframes=57871, 
comptype='NONE', compname='not compressed')
常见参数读取前四个即可
'''
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate  # 计算音频持续时间 单位：秒
print(channel, sampwidth, samplerate, frames, duration)

'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
# 将格式转为ndarray
# 由于是双声道数据，因此进行一下拆分，np.int16是根据sampwidth=2（两字节）来确定的
data = np.frombuffer(audio, dtype=np.int16)  # 所有数据读到1D array，顺序是左右声道交替读取
data.shape = frames, channel  # 如果已知声道，也可以写为-1, 2，表示格式改为：无论有多少行，每行两列数据
dataT = data.T  # 转置，变为两行数据，一个声道一行

'''可以尝试三种方式分析数据：1，两个声道混合，2：分别用左右声道'''
# 对两个声道求平均值
# dataT_mix = (dataT[0] / 2 + dataT[1] / 2).astype(np.int16)
# dataT_mix = dataT[0]
dataT_mix = dataT[1]  # 针对示例音频效果好一些
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

''' 
定义一个1秒的时间轴，数据点个数为 framerate
实际取的数据为每秒的第t_slice之后的数据，比如这里是[0.6,1)的数据
'''
t_slice = 0.6
t1 = np.arange(samplerate * (1 - t_slice))#注意实际样本点数量
# 频轴
f = fftshift(fftfreq(len(t1), 1 / samplerate))
# 截取第n秒的数据
for i in range(6):
    data_slice = dataT_mix[int(samplerate * (i + t_slice)):int(samplerate * (i + 1))]
    sd.play(data_slice, samplerate, blocking=True)  # 播放
    # 频谱
    Fw_amp = np.abs(fftshift(fft(data_slice) / samplerate))

    plt.subplot(3, 2, i + 1)
    plt.xlim(-1700, 1700)
    plt.xticks([-1477, -1336, -770, -697, 0, 697, 770, 1209, 1336, 1477], [])
    plt.plot(f, Fw_amp, c='purple')  # 波形合成之后的图
    plt.title("第%d秒" % (i + 1))
    plt.grid()  # 网格

plt.tight_layout()
plt.show()

# 参考数据
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
