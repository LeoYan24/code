import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sympy import symbols, inverse_laplace_transform, exp, cos, sin, simplify

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 画出F(s)的零极点图
def plot_pole_zero():
    # F(s) = (s+2)/(s^2+2s+2)
    # 分子系数 (s+2): [1, 2]
    # 分母系数 (s^2+2s+2): [1, 2, 2]
    
    num = [1, 2]  # s+2
    den = [1, 2, 2]  # s^2+2s+2
    
    # 计算零极点
    zeros = np.roots(num)
    poles = np.roots(den)
    
    print(f"零点: {zeros}")
    print(f"极点: {poles}")
    
    # 绘制零极点图
    plt.figure(figsize=(8, 6))
    
    # 绘制极点 (用'x'表示)
    plt.plot(poles.real, poles.imag, 'rx', markersize=10, label='极点')
    # 绘制零点 (用'o'表示)
    plt.plot(zeros.real, zeros.imag, 'bo', markersize=10, label='零点')
    
    # 添加实轴和虚轴
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('实部')
    plt.ylabel('虚部')
    plt.title('F(s) =(s+2)/(s^2+2s+2)的零极点图')
    plt.axis('equal')
    plt.legend()
    plt.show()

# 2. 求反变换f(t)
def calculate_inverse_laplace():
    t, s = symbols('t s')
    F = (s + 2)/(s**2 + 2*s + 2)
    
    # 计算反变换
    f_t = inverse_laplace_transform(F, s, t)
    f_t_simplified = simplify(f_t)
    
    print(f"拉普拉斯反变换 f(t) = {f_t}")
    print(f"简化形式: f(t) = {f_t_simplified}")
    
    return f_t_simplified

# 3. 绘制f(t)的波形
def plot_time_domain(f_t):
    # 创建时间数组
    t_vals = np.linspace(0, 10, 1000)
    
    # 使用解析表达式直接计算: f(t) = e^(-t)[cos(t) + sin(t)]
    f_numeric = np.exp(-t_vals) * (np.cos(t_vals) + np.sin(t_vals))
    
    # 绘制时域波形
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, f_numeric, 'b-', linewidth=2, label='f(t) = e^(-t)[cos(t) + sin(t)]')
    plt.xlabel('时间 t')
    plt.ylabel('f(t)')
    plt.title('f(t)的时域波形')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    plt.show()

# 主程序
if __name__ == "__main__":
    print("=" * 50)
    print("拉普拉斯变换分析: F(s) = (s+2)/(s²+2s+2)")
    print("=" * 50)
    
    # 1. 绘制零极点图
    print("\n1. 零极点分析:")
    plot_pole_zero()
    
    # 2. 计算反变换
    print("\n2. 拉普拉斯反变换:")
    f_t = calculate_inverse_laplace()
    
    # 3. 绘制时域波形
    print("\n3. 波形:")
    plot_time_domain(f_t)
    
    print("\n分析完成！")