import numpy as np
from lcapy import *
from matplotlib.pyplot import show

'''新建电路'''
cc = Circuit()
cc.add('L1 1 2;right')
cc.add('C1 2 3;right')
cc.add('R1 3 0;down, i={i_{R1}}')
cc.add('W 0_1 0; right')
cc.add('P1 1 0_1; down, v={v_{1}}')
'''绘图'''
cc.draw()
cc.s_model().draw()
show()
'''存自定义格式的网表（和ngspice不通用）
cc.save(r'..\data\circuit.cir')
'''

'''求H，此时电路中有输入,比如V1会引发告警，但能正常输出'''
H = cc.transfer(1, 0, 3, 0) / str(cc.R1.impedance)
print("H(s)= ", H)

'''加入实际输入进行仿真'''
cc1 = cc.subs({'L1': 1, 'C1': 1, 'R1': 0})
cc1.add('W 3 0; down')
cc2 = cc.subs({'L1': 1, 'C1': 1, 'R1': 0.5})
cc3 = cc.subs({'L1': 1, 'C1': 1, 'R1': 3})

H1 = cc1.transfer('P1', (1, 2)) / str(cc2.L1.impedance)
print("H1(s)= ", H1)
H2 = cc2.transfer('P1', (3, 0)) / str(cc2.R1.impedance)
print("H2(s)= ", H2)
H3 = cc3.transfer('P1', (3, 0)) / str(cc3.R1.impedance)
print("H3(s)= ", H3)

'''画出传输函数的零极点图'''
H2.plot()
show()
'''频响特性
freq = np.linspace(0, 100, 10000)
H2(f).abs.plot(freq, log_scale=True)
H2(f).dB.plot(freq, log_scale=True)
H2(f).phase.plot(freq, log_scale=True)
show()
'''
'''波特图'''
freq = np.logspace(-2, 2, 10000)
H2.bode_plot(freq)
show()

'''计算时域响应'''
# cc.remove('P1') #删除端口是为了绘图美观，实际可以不删
cc1.add('V1 1 0_1 step 1 ;down')
cc2.add('V1 1 0_1 step 1 ;down')
cc3.add('V1 1 0_1 step 1 ;down')
cc1.L1.i.plot((0, 20))
cc2.L1.i.plot((0, 20))
cc3.L1.i.plot((0, 20))
show()
