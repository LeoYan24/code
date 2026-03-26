import wave
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
import sounddevice as sd
from scipy import signal

'''读取音频'''
f = wave.open(r'../../data/voice.wav', 'rb')  #
nchannels, sampwidth, fs, nframes = f.getparams()[:4]
print(nchannels, sampwidth, fs, nframes)
y = np.frombuffer(f.readframes(nframes), dtype=np.int16)  # 本
f.close()
sd.play(y, fs, blocking=True)#原始音频
'''由于dlism方法效率较低，因此通过减少样本点和降低采样率的方法减少计算开销
例原信号为32000的采样率，因此进行了降采样，这不是必须的
'''
y = y[::2]
y = y[::2]
fs = int(fs / 4)
'''回声系统'''
h = np.hstack([1, np.zeros(int(fs * 0.25)), 0.5])
B = h
A = np.hstack([1, np.zeros(len(B)-1)])
dsys1 = signal.dlti(B, A, dt=1)
'''回声产生：（1）卷积冲激响应'''
y_echo = np.convolve(y, h)
print(len(y), len(y_echo))
y_echo = y_echo / np.max(np.abs(y_echo))
'''回声产生：（2）output方法
t, y_echo = dsys1.output(y, t=np.arange(len(y)))
y_echo = np.squeeze(y_echo) / np.max(np.abs(y_echo))
'''
'''回声产生：（3）dlsim
t,y_echo = signal.dlsim((B, A,1),y)
y_echo = np.squeeze(y_echo) / np.max(np.abs(y_echo))
'''
'''回声播放'''
sd.play(y_echo, fs, blocking=True)
'''回声消除系统'''
dsys2 = signal.dlti(A, B, dt=1)
'''回声消除：（1）lfilter 只能适配卷积方法'''
y_recovery = signal.lfilter(A, B, y_echo)
y_recovery = y_recovery / np.max(np.abs(y_recovery))
'''回声消除：（2）output方法
t, y_recovery = dsys2.output(y_echo, t=np.arange(len(y_echo)))
y_recovery = y_recovery / np.max(np.abs(y_recovery))'''
'''回声消除：（3）dlsim(略)'''

'''消除后播放'''
sd.play(y_recovery, fs, blocking=True)

'''绘制零极点和频谱特性'''
w = np.linspace(0, 0.01, 10000)
dsys1 = signal.dlti(B, A, dt=1)
w1, Hw1 = dsys1.freqresp(w=w)
dsys2 = signal.dlti(A, B, dt=1)
w2, Hw2 = dsys2.freqresp(w=w)

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
plt.figure()
plt.subplot(211)
plt.grid()
plt.title('回声产生系统-幅频特性', loc='left')
plt.plot(w1, np.abs(Hw1))
plt.xlim(0, 0.01)

plt.subplot(212)
plt.grid()
plt.title('回声消除系统-幅频特性', loc='left')
plt.plot(w2, np.abs(Hw2))
plt.xlim(0, 0.01)

plt.tight_layout()
plt.show()
