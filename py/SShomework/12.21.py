import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile
import scipy.signal as sig

# 1. 读取音频信号
file_path = r'd:\code\ss-simulations-master\data\voice_1.wav'
fs, signal = wavfile.read(file_path)

# 如果是立体声（双声道），只取其中一个声道
if signal.ndim > 1:
    signal = signal[:, 0]

# 归一化信号 (如果读取的是整数类型)
if signal.dtype != np.float32 and signal.dtype != np.float64:
    signal = signal.astype(np.float32) / np.max(np.abs(signal))

duration = len(signal) / fs
t = np.arange(0, duration, 1/fs)  # 时间向量

# 2. 画出波形图和频谱图
plt.figure(figsize=(10, 8))

# 子图1：波形图
plt.subplot(2, 1, 1)
# 为了看清波形，只画前 0.02 秒的数据
plot_duration = 0.02
if duration < plot_duration:
    plot_duration = duration
num_samples_to_plot = int(plot_duration * fs)

plt.plot(t[:num_samples_to_plot], signal[:num_samples_to_plot])
plt.title(f'Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# 子图2：频谱图
plt.subplot(2, 1, 2)
N = len(signal)
fft_y = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/fs)

# 取正频率部分
half_N = N // 2
freqs_half = freqs[:half_N]
fft_y_half = np.abs(fft_y[:half_N]) / N * 2  # 幅度归一化

plt.plot(freqs_half, fft_y_half)
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()

# 4. 数字滤波器设计与分析
# 设计一个4阶巴特沃斯低通滤波器
print("\n--- Digital Filter Analysis ---")
order = 4
nyquist = 0.5 * fs
# 截止频率必须严格小于奈奎斯特频率。
# 这里设置为 2000 Hz (对于 8000 Hz 采样率，Nyquist 是 4000 Hz)
cutoff_freq = 2000 
if cutoff_freq >= nyquist:
    cutoff_freq = 0.9 * nyquist # 如果采样率过低，自动调整截止频率

print(f"Sampling Rate: {fs} Hz, Nyquist: {nyquist} Hz, Cutoff Frequency: {cutoff_freq} Hz")

normal_cutoff = cutoff_freq / nyquist
b, a = sig.butter(order, normal_cutoff, btype='low', analog=False)

# (1) 单位样值响应
impulse = np.zeros(60)
impulse[0] = 1
h_n = sig.lfilter(b, a, impulse)

# (2) 单位阶跃响应
step = np.ones(60)
s_n = sig.lfilter(b, a, step)

# (3) 幅频特性和相频特性
w, h = sig.freqz(b, a, worN=8000)
freqs_resp = w * fs / (2 * np.pi)
amplitude_resp = np.abs(h)
phase_resp = np.angle(h)

# (4) 零极点图
z, p, k = sig.tf2zpk(b, a)

# 绘制滤波器特性图
plt.figure(figsize=(12, 10))

# 单位样值响应
plt.subplot(3, 2, 1)
plt.stem(h_n)
plt.title('Impulse Response')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# 单位阶跃响应
plt.subplot(3, 2, 2)
plt.stem(s_n)
plt.title('Step Response')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# 幅频特性
plt.subplot(3, 2, 3)
plt.plot(freqs_resp, 20 * np.log10(amplitude_resp + 1e-12))
plt.title('Magnitude Response (dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# 相频特性
plt.subplot(3, 2, 4)
plt.plot(freqs_resp, np.unwrap(phase_resp))
plt.title('Phase Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.grid(True)

# 零极点图
plt.subplot(3, 2, 5)
# 画单位圆
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k--', linewidth=1)
plt.plot(np.real(z), np.imag(z), 'bo', label='Zeros')
plt.plot(np.real(p), np.imag(p), 'rx', label='Poles')
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axis('equal')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 5. 信号通过滤波器
print("\n--- Filtering Signal ---")
filtered_signal = sig.lfilter(b, a, signal)

# 绘制滤波后的信号波形和频谱
plt.figure(figsize=(10, 8))

# 子图1：滤波后波形图
plt.subplot(2, 1, 1)
plt.plot(t[:num_samples_to_plot], filtered_signal[:num_samples_to_plot])
plt.title(f'Filtered Waveform - First {plot_duration}s')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# 子图2：滤波后频谱图
plt.subplot(2, 1, 2)
fft_y_filtered = np.fft.fft(filtered_signal)
fft_y_filtered_half = np.abs(fft_y_filtered[:half_N]) / N * 2

plt.plot(freqs_half, fft_y_filtered_half)
plt.title('Filtered Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# 3. 播放声音 (播放滤波后的声音)
print(f"Playing Filtered Audio ({duration:.2f} seconds)...")
sd.play(filtered_signal, fs, blocking=True)
print("Done.")

