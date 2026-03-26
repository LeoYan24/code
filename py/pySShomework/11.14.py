import wave
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, fftshift

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

def load_audio(file_path):
    """加载音频文件并返回数据"""
    f = wave.open(file_path, 'rb')
    n_channels, sampwidth, samplerate, n_frames = f.getparams()[:4]
    audio_data = f.readframes(n_frames)
    f.close()
    
    # 转换为numpy数组
    y = np.frombuffer(audio_data, dtype=np.int16)
    
    # 如果是立体声，取左声道
    if n_channels == 2:
        y = y[0::2]
    
    return y, samplerate, n_frames

# 加载两段音频
bass_signal, bass_rate, bass_frames = load_audio(r'D:\code\py\pySShomework\diyin.wav')
treble_signal, treble_rate, treble_frames = load_audio(r'D:\code\py\pySShomework\gaoyin.wav')

# 归一化
bass_norm = bass_signal / np.max(np.abs(bass_signal))
treble_norm = treble_signal / np.max(np.abs(treble_signal))

# 计算时间轴
bass_time = np.arange(len(bass_signal)) / bass_rate
treble_time = np.arange(len(treble_signal)) / treble_rate

# 计算频谱
bass_freq = fftshift(fftfreq(len(bass_signal), 1/bass_rate))
bass_spec = fftshift(fft(bass_signal)) / len(bass_signal)
treble_freq = fftshift(fftfreq(len(treble_signal), 1/treble_rate))
treble_spec = fftshift(fft(treble_signal)) / len(treble_signal)

# 绘制波形图和频谱图
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 低音频波形图
axes[0,0].plot(bass_time, bass_norm, linewidth=0.5)
axes[0,0].set_title('低音频 - 波形图')
axes[0,0].set_xlabel('时间 (秒)')
axes[0,0].grid(True, alpha=0.3)

# 低音频频谱图
axes[0,1].plot(bass_freq, np.abs(bass_spec), linewidth=0.5)
axes[0,1].set_title('低音频 - 频谱图')
axes[0,1].set_xlabel('频率 (Hz)')
axes[0,1].set_xlim(0, 2000)
axes[0,1].grid(True, alpha=0.3)

# 高音频波形图
axes[1,0].plot(treble_time, treble_norm, linewidth=0.5)
axes[1,0].set_title('高音频 - 波形图')
axes[1,0].set_xlabel('时间 (秒)')
axes[1,0].grid(True, alpha=0.3)

# 高音频频谱图
axes[1,1].plot(treble_freq, np.abs(treble_spec), linewidth=0.5)
axes[1,1].set_title('高音频 - 频谱图')
axes[1,1].set_xlabel('频率 (Hz)')
axes[1,1].set_xlim(0, 8000)
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 绘制伪彩图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# 低音频伪彩图
im1 = ax1.specgram(bass_signal, Fs=bass_rate, NFFT=1024, noverlap=512, cmap='viridis')
ax1.set_title('低音频 - 伪彩图')
ax1.set_xlabel('时间 (秒)')
ax1.set_ylabel('频率 (Hz)')
ax1.set_ylim(0, 2000)

# 高音频伪彩图
im2 = ax2.specgram(treble_signal, Fs=treble_rate, NFFT=1024, noverlap=512, cmap='viridis')
ax2.set_title('高音频 - 伪彩图')
ax2.set_xlabel('时间 (秒)')
ax2.set_ylabel('频率 (Hz)')
ax2.set_ylim(0, 8000)

plt.tight_layout()
plt.show()

# 打印音频信息
print(f"低音频: 采样率 {bass_rate}Hz, 持续时间 {bass_time[-1]:.2f}秒")
print(f"高音频: 采样率 {treble_rate}Hz, 持续时间 {treble_time[-1]:.2f}秒")