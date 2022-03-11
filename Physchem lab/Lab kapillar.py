import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize



def approximate_function(link=str, color_dots=None, color_curve=None, marker_dots=None):
    """"link должна иметь вид С:\home\lab\measure1.txt"""
    with open(link, 'r') as file:
        lines = file.readlines()[6:]
    t0 = list()
    E0 = list()
    I0 = list()
    for e in lines:
        t0.append(np.float64(e.split()[0]))
        E0.append(np.float64(e.split()[1]))
        I0.append(np.float64(e.split()[2]))
    t = np.array(t0)
    E = np.array(E0)
    I = np.array(I0)

    def fit_function(x, b, k, a0):
        return b * np.exp(-k * x) + a0

    beta_opt, beta_cov = optimize.curve_fit(fit_function, t, I)

    plt.plot(t, fit_function(t, *beta_opt), color=color_curve, label='fit1')
    plt.scatter(t, I, marker=marker_dots, color=color_dots, s=5)


fig, ax = plt.subplots()
approximate_function('C:\Labs\Карпович Гуревич\\11.3+400_1.txt', 'gray', 'blue', 'x')
# approximate_function('C:\Labs\Карпович Гуревич\\11.3+400_2.txt', 'orange', 'green', 'o')
# approximate_function('C:\Labs\Карпович Гуревич\\11.3+400_3.txt', 'black', 'red', '^')
# approximate_function('C:\Labs\Карпович Гуревич\\11.3+400_4.txt')
# approximate_function('C:\Labs\Карпович Гуревич\\11.3+400_5.txt')
approximate_function('C:\Labs\Карпович Гуревич\\11.3-400_1.txt', 'black', 'red')

plt.grid()
plt.show()