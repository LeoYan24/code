import wave
import sounddevice as sd
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft

''' 读取wave '''
f = wave.open("../data/voice.wav", 'r')# 读取一个单声道的音频
nchannels, sampwidth, Fs, nframes = f.getparams()[:4]
t = np.arange(0, nframes) / Fs
y = np.frombuffer(f.readframes(nframes), dtype=np.int16)
sd.play(y / np.max(np.abs(y)), Fs, blocking=True)

'''利用幅度和相位恢复信号'''
Fw = fftshift(fft(y))
# 利用幅度构造y_2
y_2 = np.real(ifft(ifftshift(np.abs(Fw))))
sd.play(y_2 / np.max(np.abs(y_2)), Fs, blocking=True)
# 利用相位构造y_3
y_3 = np.real(ifft(ifftshift(np.exp(-1j * np.angle(Fw)))))
sd.play(y_3, Fs, blocking=True)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(211)
plt.grid()  
plt.title("幅度信息重建")
plt.plot(t, y_2)
plt.ylim(-5000, 5000)

plt.subplot(212)
plt.grid()  
plt.title("相位信息重建")
plt.plot(t, y_3)

plt.tight_layout()
plt.show()
