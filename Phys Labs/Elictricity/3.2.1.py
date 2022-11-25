from matplotlib import pyplot as plt
from scipy import optimize
import numpy as np

# Константы
r = 12.4
pi = np.pi
ctg = lambda x: 1 / np.tan(x)
w = lambda x: 2 * pi * x
dx = 0.1
dnu = 5


# Данные
ctg_fi1 = np.array([0.031591144,
                    1.576746804,
                    1.963770144,
                    3.079352204,
                    5.62825366,
                    15.90262804,
                    5.244906518,
                    19.88770911,
                    9.918713401
                    ])
ctg_fi2 = np.array([0.138739867,
                    1.413594046,
                    3.507041247,
                    7.337538996,
                    21.48130688,
                    5.244906518,
                    5.62825366,
                    6.069925151,
                    6.584503283
                    ])
Rwl = np.array([6.99045E-06,
                6.94904E-05,
                0.00013199,
                0.00019449,
                0.00025699,
                0.00031949,
                0.00038199,
                0.00044449,
                0.00050699
                ])
wCR = np.array([0.038936,
                1.288656,
                2.538376,
                3.788096,
                5.037816,
                6.287536,
                7.537256,
                8.786976,
                10.036696
                ])

# Опыт1
nu1 = 1000
C1 = 0.5 * 10 ** (-6)
R1 = np.array([0,
               398,
               796,
               1194,
               1592,
               1990,
               2388,
               2786,
               3184,
               ])
X1 = np.array(([12.5,
                4.5,
                3.6,
                2.5,
                1.40,
                0.5,
                1.50,
                0.40,
                0.80,
                ]))
X01 = np.array([25.5,
                25,
                24,
                25,
                25,
                25,
                25,
                25,
                25
                ])

# Опыт 2

R2 = np.array([0,
               392.5,
               785,
               1177.5,
               1570,
               1962.5,
               2355,
               2747.5,
               3140,
               ])
L = 50 * 10 ** (-3)
R_l = 31.5
X2 = np.array([11.5,
               5,
               2.3,
               1.10,
               0.4,
               1.5,
               1.4,
               1.3,
               1.2,
               ])
X02 = np.array([25.2,
                25.5,
                26,
                25.5,
                27,
                25,
                25,
                25,
                25
                ])

# Опыт 3 R = 0
nu_0 = np.array([980,
                960,
                940,
                920,
                900,
                1140,
                1100,
                1060,
                1010
                ])
X3 = np.array([3.5,
               5.00,
               7.5,
               8.5,
               10,
               7.5,
               6.5,
               4,
               1.40,
               ])
X03 = np.array([25.00,
                26,
                28,
                27,
                29,
                22,
                23,
                24,
                24.5
                ])

# Опыт 4 R = 100
nu_100 = np.array([970,
                  940,
                  910,
                  1020,
                  1100,
                  1140
                  ])
X4 = np.array([1.75,
               3.5,
               5,
               1.5,
               2.6,
               4.5
               ])
X04 = np.array([27.5,
                27,
                28,
                24,
                23,
                22
                ])

# Рассчеты 1
psi1 = pi * X1 / X01
y1 = ctg(psi1)
x1 = w(nu1) * C1 * (R1 + r)
#
# # Рассчеты 2
# psi2 = pi * X2 / X02
# y2 = ctg(psi2)
# x2 = (R2 + r + R_l) / w(nu1) / L
#
# # Рассчеты 3
# rel_nu_0 = nu_0/1010
# psi_0 = X3 / X03
# # Рассчеты 4
#
# # Погрешности 1
# dpsi1 = ((dx / X1) ** 2 + (dx / X01) ** 2) ** 0.5 * psi1
# dy1 = dpsi1 / np.sin(psi1) ** 2
#
# # Погрешности 2
# dpsi2 = ((dx / X2) ** 2 + (dx / X02) ** 2) ** 0.5 * psi2
# dy2 = dpsi2 / np.sin(psi2) ** 2
#
# # Погрешности 3
# dnu_0 = ((dnu/nu_0)**2 + (dnu/1010)**2)**0.5 * rel_nu_0
# dpsi0 = ((dx/X3)**2 + (dx/X03)**2)**0.5 * psi_0
#
# # Погрешности 4
#
# Теоретическая кривая 1
R_theor = np.linspace(100, 3300, 100)
x_theor1 = w(nu1) * C1 * (R_theor)
psi_theor1 = pi / 2 - np.arctan(x_theor1)
y_theor1 = ctg(psi_theor1)
#
# # Теоретическая кривая 2
# R_theor2 = np.linspace(100, 1500, 100)
# x_theor2 = (R_theor2 + R_l) / (w(nu1) * L)
# psi_theor2 = pi / 2 - np.arctan(x_theor1)
# y_theor2 = ctg(psi_theor2)


