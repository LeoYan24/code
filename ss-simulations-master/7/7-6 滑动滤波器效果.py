import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

'''生成一个随机序列'''
input = np.random.randn(100)
'''定义系统'''
A = [1, 0, 0, 0, 0, 0, 0]
B = np.ones(7) / 7
dsys = signal.dlti(B, A, dt=True)
'''求冲激响应'''
n, hn = dsys.impulse(n=100)
print(hn[0].T)
# 计算输出序列的方式1，直接使用lfilter函数
output = signal.lfilter(B, A, input)
# 计算输出序列的方式2，使用
output = np.convolve(input, np.squeeze(hn))

'''绘图对比'''
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(figsize=(8, 4))
plt.subplot(211)
plt.grid()
plt.title('input', loc='left')
plt.plot(input)

plt.subplot(212)
plt.grid()
plt.title('response', loc='left')
plt.plot(output[:100])

plt.tight_layout()
plt.show()

'''方式2
B = [0.5,0.5]
A = [1,0]
dsys = signal.dlti(B, A, dt=True)
w = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
w, Hw = dsys.freqresp(w=w)\
'''
