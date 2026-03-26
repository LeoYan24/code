import numpy as np
import sounddevice as sd

fs = 8000
dt = 1 / fs  # 采样间隔
# 定义模拟信号
t = np.arange(0, 1, dt)
f1 = 262  # C大调1的频率Hz；
x1 = np.sin(2 * np.pi * f1 * t)
# 播放
sd.play(x1, fs, blocking=True)  # 播放x1
# 定义离散信号
n = np.arange(0, fs)
f1 = 262  # C大调1的频率Hz；
x2 = np.sin(2 * np.pi * f1 * dt * n)
# 播放
sd.play(x2, fs, blocking=True)  # 播放x2
