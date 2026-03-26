import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置（非衬线）中文字体为宋体
plt.rcParams['font.size'] = 12  # 设置字体大小
plt.rcParams['axes.unicode_minus'] = False

f = wave.open(r'py\pySShomework\20250929_164950.wav', 'rb')
params = f.getparams()
channel, sampwidth, samplerate, frames = params[:4]
duration = frames / samplerate 
print(f"声道数: {channel}, 采样宽度: {sampwidth}, 采样率: {samplerate}, 总帧数: {frames}, 时长: {duration:.2f}秒")

# 读取音频数据
audio = f.readframes(frames)  
data = np.frombuffer(audio, dtype=np.int16)
print(f"原始数据长度: {len(data)}, 数据类型: {data.dtype}")

# 重塑数据为 (帧数, 声道数)
if channel == 2:
    data = data.reshape(-1, 2)
    left_channel = data[:, 0]
    right_channel = data[:, 1]
    
    # 方法1：简单平均（最常用的方法，避免削波）
    data_mono = (left_channel + right_channel) / 2
    
    # 方法2：直接相加（可能导致削波）
    # data_mono = left_channel + right_channel
    
    # 方法3：取最大值（保留最响的部分）
    # data_mono = np.maximum(np.abs(left_channel), np.abs(right_channel)) * np.sign(left_channel)
    
    # 方法4：取均方根（RMS，更符合人耳感知）
    # data_mono = np.sqrt((left_channel**2 + right_channel**2) / 2)
    
    print(f"合并后数据长度: {len(data_mono)}")
else:
    data_mono = data

# 归一化
data_mono = data_mono / np.max(np.abs(data_mono))

# 正确的时间数组
t = np.arange(0, len(data_mono)) / samplerate

print(f"时间数组形状: {t.shape}, 数据数组形状: {data_mono.shape}")

# 播放合并后的单声道音频
# sd.play(data_mono, samplerate, blocking=True)

# 绘制混合声道的波形图
plt.figure(figsize=(14, 6))
plt.plot(t, data_mono, linewidth=0.5, alpha=0.8)
plt.xlabel('时间 (秒)', fontsize=12)
plt.ylabel('归一化幅度', fontsize=12)
plt.title('混合声道波形图 (左右声道平均)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xlim(0, duration)

# 添加一些统计信息
plt.text(0.02, 0.95, f'采样率: {samplerate} Hz\n时长: {duration:.2f} 秒\n声道: 混合单声道', 
         transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
         verticalalignment='top')

plt.tight_layout()
plt.show()

# 绘制频谱图
plt.figure(figsize=(14, 6))
plt.specgram(data_mono, Fs=samplerate, scale='dB', cmap='viridis')
plt.xlabel('时间 (秒)', fontsize=12)
plt.ylabel('频率 (Hz)', fontsize=12)
plt.title('混合声道频谱图', fontsize=14)
plt.colorbar(label='强度 (dB)')
plt.ylim(0, 2000)
plt.tight_layout()
plt.show()

f.close()

# 可选：比较原始声道和混合声道
if channel == 2:
    plt.figure(figsize=(14, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, left_channel / np.max(np.abs(left_channel)), linewidth=0.5, alpha=0.8, label='左声道')
    plt.ylabel('幅度')
    plt.title('左声道')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(t, right_channel / np.max(np.abs(right_channel)), linewidth=0.5, alpha=0.8, color='orange', label='右声道')
    plt.ylabel('幅度')
    plt.title('右声道')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 3)
    plt.plot(t, data_mono, linewidth=0.5, alpha=0.8, color='green', label='混合声道')
    plt.xlabel('时间 (秒)')
    plt.ylabel('幅度')
    plt.title('混合声道 (左右声道平均)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()