import wave
import sounddevice as sd
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft

''' 读取wave '''
# 读取一个单声道的音频
f = wave.open("../data/voice.wav", 'r')
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate
y = np.frombuffer(f.readframes(frames), dtype=np.int16)
sd.play(y / np.max(np.abs(y)), samplerate, blocking=True)
'''倒置信号、播放声音'''
Fw = fftshift(fft(y))
Fw_conj = np.conj(Fw) # 求y的频谱的共轭
y_neg = ifft(fftshift(Fw_conj)).real
y_neg = y_neg / np.max(np.abs(y_neg))
sd.play(y_neg, samplerate, blocking=True)

'''绘图'''
#绘图轴
t = np.arange(0, frames) / samplerate
f = fftshift(fftfreq(frames, 1 / samplerate))

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 4))  # 新建绘图，设置绘图区域的宽高
plt.subplot(231)
plt.grid()
plt.title("原信号")
plt.plot(t, y)

plt.subplot(232)
plt.grid()
plt.title('原信号幅度谱')
plt.plot(f, np.abs(Fw) / samplerate)
plt.xlim(-10000, 10000)

plt.subplot(233)
plt.grid()
plt.title('原信号相位谱')
plt.plot(f, np.unwrap(np.angle(Fw)))
plt.xlim(-10000, 10000)

plt.subplot(234)
plt.grid()
plt.title("倒置信号")
plt.plot(t, y_neg)

plt.subplot(235)
plt.grid()
plt.title('倒置信号幅度谱')
plt.plot(f, np.abs(Fw_conj) / Fs)
plt.xlim(-10000, 10000)

plt.subplot(236)
plt.grid()
plt.title('倒置信号相位谱')
plt.plot(f, np.unwrap(np.angle(Fw_conj)))
plt.xlim(-10000, 10000)

plt.tight_layout()
plt.show()

