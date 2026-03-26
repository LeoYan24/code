import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from numpy.fft import fftshift, fft, ifftshift, ifft

# 参数
fs = 8000  # 采样率
length = 1  # 时长s
freq = 1000  # Hz

t = np.arange(0, length, 1 / fs)  # 定义t，长度为1秒
data = np.cos(2 * np.pi * freq * t)  # 生成正弦波
sd.play(data, fs, blocking=True)  # 播放

# 傅里叶变换
Fw1 = fftshift(fft(data))
'''
(本例在信号与系统阶段不太好解释)
在Fw的两侧补零，使得Fw的点数变多，但中心内容没有变化，相当于采样数量翻倍，采样间隔减小
此时如果使用两倍的fs进行播放和绘图，声音的时长、频率和波形不会发生变化
'''
Fw2 = np.hstack([np.zeros(int(len(t) / 2)), Fw1, np.zeros(int(len(t) / 2))])
# 反变换
data2 = ifft(ifftshift(Fw2))

sd.play(np.real(data2), fs * 2, blocking=True)  # 播放

print(len(Fw1), len(Fw2))
print(len(data), len(data2))

plt.figure()
plt.subplot(211)  # 画布位置1
plt.grid()  # 网格
plt.plot(np.arange(100), data[:100])  # 折线图
plt.subplot(212)  # 画布位置2
plt.grid()  # 网格
plt.plot(np.arange(200), np.real(data2)[:200])  # 折线图
plt.show()
