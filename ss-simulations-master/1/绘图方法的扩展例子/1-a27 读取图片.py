import matplotlib.pylab as plt  # 绘制图形
import matplotlib.image as mpimg

image = mpimg.imread("../../data/lena.jpg")
# 创建一个图形和轴
plt.subplots()
# 显示图片
plt.imshow(image,animated=True)
# 移除坐标轴（可选）
plt.axis('off')
# 显示图形
plt.show()