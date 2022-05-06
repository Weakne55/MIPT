import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

Q_l1 = np.array([24.7, 46.8, 68.5, 93.4, 116.2], dtype=np.float64)
Q_t1 = np.array([149.6, 162.6, 177.15, 202.8], dtype=np.float64)

dP1_l = np.array([21.58, 39.24, 58.86, 80.44, 100], dtype=np.float64)
dP1_t = np.array([173.64, 213.86, 270.76, 344.33], dtype=np.float64)


def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        print("These lines are parallel!!!")
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


def fit_function1(x, k):
    return k * x


def fit_function2(x, k, b):
    return k * x + b


def viscosity(d, k, l):
    a = np.pi * d ** 4
    b = 128 * l * k
    return a / b


def Re(Q, D, n):
    a = Q
    A = np.pi * D / 4
    b = n / 1.2 * A
    return a / b


beta_opt, beta_cov = optimize.curve_fit(fit_function1, dP1_l, Q_l1)
print(beta_opt, 'Ламинарное')
plt.scatter(dP1_l, Q_l1, marker='x')
plt.plot(dP1_l, fit_function1(dP1_l, *beta_opt), alpha=0.5, color='red', linestyle='--')

line1 = [beta_opt[0], 0]

beta_opt, beta_cov = optimize.curve_fit(fit_function2, dP1_t, Q_t1)

line2 = [beta_opt[0], beta_opt[1]]

print(line_intersect(line1[0], line1[1], line2[0], line2[1]))

print(beta_opt, 'Турбулентное')
plt.scatter(dP1_t, Q_t1, marker='x')
plt.plot(dP1_t, fit_function2(dP1_t, *beta_opt), alpha=0.5, color='red', linestyle='--')

plt.ylabel('$Q, cм^3/c$')
plt.xlabel('$\Delta P, Па$')

print(viscosity(5.1, line1[0], 90))
print(Re(130.46, 5.1, viscosity(5.1, line1[0], 90)))

plt.show()
