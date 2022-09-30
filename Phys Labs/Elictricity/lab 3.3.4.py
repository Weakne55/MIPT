from matplotlib import pyplot as plt
from scipy import optimize
import numpy as np

x = [x / 10 for x in range(1, 15)]
y = [115.6, 207.6, 324.5, 416.4,
     510.9, 605.8, 691.6, 757.4, 825,
     883, 925, 967, 994, 1022, 47.9]

x.append(0.04)
print(x)


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

print('k = ', line1[0], '\n'
                        'b = ', line1[1])

print(round((0.1141 - line1[1]) / line1[0], 3))
plt.xlabel('I,$А$')
plt.ylabel('B,$мТ$')

plt.title('Зависимость магнитного поля от тока', loc='right')
plt.legend()
plt.grid()

plt.show()
