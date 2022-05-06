import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

h1 = np.array([25.1, 25.5, 24.9, 25.1, 27.8, 26.7, 29, 24.5, 26, 26.5, 27.1, 29.5, 28, 29.5, 25.9], dtype=np.float64)
h2 = np.array([6.3, 6, 6.3, 6.1, 6.7, 5.8, 5.9, 4.8, 4.6, 4, 3.1, 2.7, 2, 1.8, 1.1], dtype=np.float64)
t = np.array([0.33, 0.47, 0.53, 1, 1.21, 2, 3.23, 5.5, 7.05, 10.21, 15.5, 20.34, 25.54, 30.2, 35.23], dtype=np.float64)


def fit_function(x, k, b):
    return k * x + b


y = np.log(h1/h2)
beta_opt, beta_cov = optimize.curve_fit(fit_function, t, y)
print(beta_opt)


plt.xlim(0, 37)
plt.xlabel('$\\tau$,c')

plt.rcParams['text.usetex'] = True

plt.ylabel('$\ln\\frac{h_1}{h_2}$')

plt.scatter(t, y, marker='x')
plt.plot(t, fit_function(t, *beta_opt), alpha=0.5, color='red', linestyle='--')
plt.show()