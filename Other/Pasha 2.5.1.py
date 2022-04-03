import matplotlib.pyplot as plt
import numpy as np


sigt = -0.11861916
eps = 1.7 # %
eps2 = 1.7272
T = [303.15, 308.15, 313.15, 318.15, 323.15, 328.15, 333.05]
T = np.array(T)
sig = [59.24, 58.67, 57.89, 57.39, 56.74, 56.27, 55.70]
sig = np.array(sig)
errors = sig*eps/100
q = - T * sigt
UP = sig - q
qerr = q*eps2/100
uperr = UP*eps2/100
tabl = [71.2, 69.6, 67.9, 66.2]
tablT = [303.15, 313.15, 323.15, 333.15]

plt.errorbar(T, sig, errors, 0.1, '.', label='experiment data')
# plt.errorbar(T, UP, uperr, 0.1, '.', label='experiment data')
p, cov = np.polyfit(T, sig, deg=1, cov=True)
p2, cov = np.polyfit(tablT, tabl, deg=1, cov=True)
print(p2)
print(cov)
p = np.poly1d(p)
p2 = np.poly1d(p2)
X = np.linspace(302, 334, 100)
plt.plot(X, p(X), label='approximation')
plt.title('График 1. \n Зависимость поверхностного натяжения от температуры')
plt.xlabel('T, K')

plt.ylabel('$\sigma$, дин/см')
plt.plot(tablT, tabl, '>', label='Table data')
plt.plot(X, p2(X), '--')
plt.grid()
plt.ylim((54.5, 72))
plt.legend()
plt.show()