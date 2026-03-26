import matplotlib.pylab as plt  # 绘制图形
from scipy import signal

b = [1, -1]
a = [1, 3, 2]

sys = signal.lti(b, a)
z, p, k = signal.tf2zpk(b, a)
p = sys.poles
z = sys.zeros
print('零点：', z)
print('极点：', p)

'''绘图'''
plt.grid()
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.scatter(p.real, p.imag, marker='x', ls='None', s=100)
plt.scatter(z.real, z.imag, marker='o', ls='None', facecolors='none', s=100, edgecolors='b')
plt.show()

'''系统的另一种表示方法'''
sys = signal.TransferFunction(b, a)
p = sys.poles
z = sys.zeros
print('零点：', z)
print('极点：', p)

'''系统表示方法的转换'''
z, p, k = signal.tf2zpk(b, a)
print(z, p, k)
b, a = signal.zpk2tf(z, p, k)
print(b, a)
