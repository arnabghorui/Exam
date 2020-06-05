import numpy as np
import matplotlib.pyplot as plt 
import math

def box(x):
	if abs(x) <= 1:
		return 1
	else:
		return 0

x_min = -10
x_max = 10

fig, axis = plt.subplots(3)
# N = 128
index = 0
for N in [100, 1000, 10000]:
	m = 2*N + 1
	f = np.zeros(m)
	x = np.linspace(x_min, x_max, m)
	dx = (x_max - x_min) / (2*N)

	for i in range(m):
		f[i] = box(x_min + i*dx)

	FT_f = np.fft.fft(f, norm = 'ortho')
	k = 2*np.pi*np.fft.fftfreq(m, d = dx)
	FT_f = dx*np.exp(-1j*k*x_min)*FT_f*np.sqrt(m/(2*np.pi))


	axis[index].plot(k, np.real(FT_f), label = dx)
	axis[index].set_xlabel("k")
	axis[index].set_ylabel(r"$\tilde{F}(k)$")
	axis[index].legend()
	index = index + 1


x = np.linspace(-2, 2, 101)
y = np.zeros(101)
for i in range(101):
	y[i] = box(x[i])

plt.subplots()
plt.xlabel("x")
plt.ylabel("box(X)")
plt.plot(x, y, color = 'r')

plt.show()

