import wave
import matplotlib.pylab as plt
import numpy as np
import sounddevice as sd
from numpy.fft import fftfreq, fftshift, fft

'''打开文件（后续默认这是一个单声道的声音）'''
f = wave.open(r'../data/voice.wav', 'rb')
'''参数读取：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩方法名称)'''
params = f.getparams()
channel, sampwidth, fs, frames = params[:4]
duration = frames / fs  # 计算音频持续时间 单位：秒
print(channel, sampwidth, fs, frames, duration)
audio = f.readframes(frames)  # 格式为<class 'bytes'>
y = np.frombuffer(audio, dtype=np.int16)
'''播放'''
sd.play(y, fs , blocking=True) # 正常采样率，正常放
sd.play(y, fs / 2, blocking=True) #采样率降低，慢放
sd.play(y, 2 * fs, blocking=True) #采样率提高，快放
'''分析三种情况下的频谱'''
Fw = fftshift(fft(y)) / fs
t = np.arange(0, frames) / fs
f1 = fftshift(fftfreq(frames, 1 / fs))#正常放
f2 = fftshift(fftfreq(frames, 2 / fs))#慢放
f3 = fftshift(fftfreq(frames, 1 / fs /2))#快放

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(311)
plt.grid()  
plt.title("正常播放时，信号呈现的频谱")
plt.plot(f1, np.abs(Fw) / fs)
plt.xlim(-fs/4, fs/4)  #需要根据信号的实际情况调整

plt.subplot(312)
plt.grid()  
plt.title('降低播放采样率时，信号呈现的频谱')
plt.plot(f2, np.abs(Fw) / fs)
plt.xlim(-fs/4, fs/4) #需要根据信号的实际情况调整

plt.subplot(313)
plt.grid()  
plt.title('提高播放采样率时，信号呈现的频谱')
plt.plot(f3, np.abs(Fw) / fs)
plt.xlim(-fs/4, fs/4) #需要根据信号的实际情况调整

plt.tight_layout()
plt.show()


