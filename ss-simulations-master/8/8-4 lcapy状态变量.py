from lcapy import *

'''新建电路'''
cc = Circuit()
cc.add('L1 1 2;right')
cc.add('C1 2 3;right')
cc.add('R1 3 0;down, i={i_{R1}}')
cc.add('W 0_1 0; right')  # 保持绘图美观
cc.add('V1 1 0_1;down')

'''状态变量'''

# print(cc.ss.y)
# cc.ss.y = cc.ss.y[1]
ot = cc.state_space()

print(ot.state_equations().pretty())
# print(cc.ss.state_equations().pretty())
print(ot.output_equations().pretty())
print(cc.ss.A, cc.ss.B, cc.ss.C, cc.ss.D)
