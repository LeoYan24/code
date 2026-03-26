from scipy import signal  # 导入scipy.signal

'''例8-1'''
A = [[0, 1 / 2, -1 / 2], [-1, -1, 0], [1, 0, -1]]  # 3*3矩阵
B = [[0], [1], [0]]  # 三行一列
C = [0, 0, 1]  # 三列一行
D = [0]

sys = signal.StateSpace(A, B, C, D)
print(sys)
print("-------------------------------")
'''如果系统的离散的'''
sys = signal.StateSpace(A, B, C, D, dt=True)
print(sys)

print("-------------------------------")
'''例8-2'''
num = [1, 0]
den = [1, 3, 2]
r, p, k = signal.tf2zpk(num, den)
A, B, C, D = signal.tf2ss(num, den)
print(r, p, k)
print(A, B, C, D)
print("-------------------------------")
'''例8-3'''
A = [[-3, -2], [1, 0]]
B = [[1], [0]]
C = [1, 0]
D = [0]
num, den = signal.ss2tf(A, B, C, D)
r, p, k = signal.ss2zpk(A, B, C, D)
print(num, den)
print(r, p, k)
print("-------------------------------")
from scipy import linalg

la = linalg.eigvals(A)
print(la)
