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


# Функция для линейной апроксимации
def fit_function(x, k, b):
    return k * x + b


def X_err(X, U1=list, U2=list, Re=10):
    err = []
    for i in range(len(X)):
        sgm = (((U1[i] * 0.000035 + 0.005) / U1[i]) ** 2 + ((U2[i] * 0.000035 + 0.005) / U2[i]) ** 2 + (0.0005) ** 2)
        err.append(X[i] * sgm)
    return err


def power(U, U0, color, label):
    Q = []
    R = []

    for i in range(len(U1)):
        Q.append(U[i] * U0[i] * 1000 / 10000000)
        R.append(10 * U0[i] / U[i])

    Q_np = np.array(Q, dtype=np.float64)
    R_np = np.array(R, dtype=np.float64)
    beta_opt, beta_cov = optimize.curve_fit(fit_function, Q_np, R_np)
    dRdQ.append(beta_opt[0])
    description = 'Апроксимация при T = ' + label + ' С'
    plt.plot(Q_np, fit_function(Q_np, *beta_opt), color=color, label=description)
    plt.scatter(Q, R, marker='x', color=color)
    print('---------------------------')
    print('𝑑𝑅/𝑑Q при температуре', label, 'C ', beta_opt)
    print('k', beta_cov[0][0] ** 0.5)
    print('b', beta_cov[1][1] ** 0.5)
    print('---------------------------')
    return Q_np, R_np

dRdQ = []

fig, ax = plt.subplots()
power(U1, U2, 'red', '22.8')
ax.set_xlabel(r'$Q,мВ$')
ax.set_ylabel(r'$R,Ом$', fontsize=12, rotation='horizontal', x=0.0, y=0.45)
plt.legend()
plt.grid(True)
plt.show()

fig, ax = plt.subplots()
ax.set_ylim(13, 18)
# power(U1, U2, 'red', '22.8')
power(U3, U4, 'blue', '32.8')
power(U5, U6, 'green', '42.8')
power(U7, U8, 'orange', '52.8')
power(U9, U10, 'black', '62.8')
power(U11, U12, 'cyan', '72.8')
ax.set_xlabel(r'$Q,мВ$')
ax.set_ylabel(r'$R,Ом$', fontsize=12, rotation='horizontal', x=0.0, y=0.45)
plt.legend()
plt.grid(True)
plt.show()

# print('OOOOOOOOOOO')
# print(*dRdQ)


fig, ax = plt.subplots()
R0 = [1.54369313e+01, 15.290096, 13.47755237, 15.43339944, 15.8860217, 16.24477596]
T_np = np.array(temp, dtype=np.float64)
R0_np = np.array(R0, dtype=np.float64)
beta_opt, beta_cov = optimize.curve_fit(fit_function, T_np, R0_np)
dRdT = beta_opt[0]
print('dRdT', dRdT)
print('k', beta_cov[0][0]**0.5)
print('b', beta_cov[1][1]**0.5)
plt.plot(T_np, fit_function(T_np, *beta_opt), color='blue')
plt.scatter(temp, R0, marker='x', color='red')
ax.set_xlabel(r'$T,C$')
ax.set_ylabel(r'$R,Ом$', fontsize=12, rotation='horizontal', x=0.0, y=0.45)
plt.grid(True)
plt.show()



dQdT = []
for i in range(len(dRdQ)):
    dQdT.append(dRdT/dRdQ[i])
print('dQdT')
print(*dQdT)
k = []
for j in range(len(dQdT)):
    k.append(dQdT[j]*2.312)
print('k')


k_np = np.array(k, dtype=np.float64)
beta_opt, beta_cov = optimize.curve_fit(fit_function, T_np, k_np)
print('kkkkkkkkkkkkkkkkkk')
print('k', beta_cov[0][0]**0.5)
print('b', beta_cov[1][1]**0.5)
fig, ax = plt.subplots()
plt.plot(T_np, fit_function(T_np, *beta_opt), color='blue')
plt.scatter(temp, k, marker='x', color='red')
ax.set_xlabel(r'$T,C$')
ax.set_ylabel(r'$к,Вт/(м*K)$', fontsize=12, rotation='vertical', x=0.0, y=0.45)
plt.grid(True)
plt.show()

print(k_np)
ln_k = np.log(k_np[1:])
ln_T = np.log(T_np[1:])
beta_opt, beta_cov = optimize.curve_fit(fit_function, ln_T, ln_k)
print('beta')
print(beta_opt[0])
print(beta_cov[0][0]**0.5)
fig, ax = plt.subplots()
plt.plot(ln_T, fit_function(ln_T, *beta_opt), color='blue')
plt.scatter(ln_T, ln_k, marker='x', color='red')
ax.set_xlabel(r'$ln T$')
ax.set_ylabel(r'$ln к$', fontsize=12, rotation='vertical', x=0.0, y=0.45)
plt.grid(True)
plt.show()





