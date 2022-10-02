import matplotlib.pyplot as plt
import numpy as np


def conc_calc(C0, V0, acid):
    c_list = []
    for i in range(len(acid)):
        ci = C0*V0/(V0 + acid[i])
        c_list.append(ci)
    return np.array(c_list)


acid1 = np.arange(0, 10) * 250
acid2 = np.arange(0, 13) * 100
acid3 = np.arange(0, 7) * 100

C1 = 0.1
C2 = 0.05
C3 = 0.02

V0 = 5000

pH1 = np.array([8.93, 8.57, 8.3, 8.2, 8.04, 7.9, 7.81, 7.7, 7.61, 7.52])
pH2 = np.array([8.81, 8.67, 8.47, 8.3, 8.2, 8.08, 7.98, 7.92, 7.86, 7.71, 7.64, 7.58, 7.50])
pH3 = np.array([8.74, 8.36, 8.12, 7.9, 7.76, 7.57, 7.36])
# print(acid1)
# print(conc_calc(C1, V0, acid1))

c = conc_calc(C1, V0, acid1)
c2 = conc_calc(C2, V0, acid2)
c3 = conc_calc(C3, V0, acid3)


fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(111, projection='3d')
ax.plot(c, acid1, pH1, '*', label='0.1M')
ax.plot(c2, acid2, pH2, 's', label='0.05M')

ax.plot(c3, acid3, pH3, '^', label='0.02M')

# Labelling X-Axis
ax.set_xlabel('$C_{ТРИС}, M$')


#plt.title('Зависимость pH растворов ТРИС \nот концентрации ТРИС и объема добавленного 0.1М раствора HCl')


# Labelling Y-Axis
ax.set_ylabel('$V_{HCl}, mkL$')

# Labelling Z-Axis
ax.set_zlabel('$pH$')

# for angle in range(0, 360):
#     ax.view_init(angle, 30)
#     plt.draw()
#     plt.pause(.001)
plt.legend()
plt.show()