import matplotlib.pylab as plt
import numpy as np
from scipy import integrate

T = 2
w1 = 2 * np.pi / T
tao = T * 0.5
t = np.arange(-3 * T, 3 * T, 0.01)  # 谐波累加用的时间轴
n = np.arange(-10, 11)  # 绘制20个谐波
f = np.zeros_like(t)  # 构造空序列，后续进行谐波叠加
harms = []  # 记录各次谐波的谱系数（复数）
for i in n:
    basefunc_real = lambda x: np.exp(-1j * i * w1 * x).real
    fn_real = integrate.quad(basefunc_real, -tao / 2,
                             tao / 2)  # (3.325853178611109e-16, 1.8864874255052047e-14) <class 'tuple'>
    fn_real = fn_real[0] / T

    basefunc_imag = lambda x: np.exp(-1j * i * w1 * x).imag
    fn_imag = integrate.quad(basefunc_imag, -tao / 2, tao / 2)
    fn_imag = fn_imag[0] / T
    fn = fn_real + 1j * fn_imag
    harms.append(abs(fn))  # 把谐波模值记录到数组，后续进行画图
    f = f + fn * np.exp(1j * i * w1 * t)  # 构造完整的谐波：fn*基底函数，并进行叠加

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.grid()
plt.title("幅度谱", loc='left')
plt.stem(n, harms)
# 画出幅度谱的包络线
n_dense = np.arange(-10, 10 + 0.01, 0.01)  # 为了画出连续的包络线用的频轴
plt.plot(n_dense, abs(tao / T * np.sin(n_dense * w1 * tao / 2) / (n_dense * w1 * tao / 2)), 'r--')

plt.subplot(2, 1, 2)
plt.grid()
plt.title(r"谐波叠加", loc='left')
plt.plot(t, np.real(f))  # 谐波叠加情况
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.tight_layout()
plt.show()
