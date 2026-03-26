import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，防止绘图时中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

def solve_rlc_response():
    # 1. 定义符号
    s, t = sp.symbols('s t', real=True)
    
    # 2. 系统参数
    # 使用 SymPy 的 Rational 和 Integer 进行精确计算，避免浮点数导致的符号运算错误
    LC_val = sp.Rational(1, 100) # LC = 0.01
    L_val = sp.Integer(1)        # L = 1
    
    # R 的取值列表
    R_values = [0, sp.Rational(1, 10), 1, 10]
    
    # 3. 定义输入信号 x(t) 及其拉普拉斯变换 X(s)
    # omega_0 通常定义为 1/sqrt(LC)
    w0 = 1 / sp.sqrt(LC_val) # w0 = 10
    
    inputs = [
        {
            "label": "u(t)",
            "X_s": 1/s,
            "desc": "阶跃响应"
        },
        {
            "label": "exp(-3t)u(t)",
            "X_s": 1/(s + 3),
            "desc": "指数衰减输入"
        },
        {
            "label": f"sin({w0}t)u(t)",
            "X_s": w0 / (s**2 + w0**2),
            "desc": "正弦输入"
        }
    ]
    
    # 准备绘图
    fig, axes = plt.subplots(len(R_values), len(inputs), figsize=(15, 12), constrained_layout=True)
    
    print("开始计算系统响应...\n")
    
    for i, R_val in enumerate(R_values):
        # 构造系统函数 H(s)
        # H(s) = (s/L) / (s^2 + (R/L)s + 1/LC)
        numerator = s / L_val
        denominator = s**2 + (R_val / L_val) * s + (1 / LC_val)
        H_s = numerator / denominator
        
        print(f"--- R = {float(R_val)} ---")
        print(f"H(s) = {H_s}")
        
        for j, inp in enumerate(inputs):
            X_s = inp["X_s"]
            Y_s = H_s * X_s
            
            # 4. 利用拉普拉斯逆变换求 y(t)
            try:
                y_t = sp.inverse_laplace_transform(Y_s, s, t)
                # 简化结果
                y_t = sp.simplify(y_t)
            except Exception as e:
                print(f"逆变换计算失败: {e}")
                y_t = sp.Integer(0)

            print(f"输入: {inp['label']}")
            print(f"响应 y(t): {y_t}\n")
            
            # 5. 绘图
            # 将 sympy 表达式转换为 numpy 可调用的函数
            # modules 参数处理 Heaviside 函数
            try:
                y_func = sp.lambdify(t, y_t, modules=['numpy', {'Heaviside': lambda x: np.heaviside(x, 1)}])
                
                # 时间轴
                t_eval = np.linspace(0, 10, 1000)
                y_vals = y_func(t_eval)
                
                # 如果结果是常数（标量），扩展为数组
                if np.isscalar(y_vals):
                    y_vals = np.full_like(t_eval, y_vals)
                
                ax = axes[i, j]
                ax.plot(t_eval, y_vals)
                ax.set_title(f"R={float(R_val)}, Input={inp['label']}")
                ax.set_xlabel("t (s)")
                ax.set_ylabel("y(t)")
                ax.grid(True)
            except Exception as e:
                print(f"绘图出错 (R={float(R_val)}, Input={inp['label']}): {e}")

    plt.suptitle(f"RLC电路系统响应 (LC=0.01, L=1H)", fontsize=16)
    plt.show()

if __name__ == "__main__":
    solve_rlc_response()
