import matplotlib.pyplot as plt
import numpy as np

q = []
dT = [2.78, 4.57, 5.04, 5.28, 4.08]
N = [0.7509, 1.244, 1.337, 1.394, 1.094]

fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot()
ax.set_xlim([2.5, 6])
ax.set_ylim([0.6, 1.5])
ax.set_title('Лабораторная работа 2.1.1.')
ax.set_xlabel(r"$\Delta T$", fontsize=16)
ax.set_ylabel(r'$N$', fontsize=16, rotation='horizontal', x=0.0, y=0.45)
plt.scatter(dT, N, marker='.', label='Полученные значения', color='blue')

# drawing our approximate line
x = np.linspace(0, 10, 100)
y = 0.2593 * x + 0.03601
ax.plot(x, np.poly1d(np.polyfit(x, y, 1))(x), label='Апроксимационная прямая', linestyle='--', color='orange')

print(np.poly1d(np.polyfit(dT, N, 1)))

plt.grid(True)
plt.show()

#Подписать кресты порешностей
#Portrait and landscape
#Легенда не нужна если одно измерение на одном графике
#подпись к графику внизу