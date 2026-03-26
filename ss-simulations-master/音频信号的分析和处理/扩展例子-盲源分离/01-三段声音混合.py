import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

"""
本例主要演示盲源分离的效果，原理请自学。
代码分为两部分：
01：将三个声音进行混合，可以自行录三段声音
最好不同音色（不同人），差不多时长，且使用相同的采样率，否则就要自行处理为一致的采样率
"""
f1 = wave.open(r'D:\projects\voice1.wav', 'rb')
params = f1.getparams()
channel, sampwidth, samplerate, frames = params[:4]
print(channel, sampwidth, samplerate, frames)
audio = f1.readframes(frames)  # 格式为<class 'bytes'>
data1 = np.frombuffer(audio, dtype=np.int16)
data1 = data1[::2]#测试使用，采样率相同就不需要这一句
l1 = len(data1)

f2 = wave.open(r'D:\projects\voice2.wav', 'rb')
params = f2.getparams()
channel, sampwidth, samplerate, frames = params[:4]
print(channel, sampwidth, samplerate, frames)
audio = f2.readframes(frames)  # 格式为<class 'bytes'>
data2 = np.frombuffer(audio, dtype=np.int16)
l2 = len(data2)

f3 = wave.open(r'D:\projects\voice3.wav', 'rb')
params = f3.getparams()
channel, sampwidth, samplerate, frames = params[:4]
print(channel, sampwidth, samplerate, frames)
audio = f3.readframes(frames)  # 格式为<class 'bytes'>
data3 = np.frombuffer(audio, dtype=np.int16)
l3 = len(data3)

'''通过补零方式，将三段声音的长度一致'''
m = np.max([l1, l2, l3])
print(l1,l2,l3,m)
data1 = np.hstack([data1, np.zeros(m-l1)])
data2 = np.hstack([data2, np.zeros(m-l2)])
data3 = np.hstack([data3, np.zeros(m-l3)])

'''混合三段声音，分别使用下面三个代码，存储为三个文件，注意混合比例'''
data_mix = (data1/3+data2/3+data3/3)
'''如果播放时有明显噪音，可以先进行归一化处理'''
data_mix = data_mix / np.max(np.abs(data_mix))
sd.play(data_mix, 16000, blocking=True)  # 播放
'''存储为文件'''
import wave
notes_int16 = np.int16(data_mix * 32767)
f = wave.open(r'D:\projects\voice_mix0.wav', 'w')
f.setnchannels(1)  # 单声道
f.setsampwidth(2)  # 16位
f.setframerate(16000)
f.writeframes(notes_int16.tobytes())
f.close()

'''混合三段声音，分别使用下面三个代码，存储为三个文件，注意混合比例'''
data_mix = (data1/4+data2/2+data3/4)
'''如果播放时有明显噪音，可以先进行归一化处理'''
data_mix = data_mix / np.max(np.abs(data_mix))
sd.play(data_mix, 16000, blocking=True)  # 播放
'''存储为文件'''
import wave
notes_int16 = np.int16(data_mix * 32767)
f = wave.open(r'D:\projects\voice_mix1.wav', 'w')
f.setnchannels(1)  # 单声道
f.setsampwidth(2)  # 16位
f.setframerate(16000)
f.writeframes(notes_int16.tobytes())
f.close()

'''混合三段声音，分别使用下面三个代码，存储为三个文件，注意混合比例'''
data_mix = (data1/2+data2/4+data3/4)
'''如果播放时有明显噪音，可以先进行归一化处理'''
data_mix = data_mix / np.max(np.abs(data_mix))
sd.play(data_mix, 16000, blocking=True)  # 播放
'''存储为文件'''
import wave
notes_int16 = np.int16(data_mix * 32767)
f = wave.open(r'D:\projects\voice_mix2.wav', 'w')
f.setnchannels(1)  # 单声道
f.setsampwidth(2)  # 16位
f.setframerate(16000)
f.writeframes(notes_int16.tobytes())
f.close()