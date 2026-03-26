import matplotlib.pylab as plt  # 绘制图形
import numpy as np

t = np.arange(0, 50.0, 0.01)
y = np.exp(1j * np.pi / 8 * t)
'''获得复信号的实部虚部、模值相位'''
y_real = y.real
y_imag = y.imag
y_mag = np.abs(y)
y_ang = np.angle(y)
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
plt.subplot(221)
plt.grid()
plt.title("复函数-实部", loc='left')
plt.plot(t, y_real)

plt.subplot(222)
plt.grid()
plt.title("复函数-虚部", loc='left')
plt.plot(t, y_imag)

plt.subplot(223)
plt.grid()
plt.title("复函数-模值", loc='left')
plt.plot(t, y_mag)

plt.subplot(224)
plt.grid()
plt.title("复函数-相位", loc='left')
plt.plot(t, y_ang)

plt.tight_layout()
plt.show()
'''解卷绕相位'''
y_unwrap_ang = np.unwrap(y_ang)
'''绘图'''
plt.figure(figsize=(6, 3))  # 新建绘图，设置绘图区域的宽高
plt.subplot(121)
plt.grid()
plt.title("不解卷绕相位", loc='left')
plt.plot(t, y_ang)
plt.subplot(122)
plt.grid()
plt.title("解卷绕相位", loc='left')
plt.plot(t, y_unwrap_ang)

plt.tight_layout()
plt.show()
