import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1298)
N = 1024
x = np.linspace(0, N-1, N)
y = np.random.random(N)

Fft = np.fft.fft(y, norm = "ortho")
k = 2*np.pi*np.fft.fftfreq(N, d = 1)
# print(len(k))

k_min, k_max = min(k), max(k)
print("Minimum value of k is: ", k_min, "and maximum value of k is: ", k_max)


pw_spec = np.zeros(N)
for i in range(N):
	pw_spec[i] = ( np.absolute(Fft[i]) )**2 / N


plt.subplots()
plt.title("Random numbers")
plt.scatter(x,y, color = 'r')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")

plt.subplots()
plt.title("Power spectrum")
plt.plot(k, pw_spec, color = 'g')
plt.xlabel(r"$k$")
plt.ylabel(r"$|\tilde{f}(k)|^2 / N$")

plt.subplots()
plt.title("Density histogram of power spectrum")
plt.hist(pw_spec, range = (k_min, k_max), bins = 5, density = True)
plt.xlabel(r"bins")
plt.ylabel(r"$|\tilde{f}(k)|^2 / N$")
plt.show()


