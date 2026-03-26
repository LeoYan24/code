from scipy import signal

r, p, k = signal.residuez([1, 0, 0], [1, -1.5, 0.5])
print(r, p, k)

b, a = signal.invresz(r, p, k)
print(b, a)