rel_nu_0 = nu_0/1010
dnu_0 = ((dnu/nu_0)**2 + (dnu/1010)**2)**(1/2) * rel_nu_0
x_RLC_1 = X3
x_RLC_01 = X03
psi_0 = x_RLC_1 / x_RLC_01 # pppi
dpsi0 = ((dx/x_RLC_1)**2 + (dx/x_RLC_01)**2)**0.5 * psi_0
p_nu10 = np.poly1d(np.polyfit(nu_0[:6]/1010, psi_0[:6], deg=1))
p_nu11 = np.poly1d(np.polyfit(nu_0[5:]/1010, psi_0[5:], deg=1))
x_nu10 = np.linspace(0.9, 1)
x_nu11 = np.linspace(1, 1.1)
point_1 = (0.25 - p_nu10[0])/p_nu10[1]
point_2 = (0.25 - p_nu11[0])/p_nu11[1]
plt.scatter((point_1, point_2), (0.25, 0.25))
print('Delta nu_0 is ', point_2 - point_1)
print('Добротность 0: ', 1/(point_2 - point_1))
print('dQ_0 is ', ((np.mean(dnu_0)/point_1 + np.mean(dnu_0)/point_2)/(point_2 - point_1)**2))

rel_nu_100 = nu_100/1010
dnu_100 = ((dnu/nu_100)**2 + (dnu/1010)**2)**(1/2) * rel_nu_100

x_RLC_2 = X4
x_RLC_02 = X04
psi_100 = x_RLC_2 / x_RLC_02 #pppi
dpsi100 = ((dx/x_RLC_2)**2 + (dx/x_RLC_02)**2)**0.5 * psi_100
p_nu20 = np.poly1d(np.polyfit(nu_100[:7]/1010, psi_100[:7], deg=1))
p_nu21 = np.poly1d(np.polyfit(nu_100[6:]/1010, psi_100[6:], deg=1))
x_nu20 = np.linspace(0.8, 1)
x_nu21 = np.linspace(1, 1.2)
point_11 = (0.25 - p_nu20[0])/p_nu20[1]
point_21 = (0.25 - p_nu21[0])/p_nu21[1]
plt.scatter((point_11, point_21), (0.25, 0.25), color='red')
print('Delta nu_100 is ', point_21 - point_11)
print('Добротность 100: ', 1/(point_21 - point_11))
print('dQ_100 is ', ((np.mean(dnu_0)/point_11 + np.mean(dnu_0)/point_21)/(point_21 - point_11)**2))

# dy2[8:] /= 5
# dy2[-1] /= 3
# dy1[9:] /= 2
# dy1[-1] /= 2
# dy2 = np.sqrt(dy2)
# dy1 = np.sqrt(dy1)
# plt.errorbar(x1, y1, dy1, marker='*', linestyle='', label='Data')
# plt.plot(x_t1, y_t1, label='Theory', alpha=0.6)
# plt.plot(x_app1, p1(x_app1), '--', label='Approximation', alpha=0.6)

plt.errorbar(rel_nu_0, psi_0, dpsi0, dnu_0, 'b*')
plt.plot(x_nu10, p_nu10(x_nu10), 'b:', label='R = 0 Ом')
plt.plot(x_nu11, p_nu11(x_nu11), 'b:')
plt.errorbar(rel_nu_100, psi_100, dpsi100, dnu_100, 'r*')
plt.plot(x_nu20, p_nu20(x_nu20), 'r--', label='R = 100 Ом')
plt.plot(x_nu21, p_nu21(x_nu21), 'r--')
plt.plot((0.8, 1.2), (0.25, 0.25), 'g', alpha=0.6)

plt.grid()
plt.legend()
plt.xlabel('$\\nu / \\nu_0$')
plt.ylabel('$\psi, parts \: per \: \pi$')
plt.ylim(0, 0.3)
plt.xlim(0.8, 1.2)

plt.show()

print('Q theor is ', np.sqrt(L/C1) / (r + R_l))
print('Q_100 theor is ', np.sqrt(L/C1) / (r + R_l + 100))




# Линейная Аппроксимация
def fit_function(x, k, b):
    return k * x + b


beta_opt1, beta_cov1 = optimize.curve_fit(fit_function, wCR, ctg_fi1)
beta_opt2, beta_cov2 = optimize.curve_fit(fit_function, Rwl, ctg_fi2)
# Графики

# График 1
# plt.plot(wCR, fit_function(wCR, *beta_opt1),
#          color='red', linestyle='-',
#          label='Линейная аппроксимация МНК')
#
# plt.plot(x_theor1, y_theor1, label='Теоретическая кривая')
# plt.scatter(wCR, ctg_fi1, label='Экспериментальные данные')
# plt.errorbar(wCR, ctg_fi1, dy1, None, 'b*')
#
# plt.xlabel('$\omega$CR')
# plt.ylabel('ctg $\phi$ ')
# plt.legend()
#
# plt.grid()
# plt.show()

# График 2
# plt.plot(Rwl*10000, fit_function(Rwl, *beta_opt2),
#          color='red', linestyle='-',
#          label='Линейная аппроксимация МНК')
#
# plt.plot(x_theor2, y_theor2, label='Теоретическая кривая')
# plt.errorbar(Rwl*10000, ctg_fi2, dy2, None, 'b*')
# plt.scatter(Rwl*10000, ctg_fi2, label='Экспериментальные данные')
#
# plt.xlabel('R\ $\omega$L * $10^4$')
# plt.ylabel('ctg $\phi$ ')
#
# plt.legend()
# plt.grid()
# plt.show()
