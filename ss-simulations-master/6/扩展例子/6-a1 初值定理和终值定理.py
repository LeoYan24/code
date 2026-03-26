from sympy import symbols, limit, oo,inverse_laplace_transform,pretty
s,t = symbols('s t')  # 定义符号变量
# 假设X_s是给定的s域表达式
Ys = (2 *s + 1) / (s ** 2 + 4 * s + 3)
initial_value = limit(s * Ys , s, oo)  # 计算初值
print("Initial value:", initial_value)
final_value = limit(s * Ys , s, 0)  # 计算终值
print("Final value:", final_value)
yt = inverse_laplace_transform(Ys, s, t)
print(pretty(yt))





