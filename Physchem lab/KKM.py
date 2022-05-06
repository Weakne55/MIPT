import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

k0 = 2.61

C = np.array([0.35, 1.05, 1.75, 2.45, 3.5, 4.2, 5.95, 7.7, 9.45, 10.5], dtype=np.float64)
k_up = np.array([35.2, 98.4, 160.7, 222, 303, 332, 379, 417, 456, 478], dtype=np.float64) - k0
k_down = np.array([523, 495, 450, 404, 354, 328, 257, 183.2, 108.2, 34.7], dtype=np.float64) -k0


# k(c)


def fit_function(x, k, b):
    return k * x + b

# ---------------------------------------------
line1, beta_cov = optimize.curve_fit(fit_function, C[0:5], k_up[0:5])

line2, beta_cov = optimize.curve_fit(fit_function, C[5:10], k_up[5:10])


print(line1)
print(line2)


def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        print("These lines are parallel!!!")
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


print('точка пересечения ', line_intersect(line1[0], line1[1], line2[0], line2[1]))

x1, y1 = line_intersect(line1[0], line1[1], line2[0], line2[1])

plt.scatter(C[0:5], k_up[0:5], marker='x',color='red')
plt.plot(C[0:5], fit_function(C[0:5], *line1), alpha=0.5, color='red', linestyle='--',label='Увеличение концентрации')

plt.scatter(C[5:10], k_up[5:10], marker='x',color='red')
plt.plot(C[5:10], fit_function(C[5:10], *line2), alpha=0.5, color='red', linestyle='--')

plt.scatter(x1, y1, color='red', label='ККМ №1')  # точка пересечения


# ---------------------------------------------




# ---------------------------------------------
line1, beta_cov = optimize.curve_fit(fit_function, np.flip(C[5:10], 0), k_down[0:5])

line2, beta_cov = optimize.curve_fit(fit_function, np.flip(C[0:5], 0), k_down[5:10])


print(line1)
print(line2)


def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        print("These lines are parallel!!!")
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


print('точка пересечения ', line_intersect(line1[0], line1[1], line2[0], line2[1]))

x2, y2 = line_intersect(line1[0], line1[1], line2[0], line2[1])

plt.scatter(np.flip(C[5:10], 0), k_down[0:5], marker='x',color='blue')
plt.plot(np.flip(C[5:10], 0), fit_function(np.flip(C[5:10], 0), *line1), alpha=0.5, color='blue', linestyle='--')

plt.scatter(np.flip(C[0:5], 0), k_down[5:10], marker='x',color='blue')
plt.plot(np.flip(C[0:5], 0), fit_function(np.flip(C[0:5], 0), *line2), alpha=0.5, color='blue', linestyle='--', label='Уменьшение концентрации')

plt.scatter(x2, y2, color='blue', label='ККМ №2')  # точка пересечения

plt.title('Рис. 4', loc='right')


plt.xlabel('$C_{ПАВ}$,мМ')
plt.ylabel('$κ,\\frac{мкСм}{см}$')

plt.legend()
plt.grid()
plt.show()
# ---------------------------------------------


x_true = (x1 + x2)/2
y_true = (y1 + y2)/2
print(round(x_true, 3), round(y_true, 3))
