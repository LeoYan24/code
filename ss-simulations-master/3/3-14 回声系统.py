import wave
import matplotlib.pylab as plt
import numpy as np
import sounddevice as sd
''' 读取wave '''
f = wave.open(r'../data/voice.wav', 'rb') #
nchannels, sampwidth, fs, nframes = f.getparams()[:4]
y = np.frombuffer(f.readframes(nframes), dtype=np.int16)
f.close()
sd.play(y, fs, blocking=True)
t = np.arange(0, nframes) / fs  #原时间轴
h = np.hstack([1, np.zeros(int(fs * 0.25)), 0.5])
y_echo = np.convolve(y, h)  #离散卷积（默认full模式）
''' 为响应信号y_echo构造新的时间轴(画图)，卷积之后信号时间会变长'''
t_echo = np.arange(0, len(y_echo)) / fs
sd.play(y_echo.astype(np.int16), fs, blocking=True)  # 播放

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(211)
plt.plot(t, y)
plt.title('原声音信号')
plt.subplot(212)
plt.title('带有回声的信号')
plt.plot(t_echo, y_echo)
plt.tight_layout()
plt.show()
