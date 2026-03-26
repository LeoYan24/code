import matplotlib.pylab as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifft, ifftshift

''' ----------------------
注意：
fc是低通的截止频率
1/2fc是低通h(t)的（Sa函数）第一过零点
因此，广泛使用fc和1/fc作为参数，以方便修改fc时，仍能具有较合理的图形
比如将t和sample_freq与fc关联起来，这样t和f的采样点数量总是固定的，计算开销也比较固定
然后在绘图时，xlim根据fc限制显示范围，这样在大多数情况下，修改fc后的显示效果能够有保障
----------------------'''
t0 = 0.05  # 0.05 定义时延量
fc = 1000  # 截止频率单位是Hz
fs = 100 * fc
Ts = 1 / fs
''' ----------------------
第一部分：两种理想低通的定义方式
----------------------'''
'''定义t、f'''
t = np.arange(-100 / fc, 100 / fc, Ts)
# print(len(t)) # always 20000
f = fftshift(fftfreq(len(t), Ts))
# ------------------
'''1,从时域定义理想低通
注意对照公式乘系数，使得频域门高度为1，方便图形展示
'''
ht1 = 2 * fc * np.sinc(2 * fc * (t - t0))
'''求fft，得到正确幅度'''
Hw1 = fftshift(fft(fftshift(ht1))) * Ts
Hw1_amp = np.abs(Hw1)

'''2,从频域定义理想低通，这里直接使用f，确保和之前时域定义的数据范围一致'''
Hw2_amp = np.heaviside(f + fc, 1) - np.heaviside(f - fc, 1)

Hw2 = Hw2_amp * np.exp(t0 * -1j * f * 2 * np.pi)
'''求ifft，得到应ht，
1. Hw2或Hw2_amp相当于进行过幅度修正和fftshift，因此要反向操作一下
2. 由于时域的t是个对称区间，因此要对ifft结果再进行一次ifftshift
3. 考虑到ifft的精度问题，可能得到的ht2不是纯实的，其结果可以取个实部
'''
ht2 = ifftshift(ifft(ifftshift(Hw2 / Ts))).real

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(221)
plt.grid()
plt.xlim(-2 / fc + t0, 2 / fc + t0)
plt.title(r"在时域定义$h_1 (t)$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ht1)
# 双边谱
plt.subplot(222)
plt.grid()
plt.xlim(- 2 * fc, 2 * fc)
plt.title(r"通过$FFT$计算$|H_1 (2\pi f)|$", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Hw1_amp)

plt.subplot(223)
plt.grid()
plt.xlim(-2 / fc + t0, 2 / fc + t0)
plt.title(r"通过$IFFT$计算$h_2 (t)$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ht2, 'r')

plt.subplot(224)
plt.grid()
plt.xlim(- 2 * fc, 2 * fc)
plt.title("在频域定义$H_2 (2\pi f)$（门函数）", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Hw2_amp, 'r')

plt.tight_layout()  
plt.show()

''' ----------------------
第二部分：低通的运算效果
----------------------'''
'''周期信号'''
w1 = 2 * np.pi * fc * 0.5
w2 = 2 * np.pi * fc * 4
et = np.cos(w1 * t) + 0.2 * np.cos(w2 * t)

'''信号频谱'''
Ew = fftshift(fft(fftshift(et))) * Ts
Ew_amp = np.abs(Ew)

'''利用频域乘积方式查看低通滤波效果，对应频域定义方式'''
Ew = fftshift(fft(fftshift(et))) * Ts
Ew_amp = np.abs(Ew)
Rw = Ew * Hw2
Rw_amp = np.abs(Rw)
rt = ifftshift(ifft(ifftshift(Rw / Ts))).real

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()
plt.xlim(-5 / fc, 5 / fc)
plt.title(r"$e(t)$", loc='left')
plt.xlabel(r'$\rm{(s)}$', loc='right')
plt.plot(t, et)

plt.subplot(222)
plt.grid()
plt.xlim(- 5 * fc, 5 * fc)
plt.title(r"$|E(2\pi f)|$  $(f_c=%d \rm{Hz})$" % fc, loc='left')
plt.xlabel(r'$\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(Hw2) * np.max(Ew_amp), "r--")  # 标示一下低通的位置,修正高度使得图像更易读
plt.plot(f, Ew_amp)

plt.subplot(223)
plt.grid()
plt.xlim(-5 / fc + t0, 5 / fc + t0)
plt.title(r"$IFFT[R_2(2\pi f)]$", loc='left')
plt.xlabel(r'$\rm{(s)}$', loc='right')
plt.plot(t, rt, 'g')

plt.subplot(224)
plt.grid()
plt.xlim(- 5 * fc, 5 * fc)
plt.title(r"$|R_2(2\pi f)|$", loc='left')
plt.xlabel(r'$\rm{(Hz)}$', loc='right')
plt.plot(f, Rw_amp, 'g')

plt.tight_layout()  
plt.show()

''' ----------------------
第二部分：低通的运算效果(绘图参数略有不同)
----------------------'''
'''阶跃信号'''
tao = 10 / fc
# 定义一个方波信号,高度可变，Ew最大值为1
et = 1 / tao * (np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1))

'''信号频谱'''
Ew = fftshift(fft(fftshift(et))) * Ts
Ew_amp = np.abs(Ew)

'''利用频域乘积方式查看低通滤波效果，对应频域定义方式'''
Ew = fftshift(fft(fftshift(et))) * Ts
Ew_amp = np.abs(Ew)
Rw = Ew * Hw2  # 注意考虑幅度修正问题，根据前文代码，Rw1相当于经过了幅度修正
Rw_amp = np.abs(Rw)
rt = ifftshift(ifft(ifftshift(Rw / Ts))).real

'''研究响应信号的上升沿'''
rt_half = rt[int(t0 * fs):int(len(rt) / 2 + t0 * fs)]
min_position = np.argwhere(rt_half == np.min(rt_half)).flatten()[0]  # 找到最小值的位置
max_position = np.argwhere(rt_half == np.max(rt_half)).flatten()[0]  # 找到最大值的位置
print("最小值的位置:", min_position)
print("最大值的位置:", max_position)
print("上升沿时长:", t[min_position] - t[max_position])

'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()
plt.xlim(-10 / fc, 10 / fc)
plt.title(r"$e(t)$", loc='left')
plt.xlabel(r'$\rm{(s)}$', loc='right')
plt.plot(t, et)
# 双边谱
plt.subplot(222)
plt.grid()
plt.xlim(- 2 * fc, 2 * fc)
plt.title(r"$|E(2\pi f)|$  $(f_c=%d \rm{Hz})$" % fc, loc='left')
plt.xlabel(r'$\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(Hw2) * np.max(Ew_amp), "r--")  # 标示一下低通的位置,修正高度使得图像更易读
plt.plot(f, Ew_amp)

plt.subplot(223)
plt.grid()
plt.xlim(-10 / fc + t0, 10 / fc + t0)
plt.title(r"$IFFT[R_2(2\pi f)]$", loc='left')
plt.xlabel(r'$\rm{(s)}$', loc='right')
plt.plot(t, rt, 'g')

plt.subplot(224)
plt.grid()
plt.xlim(- 2 * fc, 2 * fc)
plt.title(r"$|R_2(2\pi f)|$", loc='left')
plt.xlabel(r'$\rm{(Hz)}$', loc='right')
plt.plot(f, Rw_amp, 'g')

plt.tight_layout()  
plt.show()
