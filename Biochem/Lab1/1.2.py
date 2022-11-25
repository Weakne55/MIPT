import matplotlib.pyplot as plt
import numpy as np

titrant = np.arange(0, 11) * 50

BuA = np.array([7.55, 7.56, 7.55, 7.55, 7.55, 7.56, 7.55, 7.55, 7.56, 7.56, 7.56])
BuB = np.array([7.68, 7.7, 7.71, 7.73, 7.74, 7.75, 7.76, 7.78, 7.79, 7.81, 7.82])
WB = np.array([7.55, 10, 10.2, 10.7, 10.9, 11, 11.1, 11.2, 11.3, 11.35, 11.4])
WA = np.array([7.56, 3.8, 3.55, 3.43, 3.3, 3.2, 3.12, 3.04, 2.97, 2.9, 2.85])

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(titrant, BuA, 'b^', label='ТРИС-HCl + HCl', color='red')
ax.plot(titrant, BuB, 'x', label='ТРИС-HCl + NaOH', color='blue')
ax.plot(titrant, WA, 'o', label='Вода + HCl', color='red')
ax.plot(titrant, WB, '*', label='Вода + NaOH', color='blue')

ax.plot(titrant, BuA, alpha=0.5, color='red')
ax.plot(titrant, BuB, alpha=0.5, color='blue')
ax.plot(titrant, WA, alpha=0.5, color='red')
ax.plot(titrant, WB, alpha=0.5, color='blue')

plt.grid()

ax.set_xlabel('$V_{HCl}$ \n $V_{NaOH}, мкл$')
ax.set_ylabel('$pH$', rotation=90)

plt.title('График 2')

plt.legend()
plt.show()
