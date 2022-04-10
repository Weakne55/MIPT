import matplotlib.pyplot as plt
import numpy as np

mass = np.array([477.4, 655.5, 832.2, 1006.9, 52.0, 217, 395, 569.9, 746.6, 924.7, 176.7, 341.7, 519.8, 719.8, 1194.9],
                dtype=np.float64)
ln0 = 16
ln = np.array([18.4, 20.2, 22.0, 23.4, 16.2, 16.8, 18, 19.4, 21.3, 23.1, 16.7, 17.7, 19.2, 21, 25.9], dtype=np.float64)

g = 9.81
f = mass * g / 100
a1 = ln / ln0
a2 = a1 - 1 / pow(a1, 2)
print(np.sort(mass))
print(np.sort(a1))

plt.scatter(a1, f, marker='x', color='black')
plt.ylabel("$f$,$H$", rotation='horizontal')
plt.xlabel("$\lambda$")
plt.grid()
plt.show()

plt.scatter(a2, f, marker='x', color='black')
plt.ylabel("$f$,$H$", rotation='horizontal')
plt.xlabel("$\lambda - 1/\lambda^2$")
plt.grid()
plt.show()
