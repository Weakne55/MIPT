from matplotlib import pyplot as plt
from scipy import optimize
import numpy as np

x = [0, 2, 1, 3, 4]
y = [0.0144, 0.0912, 0.0628, 0.1294, 0.1575]


# y =k*x + b
# (0.1141 - b) / x
# 0.1141 - ?
# 5, 7, 9
# 0.148, 0.1565, 0.1495


def fit_function(x, k, b):
    return k * x + b


# ax = plt.axes()
# ax.set_facecolor('gray')

plt.scatter(x[:len(y)], y, marker='^', color='black')
line1, beta_cov = optimize.curve_fit(fit_function, np.array(x[:len(y)],
                                                            dtype=np.float64), np.array(y, dtype=np.float64))

plt.plot(np.array(x[:len(y)], dtype=np.float64),  # x
         fit_function(np.array(x[:len(y)], dtype=np.float64), *line1),  # y
         color='red', linestyle='-',  # params
         label='Линейная аппроксимация МНК')

print('k = ', round(line1[0], 3), '\n'
                                  'b = ', round(line1[1], 3))

print(round((0.1141 - line1[1]) / line1[0], 3))
plt.xlabel('$C,\\frac{мг}{мл}$')
plt.ylabel('$Abs$')

plt.title('Зависимость оптической плотности от концентрации белка', loc='right')
plt.legend()
plt.grid()

plt.show()
