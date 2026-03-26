from lcapy import symbols
from lcapy import UnitImpulse
from lcapy.discretetime import n, z
'''7-2'''
print("7-2")
xn = 0.5 ** n
print(xn.ZT())
xn = UnitImpulse(n - 1)  # 单位样值信号
print(xn.ZT())
print("*"*20)
'''7-3'''
print("7-3")
Xz = z / (z - 0.5)
print(Xz.IZT())
Xz = 1 * z / z
print(Xz.IZT())
print("*"*20)
'''7-4'''
print("7-4")
a, b = symbols('a b')
x = a ** n
Xz = xn.ZT()
print(Xz)
Hz = 1 / (1 - b * z ** (-1))
yn = (Xz * Hz).IZT()
print(yn)
