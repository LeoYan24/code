import numpy as np
from PIL import Image  # pillow
from scipy import signal

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
# 选一个卷积和
filter = filter4
'''打开图像'''
# 打开图像,得到<class 'PIL.Image.Image'>
im = Image.open("../../data/lena.jpg")
# 查看图像参数
print(im.mode)  # RGB
print(im.format)
# 剪裁为480*480
box = (round(im.width / 2 - 240, 0),
       round(im.height / 2 - 240, 0),
       round(im.width / 2 + 240, 0),
       round(im.height / 2 + 240, 0))
crop_im = im.crop(box)
print('size', crop_im.size)
# 分离颜色通道,分类之后的类型为<class 'PIL.Image.Image'>
r, g, b = crop_im.split()
'''显示各个通道的灰度'''
to_image = Image.new('RGB', (480 * 2, 480 * 2))
to_image.paste(crop_im, (0, 0))
to_image.paste(r, (481, 0))
to_image.paste(g, (0, 481))
to_image.paste(b, (481, 481))
to_image.show()
'''
只显示单色
# Image.new('L', crop_im.size),表示空白图像
'''
new_im1 = Image.merge("RGB", (r,
                              Image.new('L', crop_im.size),
                              Image.new('L', crop_im.size)))
# 只显示green
new_im2 = Image.merge("RGB", (
    Image.new('L', crop_im.size),
    g,
    Image.new('L', crop_im.size)))

# 只显示blue
new_im3 = Image.merge("RGB", (
    Image.new('L', crop_im.size),
    Image.new('L', crop_im.size),
    b))
# 改变RGB顺序
new_im4 = Image.merge("RGB", (b, r, g))

# 显示单色通道和通道乱序
to_image = Image.new('RGB', (480 * 2, 480 * 2))
to_image.paste(new_im1, (0, 0))
to_image.paste(new_im2, (481, 0))
to_image.paste(new_im3, (0, 481))
to_image.paste(new_im4, (481, 481))
to_image.show()

# 三个通道分别卷积
r_result = signal.convolve2d(np.array(r), filter, boundary='symm', mode='same')
g_result = signal.convolve2d(np.array(g), filter, boundary='symm', mode='same')
b_result = signal.convolve2d(np.array(b), filter, boundary='symm', mode='same')
# 把三个通道分别转换为单色图像，必须加入convert语句，指示这是单色图像，否则无法merge
# 此时无论是否加convert语句，直接显示的效果都是单色图像
r_result = Image.fromarray(r_result).convert('L')
g_result = Image.fromarray(g_result).convert('L')
b_result = Image.fromarray(b_result).convert('L')
# 把三个通道合并到
new_im = Image.merge("RGB", (r_result, g_result, b_result))  # 合并通道

# 把新旧图像拼接一下
to_image = Image.new('RGB', (480 * 2, 480))
to_image.paste(crop_im, (0, 0))
to_image.paste(new_im, (481, 0))
to_image.show()

'''
mode： str {‘full’, ‘valid’, ‘same’}，可选
指示输出大小的字符串：
    full
    输出是输入的完全离散线性卷积。 (默认)
    valid
    输出仅包含那些不依赖零填充的元素。在 ‘valid’ 模式中，in1 或 in2 在每个维度上都必须至少与另一个一样大。
    same
    输出与 in1 大小相同，以 ‘full’ 输出为中心。
boundary： str {‘fill’, ‘wrap’, ‘symm’}，可选
指示如何处理边界的标志（如何填充）：
    fill
    用填充值填充输入数组。 (默认)
    wrap
    圆形边界条件。
    symm
    对称边界条件。
'''
