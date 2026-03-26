import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

'''打开文件（后续默认这是一个双声道的声音）'''
f = wave.open(r'../data/dtmf1.wav', 'rb')
'''参数读取：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩方法名称)'''
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate  # 计算音频持续时间 单位：秒
print(channel, sampwidth, samplerate, frames, duration)
'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
'''将格式转为ndarray，np.int16是根据sampwidth=2（两字节）确定的'''
data = np.frombuffer(audio, dtype=np.int16)
print(len(data), data.dtype)
'''
如果播放时有明显噪音，可以先进行归一化处理
data = data / np.max(np.abs(data))
'''
'''
data原始格式是一个单行，
如果是单声道声音，则后续关于多声道的处理均无效
此时data是一个单行结构，可以直接进行播放或绘图
sd.play(data, samplerate, blocking=True, mapping=None) 
如果data是双声道数据，数据顺序是顺序是左右声道交替读取，需要进行一下拆分
因此赋予一个合适的shape，将其转为两列多行
再转置，形成两行多列
'''
data.shape = frames, channel  # 如果已知声道，也可以写为-1, 2，表示格式改为：无论有多少行，每行两列数据
dataT = data.T  # 转置，变为两行数据，一个声道一行
print(len(data), data.shape)
print(len(dataT), dataT.shape)

'''各种播放方法'''
print("播放一个声道-两个喇叭播放相同声音")
sd.play(dataT[0], samplerate, blocking=True)  # 播放声道1
sd.play(dataT[1], samplerate, blocking=True)  # 播放声道2
print("播放声道1-只有一个喇叭响")
sd.play(dataT[0], samplerate, blocking=True, mapping=1)  # 左边响
sd.play(dataT[1], samplerate, blocking=True, mapping=2)  # 右边响
print("播放立体声")
sd.play(data, samplerate, blocking=True, mapping=None)  # 播放 ,mapping = None参数可以省略
print("两个声道混合成一个声道播放")
dataT_mix = (dataT[0] / 2 + dataT[1] / 2).astype(np.int16)
sd.play(dataT_mix, samplerate, blocking=True)

'''绘波形图'''
dataT_mix = (dataT[0] / 2 + dataT[1] / 2).astype(np.int16)
t = np.arange(0, duration, 1 / samplerate)
plt.plot(t, dataT_mix)
plt.show()

'''时频图（原理参见第四章“绘制时频图部分”）'''
plt.ylim(0, 2000)
plt.specgram(dataT_mix, Fs=samplerate)
plt.show()
