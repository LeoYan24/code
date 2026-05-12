import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

celsius = [-50, 27, 75]
kelvin = [T + 273.15 for T in celsius]

# 玻尔兹曼常数 (eV/K)
kB = 8.617333262145e-5

E = np.linspace(-0.5, 0.5, 1000)
Ef = 0.0

plt.figure(figsize=(8, 5))
for T, T_C in zip(kelvin, celsius):
    f = 1.0 / (np.exp((E - Ef) / (kB * T)) + 1.0)
    plt.plot(E, f, linewidth=2, label=f'{T_C} °C')

plt.xlabel('$E − E_f$ (eV)')
plt.ylabel('f(E)')
plt.title('费米-狄拉克分布函数')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()