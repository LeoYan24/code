import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal, integrate

# todo 可以调节周期和占空比
# 定义半波余弦，方法为余弦乘以同周期方波
T = 2
w = 2 * np.pi / T  # 基波角频率
tao = 1  # 脉冲宽度
duty = tao / T  # 占空比，调节tao可以获得三角波或锯齿波
Ts = 0.01
t = np.arange(0, 5 * T, Ts)
# todo 调节谐波标号和包络线用的频轴
n = np.arange(-20, 21)  # 谐波标号，同时也是频轴
n_dense = np.arange(-20, 21, 0.01)  # 为了画出连续的包络线用的频轴

# 三角波和锯齿波
sig = signal.sawtooth(w * t, width=duty)

# 记录各次谐波的叠加情况
f = np.zeros_like(t)
harms = []  # 记录各次谐波
'''
for循环通过数值积分计算各次谐波（fn）的实部和虚部，并进行叠加（n=0、±1、2、3、4……）
'''
for i in n:
    # todo 构建fn的积分表达式
    '''
    因为quad方法不支持复函数积分，
    需要手动拆出fn的实部.real和虚部.imag
    '''
    # 实部
    f_inside_real = lambda x: np.real(
        ((2 / tao * x - 1) if (x < tao) else
        (1 - 2 / (T - tao) * (x - tao))) * np.exp(
            -1j * i * w * x))
    fn_real = integrate.quad(f_inside_real, 0, T )
    fn_real = fn_real[0] / T #完整级数公式（取实部）
    # 虚部
    f_inside_imag = lambda x: np.imag(
        ((2 / tao * x - 1) if (x < tao) else
        (1 - 2 / (T - tao) * (x - tao))) * np.exp(
            -1j * i * w * x))
    fn_imag = integrate.quad(f_inside_imag, 0, T)
    fn_imag = fn_imag[0] / T #完整级数公式（取虚部）
    # 叠加得到真实的fn，注意虚部要乘以1j
    fn = fn_real + 1j * fn_imag
    # 把谐波模值记录到数组，后续进行画图
    harms.append(np.abs(fn))
    # 构造完整的谐波：fn*基底函数
    f_harmonic = fn * np.exp(1j * i * w * t)
    f = f + f_harmonic #叠加
# 画幅度频谱图，利用numpy+matplotlib

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.grid()  # 显示网格
plt.title(r"谐波叠加", loc='left')
plt.plot(t, f.real)             # 谐波叠加情况,加入.real是为了避免出现warning，原理上可以不加，不影响结果
#todo 画出包络线
#plt.plot(t, sig, 'r--')  # 原信号
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.subplot(2, 1, 2)
plt.grid()  # 显示网格
plt.title("幅度谱", loc='left')
plt.stem(n, harms)
# todo 画出幅度谱的包络线

plt.xlabel(r"$n\omega_1$", loc='right')
plt.xlim(-5, 5)

plt.tight_layout()
plt.show()
