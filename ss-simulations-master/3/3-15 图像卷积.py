import numpy as np
from PIL import Image
from scipy import signal

im = Image.open(r"../data/lena.jpg") # 打开图像
bw_im = im.convert('L') # 图像转为灰度
bw_im_array = np.array(bw_im)# 图像转为数组
k = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])  # 实现边缘检测的卷积核
grad = signal.convolve2d(bw_im_array, k, boundary='symm', mode='same')  # 2d卷积
print('卷积后数组数据类型:', grad.dtype)
print('卷积后数组形状:', grad.shape)
print('卷积后数组值范围:', grad.min(), '到', grad.max())
new_im = Image.fromarray(np.int16(np.array(grad)))  # 数组转为图像
new_im.show()

'''定义卷积核'''
# 低通（盒模糊）
filter1 = 1 / 9 * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# 高斯模糊
filter21 = 1 / 16 * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
filter22 = 1 / 256 * np.array([[1, 4, 6, 4, 1],
                               [4, 16, 24, 16, 4],
                               [6, 24, 36, 24, 6],
                               [4, 16, 24, 16, 4],
                               [1, 4, 6, 4, 1]])
# 锐化
filter3 = 0.9 * np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
# 边缘检测
filter4 = 0.9 * np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])