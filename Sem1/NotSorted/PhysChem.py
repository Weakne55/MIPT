import matplotlib.pyplot as plt
import numpy as np

percentage = [0.03, 0.06, 0.1, 0.15, 0.21, 0.35, 0.55, 0.73, 0.8, 0.87, 1.0]
E900 = [65.7, 42.1, 23.2, 12.8, 5.7, 3.0, 3.0, 3.0, 3.0, 3.0, 0.0]
E1050 = [95.1, 67.3, 44.9, 31.8, 20.5, 9.5, 4.2, 4.2, 4.3, 3.9, 0.0]
E1200 = [124.6, 95.6, 66.7, 50.8, 35.3, 21.0, 10.9, 6.4, 5.6, 4.7, 0.0]


def Ni_Au(E, T):
    degree = (-2*96.465*E)/(8.314*T)
    print(degree)
    act = np.exp(degree)
    print(act)
    return act


activity900 = [Ni_Au(j, 900) for j in E900]
activity1050 = [Ni_Au(j, 1050) for j in E1050]
activity1200 = [Ni_Au(j, 1200) for j in E1200]



plt.scatter(percentage, activity900, c='r')
plt.scatter(percentage, activity1050, c='b')
plt.scatter(percentage, activity1200, c='k')


p1 = np.polyfit(percentage, activity900, 9)
LinPlotEq1 = np.poly1d(p1)
X1 = np.linspace(0, 1, 50)
Y1 = [LinPlotEq1(i) for i in X1]

p2 = np.polyfit(percentage, activity1050, 9)
LinPlotEq2 = np.poly1d(p2)
X2 = np.linspace(0, 1, 50)
Y2 = [LinPlotEq2(i) for i in X2]

p3 = np.polyfit(percentage, activity1200, 9)
LinPlotEq3 = np.poly1d(p3)
X3 = np.linspace(0, 1, 50)
Y3 = [LinPlotEq3(i) for i in X3]


plt.plot(X1, Y1, 'r', alpha=0.5)
plt.plot(X2, Y2, 'b', alpha=0.5)
plt.plot(X3, Y3, 'k', alpha=0.5)


plt.xlim(0, 1)
# plt.ylim(0, 150)

plt.show()
