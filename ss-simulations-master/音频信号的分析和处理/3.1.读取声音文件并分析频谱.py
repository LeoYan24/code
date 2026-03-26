import wave
import numpy as np
import sounddevice as sd
from numpy.fft import fftfreq, fftshift, fft, ifft, ifftshift
import matplotlib.pylab as plt

# 打开文件，读取一个单频率音频文件
f = wave.open(r'../data/voice.wav', 'rb')
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate  # 计算音频持续时间 单位：秒

'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
y = np.frombuffer(audio, dtype=np.int16)  # 所有数据读到1D array，顺序是左右声道交替读取
#sd.play(y, samplerate, blocking=True)

Fw = fftshift(fft(y)) / samplerate  #fft正变换
y2 = ifft(ifftshift(Fw * samplerate)).real #ifft逆变换
y2 = y2 / np.max(np.abs(y2)) #归一化
sd.play(y2, samplerate, blocking=True)
#绘图轴
t = np.arange(0, frames) / samplerate
f = fftshift(fftfreq(frames, 1 / samplerate))

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(121)
plt.grid()
plt.title("原信号")
plt.plot(t, y)

plt.subplot(122)
plt.grid()
plt.title('原信号幅度谱')
plt.plot(f, np.abs(Fw) / samplerate)
plt.xlim(-samplerate/2, samplerate/2)  #需要根据信号的实际情况调整

plt.tight_layout()
plt.show()


