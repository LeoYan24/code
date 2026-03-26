import matplotlib.pyplot as plt

x = [1, 2, 4, 2, 3]
n = [1, 2, 3, 4, 5]
'''绘图'''
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置（非衬线）中文字体为宋体
plt.rcParams['font.size'] = 12  # 设置字体大小
plt.rcParams['axes.unicode_minus'] = False  # 解决设置中文字体下，图像中的负号'-'显示为方块的问题

plt.plot(n, x)  # 折线图
plt.grid()  # 显示网格线
plt.title('折线图')  # 显示标题
plt.xlabel('序列n')  # x轴标签
plt.ylabel('序列x')  # y轴标签
plt.xlim(0, 5)  # 限定x轴范围
plt.ylim(0, 5)  # 限定y轴范围
plt.show()  # 显示图像
'''
折线图说明
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
'''

'''
rcParams的可调节内容
https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams
'''


'''
中文支持，以及负号问题
（1）设置一个中文字体，参见衬线和非衬线的区别
（2）axes.unicode_minus选项：
解决使用中文字体时，图像中的负号'-'显示为方块的问题
选项为True时，用unicode减号来表示负号（ '\u2212' [U+2212]）
选项为False时，用连字号（hyphen）表示负号
一些中文字体中没有提供unicode减号，例如SimHei、SimSun等字体，因此需要用连字号来表示负号，
也就是将axes.unicode_minus设置为False。
但有些字体中提供了unicode减号，则不需要设置axes.unicode_minus了，例如:
微软雅黑：'Microsoft YaHei'

然而在使用指数坐标时，如loglog或semilogy时，如果配合使用SimSun、SimHei等字体，
则指数位置上的负号上标无法正常显示，即axes.unicode_minus = False不会对指数位置生效。
会报错：Font 'default' does not have a glyph for '\u2212' [U+2212], substituting with a dummy symbol.
但中文字体改成微软雅黑（Microsoft YaHei）就没问题，或只使用西文字体
'''