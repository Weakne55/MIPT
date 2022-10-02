import matplotlib.pyplot as plt
import numpy as np


def conc_calc(C0, V0, acid):
    c_list = []
    for i in range(len(acid)):
        ci = C0 * V0 / (V0 + acid[i])
        c_list.append(ci)
    return np.array(c_list)


titrant = np.arange(0, 11) * 50

C1 = 0.1
C2 = 0.05
C3 = 0.02

V0 = 5000

BuA = np.array([7.55, 7.56, 7.55, 7.55, 7.55, 7.56, 7.55, 7.55, 7.56, 7.56, 7.56])
BuB = np.array([7.68, 7.7, 7.71, 7.73, 7.74, 7.75, 7.76, 7.78, 7.79, 7.81, 7.82])
WB = np.array([7.55, 10, 10.2, 10.7, 10.9, 11, 11.1, 11.2, 11.3, 11.35, 11.4])
WA = np.array([7.56, 3.8, 3.55, 3.43, 3.3, 3.2, 3.12, 3.04, 2.97, 2.9, 2.85])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(titrant, BuA, 'b^', label='Buffer + HCl')
ax.plot(titrant * (-1), BuB, 'ro', label='Buffer + NaOH')
ax.plot(titrant, WA, 'b<', label='Water + HCl')
ax.plot(titrant * (-1), WB, 'rx', label='Water + NaOH')

ax.plot(titrant, BuA, '--')
ax.plot(titrant * (-1), BuB, '--')
ax.plot(titrant, WA, '--')
ax.plot(titrant * (-1), WB, '--')

plt.grid()

# Labelling X-Axis
ax.set_xlabel('$V_{HCl} / -V_{NaOH}, mkL$')

# plt.title('Зависимость pH растворов ТРИС \nот концентрации ТРИС и объема добавленного 0.1М раствора HCl')


# Labelling Y-Axis
ax.set_ylabel('$pH$')

# Labelling Z-Axis
# ax.set_zlabel('$pH$')

# for angle in range(0, 360):
#     ax.view_init(angle, 30)
#     plt.draw()
#     plt.pause(.001)
plt.legend()
plt.show()
