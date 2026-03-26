import control as ct
import control.matlab as ma
import matplotlib.pylab as plt  # 绘制图形

b = [1, -1]
a = [1, 3, 2]

sys = ct.TransferFunction(b, a)

'''方式1，使用control的原生函数绘图，
pzmap方法产生FutureWarning，
未来使用pzmap得到p, z有一定风险'''
p, z = ct.pzmap(sys, plot=True)
plt.show()
print("1", p, z)
'''打印零极点结果'''
p = ct.poles(sys)
z = ct.zeros(sys)
print("2", p, z)

'''方式2，使用matlab模块'''
p, z = ma.pzmap(sys, plot=True)
plt.show()
print("3", p, z)
'''打印零极点结果'''
p = ma.poles(sys)
z = ma.zeros(sys)
print("4", p, z)

'''方式3，使用matlab模块,直接转换得到zpk'''
z, p, k = ma.tf2zpk(b, a)
print("5", p, z, k)

'''扩展：绘制波特图的两种方式'''
# 使用matlab模块
mag, phase, omega = ma.bode(sys, dB=True, Hz=True, grid=True)
plt.show()  # 如果不加show()，则只会返回结果，不会出图
# 使用control库本身
ct.bode_plot(sys)
plt.show()  #
