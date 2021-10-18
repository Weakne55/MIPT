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
print(r1)


def g(a, x, T):
    g2 = []
    g1 = []
    for i in range(len(a)):
        g1.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) /
                  (((1 + 69.2 / 878) * (x[i]/100)) * ((T[i] / (2 * np.pi)) ** 2)))
        g2.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) / ((a[i]/100) * (T[i] / (2 * np.pi)) ** 2))
    return g1


print(np.mean(g(a, r1, T)))
print(g(a, r1, T))

u0 = [i**2 for i in T]
u = []
v = [j**2 for j in a]
for i in range(len(x)):
    u.append(u0[i]*r1[i])


p = np.polyfit(u, v, 1)
fig, (ax1, ax2) = plt.subplots(1, 2)
#ax1.plot(u, p, 'r')
ax1.scatter(u, v, s=8)
ax2.scatter(a, T, s=8)
plt.show()
