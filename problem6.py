import numpy as np
import math
import matplotlib.pyplot as plt

def f(x, y1, y2):
	return 32*y1 + 66*y2 + 2*x/3 + 2/3

def g(x, y1, y2):
	return -66*y1 - 133*y2 - x/3 - 1/3

x_i, x_f = 0.0, 0.5
h = 0.01
N = int( (x_f - x_i) / h )

x = np.linspace(x_i, x_f, N + 1)
y1 = np.zeros(N + 1) 
y2 = np.zeros(N + 1) 

y1[0] = 1/3
y2[0] = 1/3

for i in range(N):
	k1 = h*f(x[i], y1[i], y2[i])
	l1 = h*g(x[i], y1[i], y2[i])

	k2 = h*f(x[i] + 0.5*h, y1[i] + 0.5*k1, y2[i] + 0.5*l1)
	l2 = h*g(x[i] + 0.5*h, y1[i] + 0.5*k1, y2[i] + 0.5*l1)

	k3 = h*f(x[i] + 0.5*h, y1[i] + 0.5*k2, y2[i] + 0.5*l2)
	l3 = h*g(x[i] + 0.5*h, y1[i] + 0.5*k2, y2[i] + 0.5*l2)

	k4 = h*f(x[i+1], y1[i] + k3, y2[i] + l3)
	l4 = h*g(x[i+1], y1[i] + k3, y2[i] + l3)

	y1[i+1] = y1[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
	y2[i+1] = y2[i] + (1/6)*(l1 + 2*l2 + 2*l3 + l4)

plt.plot(x, y1, color = 'r', label = r"$y_1$")
plt.plot(x, y2, color = 'g', label = r"$y_2$")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()