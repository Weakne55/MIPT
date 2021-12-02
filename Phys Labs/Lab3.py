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

r = [43, 37.65, 32.3, 26.9, 21.55, 16.2, 10.8]  # расстояние от центра масс до призмы
a = [40, 35, 30, 25, 20, 15, 10]                        # расстояние от l/2 до призмы
x = [0.53, 0.5265, 0.523, 0.519, 0.5155, 0.512, 0.508]  # центр масс - экспериментальное
T = [1.565, 1.541, 1.523, 1.535, 1.577, 1.709, 1.967]   # период

r1 = []                             # расстояние до центра масс до призмы посчитанное
for i in range(len(r)):
    r1.append(((0.878*a[i]-0.0692)/(0.878+0.0692)))
print('Посчитанное расстояние от центра масс до призмы', *r1, '\n', sep='\n')


def g(a, x, T):
    g2 = []  # формула 6
    g1 = []  # формула 14
    for i in range(len(a)):
        g1.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) /
                  (((1 + 69.2 / 878) * (x[i]/100)) * ((T[i] / (2 * np.pi)) ** 2)))
        g2.append((((1.0011 ** 2) / 12) + (a[i]/100) ** 2) / ((a[i]/100) * (T[i] / (2 * np.pi)) ** 2))
    return g1


def gmax(a, x, T):
    g2 = []  # формула 6
    g1 = []  # формула 14
    for i in range(len(a)):
        g1.append((((1.0061 ** 2) / 12) + (a[i]/100) ** 2) /
                  (((1 + 69.7 / 878.5) * (x[i]/100)) * ((T[i] / (2 * np.pi)) ** 2)))
        g2.append((((1.0061 ** 2) / 12) + (a[i]/100) ** 2) / ((a[i]/100) * (T[i] / (2 * np.pi)) ** 2))
    return g1


def gmin(a, x, T):
    g2 = []  # формула 6
    g1 = []  # формула 14
    for i in range(len(a)):
        g1.append((((0.9961 ** 2) / 12) + (a[i]/100) ** 2) /
                  (((1 + 68.7 / 877.5) * (x[i]/100)) * ((T[i] / (2 * np.pi)) ** 2)))
        g2.append((((0.9911 ** 2) / 12) + (a[i]/100) ** 2) / ((a[i]/100) * (T[i] / (2 * np.pi)) ** 2))
    return g1


def normdev(g, mn):
    for j in range(len(g)):
        g[j] = (g[j] - mn)**2
    s = sum(g)
    return np.sqrt(s/(len(g)-1))


gk = []
for i in range(len(x)):
    gk.append((26.7*((np.pi)**2)*4)/((1 + 68.7 / 877.5))/100)
print(np.mean(gk), 'g полученное из наклона прямой на графике')


NormDev = normdev(g(a, r1, T), np.mean(g(a, r1, T)))
ErrDev = NormDev/np.sqrt(len(g(a, r1, T)))
FullDev = np.sqrt(ErrDev**2 + 0.5**2)
print('-'*20, NormDev, ErrDev, FullDev, '-'*20, sep='\n')
print(np.mean(g(a, r1, T)))  # среднее значение ускорения свободного падения
print(np.mean(gmax(a, r1, T)), 'max')  # среднее max значение ускорения свободного падения
print(np.mean(gmin(a, r1, T)), 'min')  # среднее min значение ускорения свободного падения
print(g(a, r1, T))  # все значения для разных начальных данных

u0 = [i**2 for i in T]
u = list()
v = [j**2 for j in a]
for i in range(len(x)):
    u.append(u0[i]*r1[i])
print('-'*20, '\n', u, 'Значения')


p1 = np.polyfit(u, v, 1)
LinPlotEq1 = np.poly1d(p1)
print(LinPlotEq1)
X1 = np.linspace(0, 100, 1500)
Y1 = [LinPlotEq1(i) for i in X1]


p2 = np.polyfit(a, T, 4)
LinPlotEq2 = np.poly1d(p2)
X2 = np.linspace(0, 50, 100)
Y2 = [LinPlotEq2(i) for i in X2]

fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.3, hspace=0.2)
fig.suptitle('Лабораторная работа 1.4.1')

unew = [26.7*i-833 for i in u]
print('данные', unew)
usmth = [27.2*i-862.4 for i in u]
print(usmth)

ax1.set_xlim([30, 100])
ax1.set_ylim([0, 1700])
ax1.set_title('')
ax1.set_xlabel('$u$ = $T^2$$x_ц$')
ax1.set_ylabel('$v$ = $a^2$')
ax1.grid(True)

ax2.set_xlim([5, 45])
ax2.set_ylim([1.45, 2])
ax2.set_title('График зависимости периода колебаний \n от расстояния подвеса', fontsize=10)
ax2.set_xlabel('расстояние подвеса $a$')
ax2.set_ylabel('период колебаний $T$')
ax2.grid(True)

ax1.plot(X1, Y1, 'k', alpha=0.5)
ax2.plot(X2, Y2, 'k', alpha=0.5)


ax1.scatter(u, v, s=8, c='r')
ax1.scatter(unew, v, c='b')  # не рисует эти точки?
ax2.scatter(a, T, s=8, c='r')

fig.set_figheight(2)
plt.show()
