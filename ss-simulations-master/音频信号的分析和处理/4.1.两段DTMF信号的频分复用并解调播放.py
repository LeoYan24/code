import wave
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft


# 函数：读取单声道音频
def getVoice(name):
    f = wave.open(name, 'rb')
    params = f.getparams()
    channel, sampwidth, fs, frames = params[:4]
    audio = f.readframes(frames)  # 格式为<class 'bytes'>
    f.close()
    data = np.frombuffer(audio, dtype=np.int16)
    data = data / np.max(np.abs(data))
    return data, fs


'''（1）读取两路信号，进行预处理，定义两路载波'''
sig1, fs = getVoice(r'..\..\data\voice_1.wav')
sig2, fs = getVoice(r'..\..\data\voice_2.wav')
'''（2）把两路信号的长度补齐成相同的，方便后续的运算'''
length = max(len(sig1), len(sig2))
sig1 = np.pad(sig1, (0, length - len(sig1)), 'constant')
sig2 = np.pad(sig2, (0, length - len(sig2)), 'constant')
'''
（3）用更高的采样频率进行进行重采样
音频信号的采样频率一般为8000Hz到480000Hz,但载波用了100,000Hz和200,000Hz的频率,
为了构建高频率载波信号，需要更高的采样频率，否则不满足奈奎斯特抽样率，也不能使得载波信号平滑，因此：
1，根据fc1和fc2定义新的采用频率和采样间隔
2，根据新的采样频率和采样间隔，对原信号进行重采样
'''
fc1 = 1e4  # 第一路调制载波频率（Hz）
fc2 = 2e4  # 第一路调制载波频率（Hz）
sample_freq = fc2 * 10  # 新采样频率，不能过高，否则无法播放
sample_interval = 1 / sample_freq  # 采样间隔
time = length / fs
t = np.arange(0, time, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))
'''利用线性插值方式进行重采样'''
from scipy.interpolate import interp1d

t1 = np.arange(0, time, 1 / fs)  # 原来的时间轴，对应原始音频的采样频率
f_sig1 = interp1d(t1, sig1, kind='linear', fill_value="extrapolate")
sig1 = f_sig1(t)
f_sig2 = interp1d(t1, sig2, kind='linear', fill_value="extrapolate")
sig2 = f_sig2(t)
'''（4）定义载波'''
carrier1 = np.cos(2 * np.pi * fc1 * t)
carrier2 = np.cos(2 * np.pi * fc2 * t)
'''（5）分别调制两路信号，并得到各自的频谱'''
mod_sig1 = sig1 * carrier1
sig1_fft_amp = fftshift(np.abs(fft(sig1)) * sample_interval)  # 原信号频谱
carrier1_fft_amp = fftshift(np.abs(fft(carrier1)) * sample_interval)  # 载波信号频谱
mod_sig1_fft_amp = fftshift(np.abs(fft(mod_sig1)) * sample_interval)  # 调制信号频谱

mod_sig2 = sig2 * carrier2
sig2_fft_amp = fftshift(np.abs(fft(sig2)) * sample_interval)  # 原信号频谱
carrier2_fft_amp = fftshift(np.abs(fft(carrier2)) * sample_interval)  # 载波信号频谱
mod_sig2_fft_amp = fftshift(np.abs(fft(mod_sig2)) * sample_interval)  # 调制信号频谱
'''（6）混合并传输信号，并得到混合信号的频谱'''
mix_sig = mod_sig1 + mod_sig2  # 两路调制信号混叠
mix_sig_fft = fftshift(fft(mix_sig)) * sample_interval  # 双边幅度谱,范围为正负sample_freq/2
mix_sig_fft_amp = np.abs(mix_sig_fft)
'''（7）定义带通滤波器，在频域定义理想带通1,以fc1/fc2为中心，带宽为fs,也就是两倍的信号带宽'''
BPF1 = np.heaviside(f + (fc1 + fs / 2), 1) - np.heaviside(f + (fc1 - fs / 2), 1) + \
       np.heaviside(f - (fc1 - fs / 2), 1) - np.heaviside(f - (fc1 + fs / 2), 1)

BPF2 = np.heaviside(f + (fc2 + fs / 2), 1) - np.heaviside(f + (fc2 - fs / 2), 1) + \
       np.heaviside(f - (fc2 - fs / 2), 1) - np.heaviside(f - (fc2 + fs / 2), 1)
'''(8)混合信号过带通分离信号，# 频域相乘，得到分离后信号的频域形式'''
BPF_sig1_fft = mix_sig_fft * BPF1
BPF_sig1_fft_amp = np.abs(BPF_sig1_fft)
BPF_sig1 = (ifft(ifftshift(BPF_sig1_fft / sample_interval)))

BPF_sig2_fft = mix_sig_fft * BPF2
BPF_sig2_fft_amp = np.abs(BPF_sig2_fft)
BPF_sig2 = (ifft(ifftshift(BPF_sig2_fft / sample_interval)))
'''(9)在频域定义一个低通，并进行滤波'''
LPF_HW = 2 * np.heaviside(f + fs / 2.2, 1) - 2 * np.heaviside(f - fs / 2.2, 1)
'''（10）反变换得到分离之后的时域形式，并在时域进行解调计算'''
demod_sig1_fft = fft(BPF_sig1 * carrier1)
rt1 = ifft(demod_sig1_fft * ifftshift(LPF_HW)).real

demod_sig2_fft = fft(BPF_sig2 * carrier2)
rt2 = ifft(demod_sig2_fft * ifftshift(LPF_HW)).real
'''（11）绘图1：绘制两路信号的分别调制'''
fontsize = 14
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = fontsize - 3  # 字体大小

plt.subplot(321)
plt.grid()
plt.title("第一路信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig1, 'r')

plt.subplot(322)
plt.grid()
plt.title("第二路信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig2, 'b')

plt.subplot(323)
plt.grid()
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title(r"第一路信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, sig1_fft_amp, 'r')

plt.subplot(324)
plt.grid()
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title(r"第二路信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, sig2_fft_amp, 'b')

plt.subplot(325)
plt.grid()  # 显示网格
plt.title("混合信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mix_sig, 'indigo')

plt.subplot(326)
plt.grid()
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title("两路已调信号频谱（叠加）", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mod_sig1_fft_amp, 'r')
plt.plot(f, mod_sig2_fft_amp, 'b')

plt.suptitle("多路复用（1）两路路信号分别调制")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()

'''（12）绘图2：绘制混合信号的分离过程'''
# 第三组图
plt.figure(figsize=(16, 9), dpi=100)
plt.subplot(221)
plt.grid()  # 显示网格
plt.title("混合信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mix_sig, 'indigo')

plt.subplot(222)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 1.5, fc2 * 1.5)
plt.title("混合信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mix_sig_fft_amp, 'indigo')
plt.plot(f, np.max(mix_sig_fft_amp) * BPF1, c='r', ls='--')
plt.plot(f, np.max(mix_sig_fft_amp) * BPF2, c='darkred', ls='--')

plt.subplot(223)
plt.grid()  # 显示网格
plt.title("第一路信号解调还原", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt1, 'r')

plt.subplot(224)
plt.grid()  # 显示网格
plt.title("第二路信号解调还原", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt2, 'b')

plt.suptitle("多路复用（3）混合信号分离与解调")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()

'''（13）播放'''
import sounddevice as sd

sd.play(rt1, sample_freq, blocking=True)  # 第一路信号
sd.play(rt2, sample_freq, blocking=True)  # 第二路信号
