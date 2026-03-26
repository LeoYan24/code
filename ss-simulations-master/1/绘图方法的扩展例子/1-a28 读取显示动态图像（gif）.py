from PIL import Image, ImageSequence
import matplotlib.animation as animation
import matplotlib.pylab as plt

def get_frames(filename):
    im = Image.open(filename)
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    frame_count = len(frames)
    frame_index = 0
    while True:
        yield frames[frame_index]
        frame_index = (frame_index + 1) % frame_count  # 实现循环索引
#迭代获得图像的每一帧
f1 = get_frames("../../data/a-tau-1.gif")
f2 = get_frames("../../data/a-tau-2.gif")
# 创建一个图形和轴
fig= plt.figure(figsize=(10, 5))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
#更新动画
def update(frame):
    ax1.clear()
    ax1.axis('off')
    ax1.imshow(next(f1))

    ax2.clear()
    ax2.axis('off')
    ax2.imshow(next(f2))
    return
# 创建动画
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)
# 显示动画
plt.show()