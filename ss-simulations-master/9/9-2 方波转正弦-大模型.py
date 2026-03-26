import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, square

# 参数设置
fs = 4000  # 采样频率 (Hz)
f0 = 50    # 方波频率 (Hz)
duration = 2  # 信号持续时间 (秒)，确保至少有100个周期
order = 4  # 滤波器阶数
cutoff = 100  # 截止频率 (Hz)

# 生成时间向量
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# 生成50Hz的方波信号
square_wave = square(2 * np.pi * f0 * t)

# 设计四阶巴特沃兹低通滤波器
b, a = butter(order, cutoff / (0.5 * fs), btype='low', analog=False)

# 应用滤波器
filtered_signal = lfilter(b, a, square_wave)

# 取前200个采样点
square_wave_200 = square_wave[:200]
filtered_signal_200 = filtered_signal[:200]

# 绘制波形图
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t[:200], square_wave_200)
plt.title('50Hz Square Wave (First 200 Samples)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t[:200], filtered_signal_200)
plt.title('Filtered Signal (First 200 Samples)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# 计算滤波器的频率响应
w, h = freqz(b, a, worN=int(fs / 2))

# 将频率转换为Hz
frequencies = (w / np.pi) * (fs / 2)

# 绘制幅频特性
plt.figure(figsize=(12, 6))

plt.subplot(1, 1, 1)
plt.semilogx(frequencies, 20 * np.log10(abs(h)))
plt.title('Amplitude Response of the Butterworth Lowpass Filter')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.xlim(0, 1000)  # 设置横坐标范围为0到1000Hz
plt.ylim(-10, 1)   # 设置纵坐标范围为-10到1dB
plt.grid(True)
plt.axvline(cutoff, color='red', linestyle='--', label=f'Cutoff Frequency ({cutoff} Hz)')
plt.legend()

plt.tight_layout()
plt.show()

# 计算一个周期的样本数
samples_per_period = int(fs / f0)

# 提取方波的100个周期
square_wave_100_periods = square_wave[:samples_per_period * 100]

# 提取滤波后信号的100个周期
filtered_signal_100_periods = filtered_signal[:samples_per_period * 100]

# 计算方波在100个周期内的平均功率
rms_square_wave_100_periods = np.sqrt(np.mean(square_wave_100_periods**2))
power_square_wave_100_periods = rms_square_wave_100_periods**2

# 计算滤波后信号在100个周期内的平均功率
rms_filtered_signal_100_periods = np.sqrt(np.mean(filtered_signal_100_periods**2))
power_filtered_signal_100_periods = rms_filtered_signal_100_periods**2

# 计算转换效率
conversion_efficiency = power_filtered_signal_100_periods / power_square_wave_100_periods

print(f"方波在100个周期内的平均功率: {power_square_wave_100_periods:.4f}")
print(f"滤波后信号在100个周期内的平均功率: {power_filtered_signal_100_periods:.4f}")
print(f"转换效率: {conversion_efficiency:.4f} (或 {conversion_efficiency*100:.2f}%)")


'''

写一段代码，利用numpy和scipy实现，使用scipy.signal的square函数生成一个周期为50Hz的方波，
使其通过一个四阶巴特沃兹低通滤波器，该滤波器的截止频率为80Hz。将信号的采样频率设置为4000。
对方波和生成信号的前200个采样点绘制波形图。

在上面代码的基础上，绘制所定义四阶巴特沃兹低通滤波器的波特图，只画幅频特性，纵坐标为分贝值，坐标范围为-10到1，
横坐标采用log坐标，坐标范围为0到1000Hz。

在上面代码的基础上，首先计算周期方波的平均功率，再计算输出信号的平均功率，
再以比值的方式给出转换效率。

'''