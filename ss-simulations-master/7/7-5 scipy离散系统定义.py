from scipy import signal

B = [1, -1, 0]
A = [1, 3, 2]
# 定义方式1
dsys1 = signal.dlti(B, A, dt=True)
# 定义方式2
dsys2 = signal.TransferFunction(B, A, dt=1)
# B/A和zpk转换
z, p, k = signal.tf2zpk(B, A)
print(z, p, k)
# 定义方式3
dsys3 = signal.dlti(z, p, k)
# 定义方式4
dsys4 = signal.ZerosPolesGain(z, p, k, dt=1)
b, a = signal.zpk2tf(z, p, k)
print(b, a)
