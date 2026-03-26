import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
y1 = np.convolve(a, b, mode='full')
print('full mode (length = 3+4-1):', y1)
y2 = np.convolve(a, b, mode='same')
print('same mode (length = 4):', y2)
y3 = np.convolve(a, b, mode='valid')
print('valid mode (length = 4 -3 + 1):', y3)
