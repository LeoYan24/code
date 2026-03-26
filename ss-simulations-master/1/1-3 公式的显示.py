import matplotlib.pyplot as plt

'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
'''公式字体风格——stix
stix字体（ Scientific and Technical Information Exchange 字体）（https://www.stixfonts.org/），
该风格比较接近Time New Roma，甚至可以直接当新罗马来用，并且是开放免费的
对比而言，Times New Roman是有版权的，为 Monotype 公司所有'''
plt.rcParams['mathtext.fontset'] = 'stix'

plt.title('$f_1(t)$')  # 显示标题
plt.text(1, 1, r"$e^{j\omega_0 t}$", fontsize=14)
plt.text(2, 2, r"$cos(100\pi t+\phi)$", fontsize=14)
plt.text(3, 3, r"$G_\tau (t)$", fontsize=14)
plt.xlim(0, 4)  # 限定x轴范围
plt.ylim(0, 4)  # 限定y轴范围
plt.grid()
plt.show()  # 显示图像


'''
五类字体：serif，sans-serif，monospace，cursive和fantasy，（衬线，无衬线和等宽字体族、手写、艺术字体）
默认使用非衬线字体
plt.rcParams['font.family'] = 'serif'  # 指定衬线字体
plt.rcParams['font.serif'] = ['SimSun']  # 指定默认衬线字体

常见字体：
宋体 SimSun
黑体 SimHei
微软雅黑 Microsoft YaHei
微软正黑体 Microsoft JhengHei
新宋体 NSimSun
新细明体 PMingLiU
细明体 MingLiU
标楷体 DFKai-SB
仿宋 FangSong
楷体 KaiTi
仿宋_GB2312 FangSong_GB2312
楷体_GB2312 KaiTi_GB2312
'''

'''
关于plt.rcParams['font.size'] = 10
matplotlib自己有一套字体比例缩放机制，不一定所有位置显示内容均为10号字
比如：
plt.rcParams['font.size'] = 12
和
plt.title("原信号", fontsize=12, loc='left')
相比较，只配置前者时，显示的（title）字体要大，主观感觉大2-3号
'''
