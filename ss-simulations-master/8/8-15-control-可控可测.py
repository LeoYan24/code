import control as ct
import numpy as np

A = np.array([[-1, -2, -1], [0, -3, 0], [0, 0, -2]])
B = np.array([[2], [1], [1]])
C = np.array([1, -1, 0])
D = np.array([0])

sys1 = ct.StateSpace(A, B, C, D)
sys2 = ct.canonical_form(sys1, form='modal')
# sys2 = ct.modal_form(sys1)#方式2
# sys2包含两个输出，sys2[1]是一个坐标变换矩阵T，满足sys2[0] = T * x

print('对角线化的系统状态空间描述：\n', sys2[0])

ct1 = np.linalg.matrix_rank(ct.ctrb(A, B))
ob1 = np.linalg.matrix_rank(ct.obsv(A, C))
print('可控阵的秩：', ct1)
print('可观阵的秩：', ob1)
