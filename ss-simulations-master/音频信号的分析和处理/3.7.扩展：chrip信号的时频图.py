import matplotlib.pylab as plt  # 绘制图形
import numpy as np
import sounddevice as sd
from scipy import signal

sample_freq = 8192
sample_interval = 1 / sample_freq  # 模拟连续信号的采样间隔
t = np.arange(0, 10, sample_interval)
fstart = 100
fend = 4000
'''
生成chirp信号
参数t1是上升到f1的时间，信号频率会一直上升或一直下降，如果上升，信号会频率到达sample_freq的一半（即信号满足奈奎斯特抽样定理）即“折返”
此外，信号频率到达t1之后，是否继续上升，取决于sample_freq，
也就是说如果sample_freq非常大，则信号会一直上升，如果sample_freq较小，则可能在剩余时间段内下降
后面转为.astype(np.float32)是为了存储为wave（原本格式是np.float64
method {‘linear’, ‘quadratic’平方, ‘logarithmic’, ‘hyperbolic’双曲线}，应该是频率上升的取值方式
'''
c = signal.chirp(t, f0=fstart, f1=fend, t1=5, method='linear').astype(np.float32)
plt.plot(t[:2000], c[:2000])
plt.title("Linear Chirp, f(0)=100, f(5)=4000")
plt.xlabel('t (sec)')
plt.show()
# 短时傅立叶变换频谱图（伪彩图）
plt.specgram(c, Fs=sample_freq)
plt.show()
'''播放'''
sd.play(c, sample_freq, blocking=True)

'''如果需要存储
#以写方式打开一个新文件
wave_out = wave.open("crisp.wav", 'wb')
#以下参数必须指定
wave_out.setnchannels(1)#单声道
wave_out.setsampwidth(4)#位深度<class 'numpy.float32'>
wave_out.setframerate(sample_freq)#采样率
wave_out.writeframes(c)#写入数据
wave_out.close()
'''
