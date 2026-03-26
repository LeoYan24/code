import numpy as np
import sounddevice as sd
fs = 8192  # 采样率
# 定义音阶的频率
f1 = 262  # C大调1的频率Hz；
f2 = 262 * np.power(2, 2 / 12)  # 即1的频率再乘以2的（2/12）次方
f3 = 262 * np.power(2, 4 / 12)
f4 = 262 * np.power(2, 5 / 12)
f5 = 262 * np.power(2, 7 / 12)
f6 = 262 * np.power(2, 9 / 12)
f7 = 262 * np.power(2, 11 / 12)
fh1 = 262 * np.power(2, 12 / 12)
# 定义音符时长
# 二分音符
l2 = np.arange(fs * 2)
x_1 = np.sin((2 * np.pi * f1 / fs) * l2)
x_2 = np.sin((2 * np.pi * f2 / fs) * l2)
x_3 = np.sin((2 * np.pi * f3 / fs) * l2)
x_4 = np.sin((2 * np.pi * f4 / fs) * l2)
x_5 = np.sin((2 * np.pi * f5 / fs) * l2)
# 四分音符
l4 = np.arange(fs * 1)
x1 = np.sin((2 * np.pi * f1 / fs) * l4)
x2 = np.sin((2 * np.pi * f2 / fs) * l4)
x3 = np.sin((2 * np.pi * f3 / fs) * l4)
x4 = np.sin((2 * np.pi * f4 / fs) * l4)
x5 = np.sin((2 * np.pi * f5 / fs) * l4)
# 八分音符
l8 = np.arange(fs * 0.5)
xh1 = np.sin((2 * np.pi * f1 / fs) * l8)
xh2 = np.sin((2 * np.pi * f2 / fs) * l8)
xh3 = np.sin((2 * np.pi * f3 / fs) * l8)
xh4 = np.sin((2 * np.pi * f4 / fs) * l8)
xh5 = np.sin((2 * np.pi * f5 / fs) * l8)
# 合并乐谱，因为比较长，按小节合并，再总体合并
notes1 = np.hstack([xh5, xh3, x3, xh4, xh2, x2, xh1, xh2, xh3, xh4, xh5, xh5, x5])
notes2 = np.hstack([xh5, xh3, x3, xh4, xh2, x2, xh1, xh3, xh5, xh5, x_3])
notes3 = np.hstack([xh2, xh2, xh2, xh2, xh2, xh3, x4, xh3, xh3, xh3, xh3, xh3, xh4, x5])
notes4 = np.hstack([xh5, xh3, x3, xh4, xh2, x2, xh1, xh3, xh5, xh5, x_1])
notes = np.hstack([notes1, notes2, notes3, notes4])  # 最终乐谱
sd.play(notes, fs, blocking=True)  # 播放

'''存储为wav文件
参数：
1，文件名
2. 输入信号（notes）
'''
import wave
filename = r'../data/xiaomifeng.wav' #存储名字
notes_scaled = notes / np.max(np.abs(notes)) #输入信号为notes，此处归一化处理，防止播放时出现噪音
notes_int16 = np.int16(notes_scaled * 32767)
f = wave.open(filename, 'w')
f.setnchannels(1)  # 单声道
f.setsampwidth(2)  # 16位
f.setframerate(fs)
f.writeframes(notes_int16.tobytes())
f.close()
