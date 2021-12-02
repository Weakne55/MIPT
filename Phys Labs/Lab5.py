import matplotlib.pyplot as plt
import numpy as np

# значения гамма параллелепипеда
l = 0.210
m = 0.185
n = 0.296

#
a = m/l
b = n/l

# получаем массив x-ов
X = np.linspace(-l, l, 100)

Y = (l**2 - X**2) ** (0.5)*a
mY = -1*Y

# Z = (l**2 - X**2) ** (0.5)*b
# mZ = -1*Z


sp = plt.axes()
# sp.spines['left'].set_position('center')
# sp.spines['bottom'].set_position('center')
plt.ylim([-0.5, 0.5])
plt.xlim([-0.5, 0.5])


plt.plot(X, Y, color='k')
plt.plot(X, mY, color='k')
# plt.plot(X, Z, color='red')
# plt.plot(X, mZ, color='red')


plt.show()
