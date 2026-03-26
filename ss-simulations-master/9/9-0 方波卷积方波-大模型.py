import matplotlib.pyplot as plt
import numpy as np


def plot_subplot(position, x, y, title, xlabel, xlim, color):
    plt.subplot(3, 2, position)
    plt.plot(x, y, color=color)
    plt.title(title, loc='left', fontsize=title_fontsize)
    plt.xlabel(xlabel, loc='right', fontsize=xlabel_fontsize)
    plt.xticks(fontsize=xticks_fontsize)
    plt.grid(True)
    plt.xlim(xlim)
    plt.gca().set_yticklabels([])


# 自定义参数
sampling_density = 1000
square_wave_width = 2
figure_width = 16
figure_height = 9
title_fontsize = 14
xlabel_fontsize = 14
xticks_fontsize = 12
t_min = -10
t_max = 10

# 设置字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'

# 定义时间轴
t = np.linspace(t_min, t_max, sampling_density)

# 定义方波
square_wave1 = np.piecewise(t, [t < 0, t >= 0, t >= square_wave_width], [0, 1, 0])
square_wave2 = np.piecewise(t, [t < 0, t >= 0, t >= square_wave_width], [0, 1, 0])

# 计算卷积
dt = t[1] - t[0]
convolution = np.convolve(square_wave1, square_wave2, 'same') * dt

# 计算FFT
freqs = np.fft.fftfreq(len(t), dt)
freqs = np.fft.fftshift(freqs)
fft_square_wave1 = np.fft.fftshift(np.fft.fft(square_wave1))
fft_square_wave2 = np.fft.fftshift(np.fft.fft(square_wave2))
fft_convolution = np.fft.fftshift(np.fft.fft(convolution))

# 绘制图形
plt.figure(figsize=(figure_width, figure_height))

plot_subplot(1, t, square_wave1, r'$e(t)$', r'$\mathit{time(s)}$', (-2, 8), 'red')
plot_subplot(2, freqs, np.abs(fft_square_wave1), r'$F[e(t)]$', r'$\mathit{frequency(Hz)}$', (-5, 5), 'red')
plot_subplot(3, t, square_wave2, r'$h(t)$', r'$\mathit{time(s)}$', (-2, 8), 'blue')
plot_subplot(4, freqs, np.abs(fft_square_wave2), r'$F[h(t)]$', r'$\mathit{frequency(Hz)}$', (-5, 5), 'blue')
plot_subplot(5, t, convolution, r'$e(t) \ast h(t)$', r'$\mathit{time(s)}$', (-2, 8), 'darkviolet')
plot_subplot(6, freqs, np.abs(fft_convolution), r'$F[e(t) \ast h(t)]$', r'$\mathit{frequency(Hz)}$', (-5, 5),
             'darkviolet')

# 显示图形
plt.tight_layout()
plt.show()
