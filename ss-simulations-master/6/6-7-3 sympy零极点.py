import sympy as sy
from sympy.physics.control import TransferFunction, pole_zero_plot

s = sy.symbols('s')
tf1 = TransferFunction(s - 1, s ** 2 + 3 * s + 2, s)
print(tf1.poles(), tf1.zeros())
zs = pole_zero_plot(tf1)

'''
https://docs.sympy.org/latest/modules/physics/control/control_plots.html
'''
