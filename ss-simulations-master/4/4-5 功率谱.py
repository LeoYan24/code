import matplotlib.pylab as plt
import numpy as np
from scipy import integrate

T = 2
w1 = 2 * np.pi / T
t = np.arange(-3 * T, 3 * T, 0.01)
# n = np.arange(-10, 11) #使用较少的谐波
n = np.arange(-100, 101)  # 使用较多的谐波
harms = []  # 记录各次谐波的谱系数（复数）
harms_power = []  # 记录功率谱
for i in n:  # 实际谐波范围为-n到n
    basefunc_real = lambda x: np.exp(-1j * i * w1 * x).real
    fn_real_1 = integrate.quad(basefunc_real, -T/4, T / 4)[0] / T # -T/4到T/4部分
    fn_real_2 = -1 * integrate.quad(basefunc_real, T / 4, 3 * T / 4)[0] / T  #T/4到3T/4部分
    fn_real = fn_real_1 + fn_real_2

    basefunc_imag = lambda x: np.exp(-1j * i * w1 * x).imag
    fn_imag_1 = integrate.quad(basefunc_imag, -T / 4, T / 4)[0] / T
    fn_imag_2 =  -1 * integrate.quad(basefunc_imag, T / 4, 3 * T / 4)[0] / T
    fn_imag = fn_imag_1 + fn_imag_2

    fn = fn_real + 1j * fn_imag
    harms.append(abs(fn)) #幅度谱
    harms_power.append(abs(fn * np.conj(fn))) # 功率谱

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.grid()
plt.title("幅度谱", loc='left')
plt.stem(n, harms)

plt.subplot(2, 1, 2)
plt.grid()
plt.title("功率谱", loc='left')
plt.stem(n, harms_power)

plt.tight_layout()
plt.show()

'''计算x(t)的功率'''
func = lambda x: np.cos(w1 * x) ** 2
print(integrate.quad(func, 0, T)[0] / T)
'''计算y(t)基波功率'''
print(harms_power[9] + harms_power[11])

'''分析功率谱的叠加情况'''
right_harms_power = np.array(harms_power[int(len(n)/2):]) * 2  # 根据功率谱的对称性，取半边谱线,并且数值乘以2
right_harms_power[0] = right_harms_power[0] / 2  #
print(right_harms_power[0])  # F0的功率谱线不需要乘以2，因此进行了修正
right_harms_power_sum = np.cumsum(right_harms_power)
plt.stem(np.arange(0, len(right_harms_power_sum)),right_harms_power_sum )
plt.show()
print(right_harms_power_sum[-1]) #100个谐波的功率累加