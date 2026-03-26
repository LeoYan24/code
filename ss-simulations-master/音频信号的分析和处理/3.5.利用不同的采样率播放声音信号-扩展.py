import wave

import numpy as np
import sounddevice as sd

# 打开文件
f = wave.open('../data/sound1.wav', 'rb') #单声道
'''
# 参数读取方式1：一次性返回所有参数(元组),
(声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩方法名称)
_wave_params(nchannels=2, sampwidth=2, framerate=4800, nframes=57871, 
comptype='NONE', compname='not compressed')
常见参数读取前四个即可
'''
params = f.getparams()
channel, sampwidth, fs, frames = params[:4]
duration = frames / fs  # 计算音频持续时间 单位：秒
print(channel, sampwidth, fs, frames, duration)

'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
f.close()
data = np.frombuffer(audio, dtype=np.int16)
data = data / np.max(np.abs(data))
# 播放
sd.play(data, fs, blocking=True)  # 播放

'''
测试1
把采样率加倍，会使得每秒播放更多的样本，相当于将信号压缩得到f(2t)再播放，音调为快放效果
把采样率减半，会使得每秒播放更少的样本，相当于将信号扩展得到f(1/2t)再播放，音调为慢放效果
'''
data1= np.hstack([data,np.zeros(int(fs*0.4), dtype=np.int16)])#补零的目的是防止播放声音不全
sd.play(data1, fs * 2, blocking=True) #高频且短促
sd.play(data, fs * 0.5, blocking=True) #低频且更长


'''
测试2
如果尝尝试利用interp插值方法增加信号的密度，再进行利用更大的采样率进行播放，音调不会发生变化
如果利用原采样率呢？
'''
t1 = np.arange(0, duration, 1 / fs)
t2 = np.arange(0, duration, 1 / fs / 2)
data2 = np.interp(t2, t1, data)
data2 = data2 / np.max(np.abs(data2)) #归一化，否可会有噪音
sd.play(data2, fs*2, blocking=True)  # 插值后的信号，以二倍速播放，时长1秒

'''
测试3
如果尝尝试利用删减信号的样本点，
进行利用更小的采样率进行播放，音调不会发生变化
如果利用原采样率呢？
'''
data3 = data[::2]
sd.play(data3, fs/2, blocking=True)

import librosa
'''
扩展知识
使用librosa库
做进一步处理,拉长或缩短声音（time_stretch），通过rate参数调整比例
'''
data_h = librosa.effects.time_stretch(data, rate=0.5)
# sd.play(data_h, fs * 2 , blocking=True)
data_l = librosa.effects.time_stretch(data, rate=2.0)
# sd.play(data_l, fs * 0.5, blocking=True)
print("处理后的样本点数量对比",len(data),len(data_h), len(data_l))  # 323840 80960
# 通过加点或减点的方式，使得在原采样率播放时产生高音或低音
# data_h 减点，产生高音
data_h = data_h[::2]
# data_l 插值，产生低音
n1 = np.arange(0, len(data_l), 1)
n2 = np.arange(0, len(data_l), 1 / 2)
data_l = np.interp(n2, n1, data_l)
# sd.play(data_l, fs, blocking=True)
print(len(data_h), len(data_l))  # 161920 161920
# 播放立体声
data_mix = np.append([data_h], [data_l], axis=0).T
# sd.play(data_mix, fs, blocking=True, mapping=None)
# 播放混合声音（调高音调和调低音调的混合，有点恐怖片的效果）
data_mix = (0.7 * data_l + 0.3 * data_h)
sd.play(data_mix, fs, blocking=True)  # 播放

'''扩展介绍：
使用librosa做直接改变音调
之前的例子，如果改变音调，则音频的长度会发生变化，
使用librosa库，可以做到声音长度不变，但音调会发生变化（pitch_shift）
通过n_steps参数可以调整音调高低
'''
data_h = librosa.effects.pitch_shift(data, sr = fs,n_steps=10)
sd.play(data_h, fs, blocking=True)
data_l = librosa.effects.pitch_shift(data, sr = fs,n_steps=-10)
sd.play(data_l, fs, blocking=True)
