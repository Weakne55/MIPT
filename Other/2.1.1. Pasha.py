import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

dT1 = np.array([0,2.78, 4.57, 5.04, 5.28, 4.08])
N1 = np.array([0,0.7509, 1.244, 1.337, 1.394, 1.094])

dT2 = np.array([0,2.53, 3.83, 5.85, 7.42])
N2 = np.array([0,0.4937, 0.7864, 1.168, 1.385])


def fit_function(x, k):
    return k * x


beta_opt1, beta_cov1 = optimize.curve_fit(fit_function, N1, dT1)
plt.plot(N1, fit_function(N1, *beta_opt1), color='blue',alpha=0.5)
print('k1')
print(beta_opt1[0])
print(beta_cov1[0]**0.5)
beta_opt2, beta_cov2 = optimize.curve_fit(fit_function, N2, dT2)
plt.plot(N2, fit_function(N2, *beta_opt2), color='red',alpha=0.5)
print('k2')
print(beta_opt2[0])
print(beta_cov2[0]**0.5)

plt.plot(N1, dT1, '.', label='q$_1$= 0.2127 г/с')
plt.plot(N2, dT2, 'x', color='black', label='q$_2$ = 0.1488 г/с')

plt.xlabel('$N$, Вт')
plt.ylabel('$\Delta T, ^oC$')

plt.legend(loc='best')
plt.grid()
plt.show()

