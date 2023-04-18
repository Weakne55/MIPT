import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

# # Поле квадруполя
# v0 = 20
# dl = np.array([2.3, 2.5, 2.3, 2.4, 1.6, 1.25, 0.9, 0.8, 0.6, 0.6, 0.6, 0.7, 1.1])
# d = np.array([1.9, 1.7, 1.3, 1.1, 1, 0.8, 0.6, 0.5, 0.5, 0.5, 0.6, 0.6, 0.7])
# # E = 0.1 * v0 / d
# # print(*E, 'E_i')
# F = 0.1 * v0 * sum(dl / d) / 300
# print(round(F, 2), 'Поток напряженности эл.поля')
# q = F / 4 / np.pi
# print(round(q, 3), 'Заряд на электродах')
# C0 = q/v0*300
# print(round(C0, 5), 'межэлектродная ёмкость(на единицу длины)')

plt.figure(figsize=(7, 7))

for a in np.linspace(0.03, 1, 20):
    x = np.linspace(0.01, 10, 10**4)  # для 10**6 прямые упираются в границы
    y = ((x ** 2 - a ** 2) ** 0.5)
    if x.all() > a:
        plt.plot(x, y, 0.5, color='red', alpha=0.5)
        plt.plot(-x, y, 0.5, color='red', alpha=0.5)
        plt.plot(x, -y, 0.5, color='red', alpha=0.5)
        plt.plot(-x, -y, 0.5, color='red', alpha=0.5)
        plt.plot(y, x, 0.5, color='red', alpha=0.5)
        plt.plot(-y, x, 0.5, color='red', alpha=0.5)
        plt.plot(y, -x, 0.5, color='red', alpha=0.5)
        plt.plot(-y, -x, 0.5, color='red', alpha=0.5)
    plt.plot(x, a ** 2 / x / 2, 0.5, color='blue', alpha=0.5)
    plt.plot(-x, a ** 2 / x / 2, 0.5, color='blue', alpha=0.5)
    plt.plot(x, -a ** 2 / x / 2, 0.5, color='blue', alpha=0.5)
    plt.plot(-x, -a ** 2 / x / 2, 0.5, color='blue', alpha=0.5)
    plt.ylim((-1, 1))
    plt.xlim((-1, 1))
plt.grid()
plt.show()

# a = 8
# r = 3
# V0 = 20
# V = np.linspace(0.1, 1, 9)
# x = np.linspace(0.01, 10, 1000)
#
# y_e = (2 * x ** 2) ** 0.5
#
# plt.figure(figsize=(7, 7))
#
# for v_n in V:
#     y = (a**2)/2 * (v_n/V0) / x
#     E = 2 * V0 * y_e / (a ** 2)
#     plt.plot(x, y,color='red')
#     plt.plot(x, E,color='blue')
# plt.ylim((0, 1.6))
# plt.xlim((0, 5))
# plt.show()


# Поле квадранта провода
# quattro_dl = np.array([1.2, 0.9, 1.2, 1, 1.5, 1.3, 1.3, 1.4, 1.3, 1.2, 1.1, 1.4, 1.3, 1.4, 1.4, 1.5, 1.3, 1.3])
# quattro_d = np.array([0.7, 0.7, 0.6, 0.6, 0.6, 0.8, 0.9, 1.1, 1.3, 1.4, 1.3, 1.4, 1.3, 1.3, 1.2, 1.3, 1.3, 1.2])
#
# quattro_F = 0.1*20*sum(quattro_dl/quattro_d)
# quattro_q = quattro_F/4/np.pi
# quattro_c = quattro_q/20

# print(round(quattro_F,3),round(quattro_q,3),round(quattro_c,3))
#
#
# def line(x1, x2, y1, y2):
#     def help_line(x):
#         return (x - x1) * (y2 - y1) / (x2 - x1) + y1
#
#     return help_line
#
#
# cabel_3x = np.array(
#     [1.75, 1.75, 1.8, 1.95, 2.1, 2.2, 2.6, 3.2, 3.8, 4.7, 5.8, 7.1, 8.2, 9.6, 11, 12.9, 14.45, 15.95, 17.35, 18.7, 19.8])
# cabel_3y = np.array(
#     [0, 2, 3.3, 4.6, 5.9, 7.3, 8.85, 10.2, 11.4, 12.5, 13.55, 14.25, 14.7, 15.1, 15.4, 15.7, 15.9, 15.9, 15.95, 16, 16])
#
# cabel_4x = np.array(
#     [2.4, 2.4, 2.5, 2.6, 2.8, 2.9, 3.2, 3.7, 4.35, 5.2, 6.05, 6.9, 7.9, 9, 10.1, 11, 12, 13.3, 14.6, 15.8, 17.3])
#
# cabel_4y = np.array(
#     [0, 2.8, 4.1, 5.4, 6.5, 7.1, 8.4, 9.4, 10.4, 11.4, 12.1, 12.7, 13.1, 13.5, 13.8, 14.1, 14.3, 14.4, 14.5, 14.6, 14.8])
#
# plt.scatter(cabel_4x, cabel_4y, s=3)
# plt.scatter(cabel_3x, cabel_3y, color='r', s=3)
#
# cabel_mx = (cabel_3x + cabel_4x) / 2
# cabel_my = (cabel_3y + cabel_4y) / 2
#
# for i in range(len(cabel_mx)-1):
#     y = line(cabel_mx[i], cabel_mx[i+1], cabel_my[i], cabel_my[i+1])
#     se = np.linspace(cabel_mx[i], cabel_mx[i+1], 100)
#     plt.plot(se, y(se))
#
# plt.scatter(cabel_mx, cabel_my, color='g', s=3)
# plt.xlim(0, 19.8)
# plt.ylim(0,)
# plt.show()

# Поле конденсатора
# cap_4x = np.array(
#     [2.5, 3.4, 4.4, 5.2, 6, 6.6, 7.3, 8.2, 8.7, 9.5, 10.6, 11.2, 11.8, 12.2, 12.7, 13.1, 13.6, 13.9, 14.3, 14.8, 15.2,
#      15.7, 16.3, 17, 17.6, 18.3, 19.3, 20.1])
# cap_4y = np.array(
#     [1.5, 1.5, 1.5, 1.5, 1.6, 1.6, 1.6, 1.6, 1.5, 1.5, 1.7, 1.7, 1.9, 2, 2.2, 2.3, 2.6, 2.8, 3.1, 3.5, 4, 4.6, 5.1, 5.8,
#      6.6, 7.3, 8.2, 9.1])
#
# cap_5x = np.array(
#     [2.6, 3.4, 4.2, 4.8, 5.2, 5.7, 6.1, 6.9, 7.7, 8.5, 9.3, 10, 10.8, 11.5, 12.3, 12.8, 13.1, 13.7, 14.1, 14.5, 14.7,
#      15.1, 15.6, 16, 16.5, 16.9, 17.2, 17.7, 18.2])
# cap_5y = np.array(
#     [1.9, 1.9, 1.9, 1.9, 2, 2, 2, 2, 2, 2, 2, 2.1, 2.2, 2.5, 2.7, 2.9, 3.5, 4, 4.6, 5.2, 5.9, 7, 8.1, 9.1, 10.2, 11.3,
#      12.3])
# print(len(cap_5x), len(cap_5y))
