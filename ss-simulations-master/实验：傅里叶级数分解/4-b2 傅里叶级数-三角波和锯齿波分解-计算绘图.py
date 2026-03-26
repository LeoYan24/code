import matplotlib.pylab as plt
import numpy as np
from scipy import integrate, signal

#todo 调整tao等参数
T = 2
w = 2 * np.pi / T  # 基波角频率
tao = 0.5  # 脉冲宽度
duty = tao / T  # 占空比，调节tao可以获得三角波或锯齿波
Ts = 0.01
t = np.arange(0, 5 * T, Ts)
#三角波和锯齿波
sig = signal.sawtooth(w * t,width=duty)


def harmonic(i):
    # todo 构建an、bn的积分表达式
    '''
    函数通过数值积分计算各次谐波的幅度和相位，思路是分别计算an和bn，再组合为cn和phi(n)
    锯齿波的表达式在0到tao之间为 (2 / tao * x - 1)，在tao到T之间为(1 - 2 / (T-tao) * (x-tao))
    此外注意a0的公式和an不同，差2倍。
    '''
    an_quad = lambda x: ((2 / tao * x - 1) if x < tao else (1 - 2 / (T - tao) * (x - tao)) if x < T else 0) * np.cos(i * w * x)
    an = integrate.quad(an_quad, 0, T )
    if i ==0: #直流a0
        an = 1 * an[0] / T
    else:
        an = 2 * an[0] / T
    bn_quad = lambda x: ((2 / tao * x - 1) if x < tao else (1 - 2 / (T - tao) * (x - tao)) if x < T else 0) * np.sin( i * w * x)
    bn = integrate.quad(bn_quad, 0,T )
    bn = 2 * bn[0] / T
    cn = np.sqrt(an**2+bn**2)
    if an == 0:
        phi = 0
    else:
        phi = -np.arctan(bn / an)
    #todo 谐波参数读数
    print(n,cn,phi)
    return cn,phi

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
plt.plot(t, cn * np.cos(n * w * t + angle))

n = 1
cn, angle = harmonic(n)
plt.subplot(3, 2, 2)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))

n = 2
cn, angle = harmonic(n)
plt.subplot(3, 2, 3)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))

n = 3
cn, angle = harmonic(n)
plt.subplot(3, 2, 4)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))

n = 4
cn, angle = harmonic(n)
plt.subplot(3, 2, 5)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))

n = 5
cn, angle = harmonic(n)
plt.subplot(3, 2, 6)
plt.grid()
plt.title("%d次谐波" % n, loc='left')
plt.plot(t, sig, "r--")
plt.plot(t, cn * np.cos(n * w * t + angle))
plt.tight_layout()
plt.show()

'''
积分表达式验证
ff = lambda x: (2 / tao * x - 1) if x < tao else  (1 - 2 / (T-tao) * (x-tao)) if x < T else 0
ff = np.array([ff(x) for x in t])
plt.plot(t,ff)
'''
