
import control as ct
import matplotlib.pylab as plt

B = [1, 0.5, 0, 0]
A = [1, -1.25, 0.75, -0.125]

dsys = ct.TransferFunction(B, A, dt=1)
zp = ct.pzmap(dsys, plot=True, grid=True, marker_size=10)
plt.show()

print(zp)  # 显示零极点结果
