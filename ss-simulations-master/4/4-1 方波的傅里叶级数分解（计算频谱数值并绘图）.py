import matplotlib.pylab as plt
import numpy as np
from scipy import integrate, signal

T = 2
w = 2 * np.pi / T  # 基波角频率
tao = 0.8  # 脉冲宽度
duty = tao / T  # 占空比
Ts = 0.01
t = np.arange(0, 5 * T, Ts)
# 方波
sig = 0.5 * signal.square(w * (t + tao / 2), duty=duty) + 0.5  # 周期方波，duty为占空比

def harmonic(i):
    if i ==0: #直流
        return tao / T,0
    an_quad = lambda x: np.cos(i * w * x)
    an = integrate.quad(an_quad, 0, tao / 2)
    an = 4 * an[0] / T
    bn = 0  #偶函数

    cn = an
    if an > 0:
        angle = 0
    else:
        angle = -np.pi

    print(n, cn, angle)
    return cn, angle


'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

n = 0
cn, angle = harmonic(n)
plt.subplot(3, 2, 1)
plt.grid()
plt.title("直流分量", loc='left')
plt.plot(t, sig, "r--")
plt.plot()
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况

n = 1
cn, angle = harmonic(n)
plt.subplot(3, 2, 2)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况

n = 2
cn, angle = harmonic(n)
plt.subplot(3, 2, 3)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况

n = 3
cn, angle = harmonic(n)
plt.subplot(3, 2, 4)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况

n = 4
cn, angle = harmonic(n)
plt.subplot(3, 2, 5)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况

n = 5
cn, angle = harmonic(n)
plt.subplot(3, 2, 6)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))  # 谐波叠加情况
'''表达式验证
ff = lambda x:  np.cos(w * x) if np.cos(w * x) >= 0 else  0
ff = np.array([ff(x) for x in t])
plt.plot(t,ff)
'''

plt.tight_layout()
plt.show()


'''
0.6054613829125256
-0.18709785675772778
-0.12473190450515192
0.1513653457281314
4.677806199023251e-17
'''