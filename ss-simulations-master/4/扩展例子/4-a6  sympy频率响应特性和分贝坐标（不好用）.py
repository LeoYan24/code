import matplotlib.pylab as plt  # 绘制图形
from sympy import *

t, f, w = symbols('t f w')
ht, HW = symbols('ht HW', cls=Function)
# --------------------------------------
# 单边指数信号
ht = exp(-1 * t) * Heaviside(t)
# H(w)
HW = 1 / (I * w + 1)
H_Amp = 20 * log(Abs(HW))
H_pha = arg(HW)
# 绘图
# warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块

p1 = plot(ht, (t, -1, 5), title='ht', xlabel='t', line_color='orange', show=False)
# 注意-3dB这条横线，下列函数再一个画布上画了两条线，目前没看到画虚线的方法,linestyle = '--',不管用
# p2 = plot(-3,(w,0,2),color = 'red',show=False)
# p3 = plot(H_Amp,(w,0,2),axis_center = (0,0),title='幅度谱',xlabel='w',show=False)
# 横坐标改为log坐标的写法，但此时w的起始点不能是0，会报错
p3 = plot(H_Amp, (w, 0.01, 10), xscale='log', axis_center=(0.2, 0), title='幅度谱', xlabel='w', show=False)
# p3.extend(p2)
p4 = plot(H_pha, (w, 0.01, 10), xscale='log', axis_center=(0, 0), title='相位谱', xlabel='w', show=False)
# p4.extend(p2)
p = plotting.PlotGrid(3, 1, p1, p3, p4)

'''
1,无法画虚线 3bB点
2，无法画网格
3，sympy函数输出到numpy序列的方法
'''
'''
#绘制幅度频谱图
plt.specgram(h)
plt.grid()
plt.show()
'''
# sympy.integrals.transforms.fourier_transform
