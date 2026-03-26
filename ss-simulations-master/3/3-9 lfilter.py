from scipy import signal
b = [0, 2]
a = [1, -0.8]
x1 = [1, 2, 3, 4]
y1 = signal.lfilter(b, a, x1)
print(y1)
_,y2 = signal.dlsim((b, a, 1),x1)
print(y2)
