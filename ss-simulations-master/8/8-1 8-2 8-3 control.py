import control as ct

'''
control中，没有xxx2zpk方法，因此需要采用另外方法获得零极点，且不太方便获得增益k
此外control中没有直接的eig或eigvals方法求特征根
'''

'''例8-1'''
A = [[0, 1 / 2, -1 / 2], [-1, -1, 0], [1, 0, -1]]  # 3*3矩阵
B = [[0], [1], [0]]  # 三行一列
C = [0, 0, 1]  # 三列一行
D = [0]

sys = ct.StateSpace(A, B, C, D)
print(sys)
print("-------------------------------")
'''如果系统的离散的'''
sys = ct.StateSpace(A, B, C, D, dt=True)
print(sys)

print("-------------------------------")
'''例8-2'''
num = [1, 0]
den = [1, 3, 2]
sys = ct.TransferFunction(num, den)
print(sys.zeros(), sys.poles(), sys.dcgain())
ss1 = ct.tf2ss(num, den)

print(ss1.A, ss1.B, ss1.C, ss1.D)
print("-------------------------------")
'''例8-3'''
A = [[-3, -2], [1, 0]]
B = [[1], [0]]
C = [1, 0]
D = [0]
sys = ct.StateSpace(A, B, C, D)
tf1 = ct.ss2tf(sys)
print(tf1.num, tf1.den)
print(sys.zeros(), sys.poles(), sys.dcgain())
