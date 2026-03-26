import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

'''打开文件（后续默认这是一个双声道的声音）'''
f = wave.open(r'../data/xiaomifeng.wav', 'rb')
'''参数读取：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩方法名称)'''
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate  # 计算音频持续时间 单位：秒
print(channel, sampwidth, samplerate, frames, duration)
'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
'''将格式转为ndarray，np.int16是根据sampwidth=2（两字节）确定的'''
data = np.frombuffer(audio, dtype=np.int16)
print(len(data),data.dtype)
'''
如果播放时有明显噪音，可以先进行归一化处理
data = data / np.max(np.abs(data))
'''
print("播放立体声")
# sd.play(data, samplerate, blocking=True, mapping=None)  # 播放 ,mapping = None参数可以省略

'''绘波形图，
对于小蜜蜂这个例子无意义，因为全是由等强度的单频信号构成的，
对于单/多声道的录音信号，可以看出波形变化
'''
data = data / np.max(np.abs(data))
t = np.arange(0, duration, 1 / samplerate)
plt.plot(t, data)
plt.show()

'''时频图（原理参见第四章“绘制时频图部分”）'''
plt.ylim(0, 2000)
plt.specgram(data, Fs=samplerate)
plt.show()
