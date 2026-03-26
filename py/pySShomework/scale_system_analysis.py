import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 采样率
fs = 8192
# 音阶频率（C大调1-7和高音1）
notes_freq = [262, 294, 330, 349, 392, 440, 494, 523]
# 每个音符时长（秒）
duration = 0.5
# 构造音阶信号
scale = np.hstack([
    np.sin(2 * np.pi * f * np.arange(int(fs * duration)) / fs) for f in notes_freq
])
t = np.arange(len(scale)) / fs

# 系统1：RC低通，fc=262Hz
fc1 = 262
w1 = 2 * np.pi * fc1
num1 = [w1]
den1 = [1, w1]
sys1 = (num1, den1)

# 系统2：RC高通，fc=262Hz
fc2 = 262
w2 = 2 * np.pi * fc2
num2 = [1, 0]
den2 = [1, w2]
sys2 = (num2, den2)

# 通过系统1
_, y1, _ = signal.lsim(sys1, U=scale, T=t, X0=[0])
# 通过系统2
_, y2, _ = signal.lsim(sys2, U=scale, T=t, X0=[0])

# 频谱分析
N = len(scale)
N_half = N // 2
f_axis = np.linspace(0, fs/2, N_half)

X = np.fft.fft(scale)
Y1 = np.fft.fft(y1)
Y2 = np.fft.fft(y2)

X_abs = np.abs(X[:N_half])
Y1_abs = np.abs(Y1[:N_half])
Y2_abs = np.abs(Y2[:N_half])

# 绘图参数
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# 原始信号时域
axs[0, 0].plot(t, scale, label='原始音阶信号')
axs[0, 0].set_title('原始音阶信号（时域）')
axs[0, 0].set_xlabel('时间 (s)')
axs[0, 0].set_ylabel('幅值')
axs[0, 0].legend()

# 原始信号频谱
axs[0, 1].plot(f_axis, X_abs, label='原始音阶信号')
axs[0, 1].set_title('原始音阶信号（幅度谱）')
axs[0, 1].set_xlabel('频率 (Hz)')
axs[0, 1].set_ylabel('幅度')
axs[0, 1].legend()

# 系统1输出时域
axs[1, 0].plot(t, y1, color='g', label='系统1输出')
axs[1, 0].set_title('系统1输出（时域）')
axs[1, 0].set_xlabel('时间 (s)')
axs[1, 0].set_ylabel('幅值')
axs[1, 0].legend()

# 系统1输出频谱
axs[1, 1].plot(f_axis, Y1_abs, color='g', label='系统1输出')
axs[1, 1].set_title('系统1输出（幅度谱）')
axs[1, 1].set_xlabel('频率 (Hz)')
axs[1, 1].set_ylabel('幅度')
axs[1, 1].legend()

# 系统2输出时域
axs[2, 0].plot(t, y2, color='r', label='系统2输出')
axs[2, 0].set_title('系统2输出（时域）')
axs[2, 0].set_xlabel('时间 (s)')
axs[2, 0].set_ylabel('幅值')
axs[2, 0].legend()

# 系统2输出频谱
axs[2, 1].plot(f_axis, Y2_abs, color='r', label='系统2输出')
axs[2, 1].set_title('系统2输出（幅度谱）')
axs[2, 1].set_xlabel('频率 (Hz)')
axs[2, 1].set_ylabel('幅度')
axs[2, 1].legend()

plt.tight_layout()
plt.show()
