import numpy as np
import matplotlib.pyplot as plt

quant = [31.88, 31.97, 31.96, 31.91, 32.12, 32.04, 32.10, 32, 32]
mn = np.mean(quant)


def random(arr, m):
    s = 0
    for item in arr:
        s += (item - m) ** 2
    return np.sqrt(s / (len(arr) - 1))


# print(np.sqrt(random(quant, mn) ** 2 + 0.0001))

r = [43, 37.65, 32.3, 26.9, 21.55, 16.2, 10.8]  #расстояние от центра масс до призмы
a = [40, 35, 30, 25, 20, 15, 10]                        #расстояние от l/2 до призмы
x = [0.53, 0.5265, 0.523, 0.519, 0.5155, 0.512, 0.508]  #центр масс - экспериментальное
T = [1.565, 1.541, 1.523, 1.535, 1.577, 1.709, 1.967]   #период

r1 = []                             #расстояние до центра масс до призмы посчитанное
for i in range(len(r)):
    r1.append(((0.878*a[i]-0.0692)/(0.878+0.0692)))


def g(a, x, T):
    g2 = []
    g1 = []
    for i in range(len(a)):
        g1.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) /
                  (((1 + 69.2 / 878) * (x[i]/100)) * ((T[i] / (2 * np.pi)) ** 2)))
        g2.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) / ((a[i]/100) * (T[i] / (2 * np.pi)) ** 2))
    return g1


print(np.mean(g(a, r1, T)))  # среднее значение ускорения свободного падения
print(g(a, r1, T))  # все значения для разных начальных данных

u0 = [i**2 for i in T]
u = []
v = [j**2 for j in a]
for i in range(len(x)):
    u.append(u0[i]*r1[i])


p1 = np.polyfit(u, v, 1)
LinPlotEq1 = np.poly1d(p1)
X1 = np.linspace(0, 100, 1500)
Y1 = [LinPlotEq1(i) for i in X1]

p2 = np.polyfit(a, T, 4)
LinPlotEq2 = np.poly1d(p2)
X2 = np.linspace(0, 50, 100)
Y2 = [LinPlotEq2(i) for i in X2]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.set_xlim([30, 100])
ax1.set_ylim([0, 1700])
ax1.grid(True)

ax2.set_xlim([5, 45])
ax2.set_ylim([1.45, 2])
ax2.grid(True)

ax1.plot(X1, Y1, 'k', alpha=0.5)
ax2.plot(X2, Y2, 'k', alpha=0.5)

ax1.scatter(u, v, s=8, c='r')
ax2.scatter(a, T, s=8, c='r')
plt.show()
