import matplotlib.pyplot as plt
import numpy as np

all = 100  # 总贷款额度
I = 0.063  / 12 # 月利率
B = all  # 当前剩余的贷款额度
x = 1  # 假设每月还1万
y_total = []  # 本金减少的趋势数组
i = 0  # 还款月份计数
while True:
    i += 1  # 月份计数
    Im = B * I / 12  # 当前利息
    B = B + B * I- x  # 本金减少额度
    y_total.append(B)  # 本金减少的趋势数组
    if B <= 0:
        y_total[-1] = 0  # 本金剩余不能为负数，相当于最后一个月还款额根据实际情况缴纳
        break
print("共计还款%d月（约%d年）" % (i, round(i / 12, 0)))

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 14
plt.ylabel("剩余本金变化")
plt.xlabel("月份")
plt.bar(np.arange(i), y_total, width=0.4)
plt.show()
