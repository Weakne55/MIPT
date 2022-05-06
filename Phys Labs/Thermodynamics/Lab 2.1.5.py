import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

mass0 = np.array([477.4, 655.5, 832.2, 1006.9, 52.0,
                  217, 395, 569.9, 746.6, 924.7,
                  176.7, 341.7, 519.8, 719.8, 1194.9],
                 dtype=np.float64)
ln0 = 16
ln_ = np.array([18.4, 20.2, 22.0, 23.4, 16.2,
                16.8, 18, 19.4, 21.3, 23.1,
                16.7, 17.7, 19.2, 21, 25.9], dtype=np.float64)

mass = np.sort(mass0)
ln = np.sort(ln_)

g = 9.81
f = mass * g / 1000
a1 = ln / ln0
a2 = a1 - (1 / (a1 ** 2))


# print('mass', mass)
# print('ln', ln)
# print('lambda', a1)
# print('force', f)
# print('lambda2', a2)


def fit_function(x, k, b):
    return k * x + b


# plt.scatter(a1, f, marker='x', color='black')
# plt.ylabel("$f$,$H$", rotation='horizontal')
# plt.xlabel("$\lambda$")
# beta_opt, beta_cov = optimize.curve_fit(fit_function, a1, f)
# print('a1', beta_opt)
# plt.plot(a1, fit_function(a1, *beta_opt), color='blue')
# plt.grid()
# plt.show()
#
# plt.scatter(a2, f, marker='x', color='black')
beta_opt, beta_cov = optimize.curve_fit(fit_function, a2, f)
# print('a2',beta_opt)
# print('a2',beta_cov)
# plt.plot(a2, fit_function(a2, *beta_opt), color='blue', label='fit1')
# plt.ylabel("$f$,$H$", rotation='horizontal')
# plt.xlabel("$\lambda - 1/\lambda^2$")
# plt.grid()
# plt.show()


s0 = 21.6
# E = (f * 3 / s0) / a2
E = 1.24

l0 = 16 / 100
a3 = np.array([1.11, 1.23, 1.3, 1.41, 1.46, 1.53, 1.64],
              dtype=np.float64)

A = (E * s0 / 3) * (a3 ** 2 * l0 / 2 + l0 / a3 - l0 / 2 - l0)

dT = np.array([0.067, 0.221, 0.34, 0.52, 0.62, 0.75, 1.05],
              dtype=np.float64)

# plt.scatter(A, dT, marker='x', color='black')
# plt.ylabel("$\Delta$,$T,C$")
# plt.xlabel("$A$,$Дж$")
# beta_opt3, beta_cov3 = optimize.curve_fit(fit_function, A, dT)
# print('A', beta_opt3)
# plt.plot(A, fit_function(A, *beta_opt3), color='blue')
# plt.grid()
# plt.show()


Cl = A / dT
# print(Cl)

t = np.array([11, 23.4, 37.6, 49.8, 53, 97.2],
             dtype=np.float64)
lnt = np.array([-3.215, -3.434, -3.680, -3.887, -4.082, -4.560],
               dtype=np.float64)

plt.scatter(t, lnt, marker='x', color='black')
plt.ylabel("$ln T$")
plt.xlabel("$t,c$")
beta_opt4, beta_cov4 = optimize.curve_fit(fit_function, t, lnt)
print('ln', beta_opt4)
plt.plot(t, fit_function(t, *beta_opt4), color='blue')
plt.grid()
plt.show()

