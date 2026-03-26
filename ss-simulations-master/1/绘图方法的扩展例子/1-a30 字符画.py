import os

import easygui as eg
from PIL import Image

'''手动打开图片
pth = eg.fileopenbox(title='请打开要转换的图片')  # 打开图片
dir = os.path.dirname(pth)  # 返回图片所在的路径
name = os.path.basename(pth)  # 返回图片名称及扩展名
name = os.path.splitext(name)[0]  # 返回图片名称
out_name = os.path.join(dir, name + '.txt')  # 输出的名字及路径
img = Image.open(pth)
'''

'''打开固定图片'''
img = Image.open(r"../../data/lena.jpg")  # 打开图像
out_name = os.path.join("../../data/", 'lena.txt')  # 输出的名字及路径
crop_img = img.resize((256, 256))  # 缩小图像
out_img = crop_img.convert('L')  # 图片转换为灰度模式
w, h = out_img.size
asciis = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^\ '
asciis = "@%#*+=-:. "  # 灰度表
texts = ''
for row in range(h):
    for col in range(w):
        gray = out_img.getpixel((col, row))
        texts += asciis[int(gray / 255 * (len(asciis) - 1))]  # 根据灰度值选择不同复杂度的 ASCII 字符
    texts += '\n'
with open(out_name, "w") as file:
    file.write(texts)
    file.close()

'''实际显示效果和字体、图像、asciis选取和屏幕设置都有关系'''
