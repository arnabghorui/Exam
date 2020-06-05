from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

def fun(x, y):
	return np.vstack((y[1], 4*(y[0]-x)))

def bc(ya, yb):
	return np.array([ya[0], yb[0]-2])


x = np.linspace(0, 1, 20)
y = np.zeros((2, x.size))
res = solve_bvp(fun, bc, x, y)
# print(len(x))
# print(len(y ))

e = np.exp(1)
y_exact = e**2*( (e**4-1)**-1)*(np.exp(2*x)-np.exp(-2*x))+x

x_plot = np.linspace(0, 1, 20)
y_plot = res.sol(x_plot)[0]

print("\tx  \t\t\t\t\t\tRelative Error")
for i in range(1,20):
	print(x[i], "\t\t\t\t", 100*abs(y_plot[i] - y_exact[i])/y_exact[i])

# x_plot = np.linspace(0, 1, 20)
# y_plot = res.sol(x_plot)[0]
plt.plot(x_plot, y_plot, label='Calculated Solution')

plt.scatter(x, y_exact, label='Exact Solution', color = 'r')

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()