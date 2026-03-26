import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA
import wave
import sounddevice as sd

"""
本例主要演示盲源分离的效果（FastICA），原理请自学。
代码分为两部分：
02，读取01制作的三个混合音频，并进行分离
"""

f1 = wave.open(r'D:\projects\voice_mix0.wav', 'rb')
params = f1.getparams()
channel, sampwidth, samplerate, frames = params[:4]
audio = f1.readframes(frames)  # 格式为<class 'bytes'>
data0 = np.frombuffer(audio, dtype=np.int16)
f1.close()
f1 = wave.open(r'D:\projects\voice_mix1.wav', 'rb')
params = f1.getparams()
channel, sampwidth, samplerate, frames = params[:4]
audio = f1.readframes(frames)  # 格式为<class 'bytes'>
data1 = np.frombuffer(audio, dtype=np.int16)
f1.close()
f1 = wave.open(r'D:\projects\voice_mix2.wav', 'rb')
params = f1.getparams()
channel, sampwidth, samplerate, frames = params[:4]
audio = f1.readframes(frames)  # 格式为<class 'bytes'>
data2 = np.frombuffer(audio, dtype=np.int16)
f1.close()

S = np.c_[data0, data1, data2]
'''注意！A的三个比例要和01中的混合比例一致'''
A = np.array([[1/3, 1/3, 1/3], [0.25, 0.5, 0.25], [0.5, 0.25, 0.25]])
X = np.dot(S, A.T)
data1= data2 / np.max(np.abs(data2))
'''使用FastICA算法分离信号'''
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X) # 重建信号
A_ = ica.mixing_ # 估计的混合矩阵

'''播放'''
sd.play(S_.T[0], 16000, blocking=True)  # 播放

sd.play(S_.T[1], 16000, blocking=True)  # 播放

sd.play(S_.T[2], 16000, blocking=True)  # 播放

exit()
