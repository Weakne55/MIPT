import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

# Данные снятые во время лабы
U1 = [0.4, 0.45, 0.813, 4.083, 81.48, 779.9]
U2 = [0.637, 0.710, 1.253, 6.141, 122.38, 1167]

U3 = [0.41, 0.81, 4.08, 8.15, 39.97, 77.9, 49, 10, 1.36]
U4 = [0.61, 1.25, 6.28, 12.55, 61.6, 120, 76, 15.6, 2.08]

U5 = [0.408, 0.816, 4.08, 8.15, 39.95, 77.8, 49.58, 10, 1.36]
U6 = [0.58, 1.23, 6.41, 18.86, 63.33, 0.123, 78.6, 16, 2.09]

U7 = [0.408, 0.816, 4.08, 8.14, 39.94, 77.7, 49.5, 10.1, 1.36]
U8 = [0.567, 1.235, 6.56, 13.2, 65.09, 126.8, 80, 16.5, 2.1]

U9 = [0.407, 4.08, 5.1, 5.82, 8.14, 20.21, 56.34, 77.7, 125]
U10 = [0.56, 6.73, 8.44, 9.66, 13.5, 33.8, 94.43, 130, 210]

U11 = [0.408, 4.08, 5.10, 8.150, 13.5, 39.9, 57.3, 77.65, 125]
U12 = [0.55, 6.89, 8.65, 13.9, 23.2, 68.7, 97, 133.8, 215.7]

temp = [22.8, 32.8, 42.8, 52.8, 62.8, 72.8]  # температура измерений

# Сопротивление проволки при Q=0
R0 = [1.55394710e+01, 1.53469311e+01, 1.41431458e+01, 1.55848214e+01, 1.61892825e+01, 1.64966462e+01]
# наклон проволки при Q=0
K = [-5.22569449e-04, 1.25736950e-04, 5.81330271e-03, 9.68274509e-04, 3.04909169e-04, 3.75441822e-04]


# Функция для линейной апроксимации
def fit_function(x, k, b):
    return k * x + b


# Функция для нахождения сопротивления нити из известных напряжений
def resistance_of_thread(U_1=list, U_2=list, color=str, T=int):
    R_thread0 = list()
    Q_thread0 = list()
    I_thread0 = list()
    for i in range(len(U_1)):
        R_thread0.append((U_2[i] * 10) / U_1[i])
        Q_thread0.append(U_2[i] * (U_1[i] / 10)*0.000001)
        I_thread0.append(U_1[i] / 100)
    print('Сопротивление при температуре ', T)
    for k in range(len(R_thread0)):
        print(R_thread0[k].__round__(2))
    print('Тепловой поток при температуре ', T)
    for k in range(len(Q_thread0)):
        print(Q_thread0[k])
    print('Ток при температуре ', T)
    for k in range(len(I_thread0)):
        print(I_thread0[k])
    print('---------------------------')
    R_thread = np.array(R_thread0, dtype=np.float64)
    Q_thread = np.array(Q_thread0, dtype=np.float64)

    beta_opt, beta_cov = optimize.curve_fit(fit_function, Q_thread, R_thread)
    print('𝑑𝑅/𝑑Q при температуре', T, 'C ', beta_opt)  #
    label = 'Апроксимация при T = ' + T + ' С'
    plt.plot(Q_thread, fit_function(Q_thread, *beta_opt), color=color, label=label)
    plt.scatter(Q_thread0, R_thread0, marker='x', color=color)


# отрисовка сопротивлений
fig, ax = plt.subplots()
ax.set_ylim(13, 18)
ax.set_xlim(-0.00025, 0.003)
resistance_of_thread(U1, U2, 'red', '22.8')
resistance_of_thread(U3, U4, 'blue', '32.8')
resistance_of_thread(U5, U6, 'green', '42.8')
resistance_of_thread(U7, U8, 'orange', '52.8')
resistance_of_thread(U9, U10, 'black', '62.8')
resistance_of_thread(U11, U12, 'cyan', '72.8')
ax.set_xlabel(r'$Q$')
ax.set_ylabel(r'$R$', fontsize=12, rotation='horizontal', x=0.0, y=0.45)
plt.legend()
plt.grid(True)
plt.show()


# Апроксимация зависимости сопротивления нити от её температуры
R0np = np.array(R0, dtype=np.float64)
tempnp = np.array(temp, dtype=np.float64)
best_R0, cov_R0 = optimize.curve_fit(fit_function, tempnp, R0np)
print('Апроксимация R(T) ', best_R0)


# alpha - температурный коэффициент сопротивления материала нити
alpha = best_R0[0]/best_R0[1]
print('alpha ', alpha)

# Отрисовка зависимости сопротивления нити от её температуры и апроксимации
fig1, ax1 = plt.subplots()
ax1.set_xlabel(r'$T$')
ax1.set_ylabel(r'$R$', fontsize=12, rotation='horizontal', x=0.0, y=0.45)
ax1.plot(temp, R0, color='red', linestyle='--')
ax1.plot(tempnp, fit_function(tempnp, *best_R0), color='blue')
plt.show()


# Вычисление наклона зависимости выделяющейся на нити мощности от её перегрева относительно стенок
dRdQ = []

for j in range(len(K)):
    dRdQ.append(0.02501316/K[j])

print('(dR/dT)/(dR/dQ) ', dRdQ)


# коэффициенты теплопроводности газа 𝜅 для каждой температуры термостата 𝑇0
coef = []

for l in range(len(dRdQ)):
    coef.append((dRdQ[l] * 5.3) / (2 * np.pi * 0.365))

#  Апроксимация коэффициентов
coefnp = np.array(coef, dtype=np.float64)
best_coef, cov_coef = optimize.curve_fit(fit_function, tempnp, coefnp)
print('коэффициенты теплопроводности', coef)


# отрисовка графика 𝜅(𝑇)
fig2, ax2 = plt.subplots()
ax2.set_xlabel(r'$T$')
ax2.set_ylabel(r'$𝜅$', fontsize=13, rotation='horizontal', x=0.0, y=0.45)
ax2.plot(temp, coef, color='red', linestyle='--')
ax2.plot(tempnp, fit_function(tempnp, *best_coef), color='blue')
plt.show()


# нахождение логарифмов 𝜅 и 𝑇
ln_coef = []
ln_T = []
for m in range(1, len(coef)):
    ln_coef.append(np.log(coef[m]))
    ln_T.append(np.log(temp[m]))
ln_coefnp = np.array(ln_coef, dtype=np.float64)
ln_Tnp = np.array(ln_T, dtype=np.float64)
best_ln_coef, cov_ln_coef = optimize.curve_fit(fit_function, ln_Tnp, ln_coefnp)
print('коэффициент бета ', best_ln_coef[0])

# отрисовка графика ln 𝜅(ln 𝑇))
fig3, ax3 = plt.subplots()
ax3.set_xlabel(r'$ln T$', fontsize=13)
ax3.set_ylabel(r'$ln 𝜅$', fontsize=13, rotation='horizontal', x=0.0, y=0.50)
ax3.plot(ln_Tnp, ln_coefnp, color='red', linestyle='--')
ax3.plot(ln_Tnp, fit_function(ln_Tnp, *best_ln_coef), color='blue')
plt.show()


