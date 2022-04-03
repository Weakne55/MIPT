import matplotlib.pyplot as plt
import numpy as np


def X_err(X, U1=list, U2=list, Re=10):
    err = []
    for i in range(len(X)):
        sgm = (((U1[i] * 0.000035 + 0.005) / U1[i]) ** 2 + ((U2[i] * 0.000035 + 0.005) / U2[i]) ** 2 + (0.0005) ** 2)
        err.append(X[i] * sgm)
    return err


T = [30, 35, 40, 50, 60] #oC
T1 = [30, 35, 40, 50]

L = 0.37 #m
d0 = 0.01
d1 = 0.05*10**(-3)
pi = np.pi
Re = 10.000 #Om

R_30 = np.array([100000, 10000, 5000, 1000, 500, 100, 70, 50, 40])
R_35 = np.array([100000, 10000, 5000, 1000, 500, 100, 70, 50, 40])
R_40 = np.array([100000, 10000, 5000, 1000, 500, 100, 70, 50, 40])
R_50 = np.array([100000, 10000, 5000, 1000, 500, 100, 70, 50, 40])
R_60 = np.array([100000, 50000, 10000, 5000, 1000, 500, 100, 70, 50, 40])

U_I30 = np.array([321.39, 422.63, 534.76, 616.35]) #mV
U_I35 = np.array([321.12, 422.13, 534.93, 615.19])
U_I40 = np.array([320.71, 421.41, 532.72, 613.63])
U_I50 = np.array([320.20, 420.47, 531.19, 611.48])
U_I60 = np.array([319.29, 418.88, 528.76, 608.34])

U_U30 = np.array([480.73, 633.68, 804.71, 930.36])
U_U35 = np.array([483.65, 637.57, 811.60, 935.92])
U_U40 = np.array([487.6, 642.8, 815.8, 942.9])
U_U50 = np.array([493.5, 650.2, 825.5, 953.6])
U_U60 = np.array([503.3, 662.8, 839.8, 969.22])

I_30 = U_I30/Re/1000 #A
I_35 = U_I35/Re/1000
I_40 = U_I40/Re/1000
I_50 = U_I50/Re/1000
I_60 = U_I60/Re/1000

R_n30 = U_U30/I_30/1000 #Om
R_n35 = U_U35/I_35/1000
R_n40 = U_U40/I_40/1000
R_n50 = U_U50/I_50/1000
R_n60 = U_U60/I_60/1000

Q_30 = U_U30*I_30/1000 #Wt
Q_35 = U_U35*I_35/1000
Q_40 = U_U40*I_40/1000
Q_50 = U_U50*I_50/1000
Q_60 = U_U60*I_60/1000

Q30_err = X_err(Q_30, U_I30, U_U30)
Q35_err = X_err(Q_35, U_I35, U_U35)
Q40_err = X_err(Q_40, U_I40, U_U40)
Q50_err = X_err(Q_50, U_I50, U_U50)
Q60_err = X_err(Q_60, U_I60, U_U60)


R30_err = X_err(R_n30, U_I30, U_U30)
R35_err = X_err(R_n35, U_I35, U_U35)
R40_err = X_err(R_n40, U_I40, U_U40)
R50_err = X_err(R_n50, U_I50, U_U50)
R60_err = X_err(R_n60, U_I60, U_U60)



p1, v1 = np.polyfit(Q_30, R_n30, deg=1, cov=True)
p2, v2 = np.polyfit(Q_35, R_n35, deg=1, cov=True)
p3, v3 = np.polyfit(Q_40, R_n40, deg=1, cov=True)
p4, v4 = np.polyfit(Q_50, R_n50, deg=1, cov=True)
p5, v5 = np.polyfit(Q_60, R_n60, deg=1, cov=True)

print(p1, v1)
print(p2, v2)
print(p3, v3)
print(p4, v4)
print(p5, v5)

p1 = np.poly1d(p1)
p2 = np.poly1d(p2)
p3 = np.poly1d(p3)
p4 = np.poly1d(p4)
p5 = np.poly1d(p5)

X = np.linspace(0, 60/1000, 200)



plt.plot(X, p1(X), alpha=0.5)
plt.plot(X, p2(X), alpha=0.5)
plt.plot(X, p3(X), alpha=0.5)
plt.plot(X, p4(X), alpha=0.5)
plt.plot(X, p5(X), alpha=0.5)


plt.errorbar(Q_30, R_n30, R30_err, Q30_err, ' ', ecolor='black')
plt.errorbar(Q_35, R_n35, R35_err, Q35_err, ' ', ecolor='black')
plt.errorbar(Q_40, R_n40, R40_err, Q40_err, ' ', ecolor='black')
plt.errorbar(Q_50, R_n50, R50_err, Q50_err, ' ', ecolor='black')
plt.errorbar(Q_60, R_n60, R60_err, Q60_err, ' ', ecolor='black')



# plt.plot(Y, p2(Y))

plt.grid(which='both')
plt.xlabel('T, $^oC$')
plt.ylabel('R, Om')
plt.title('График 2. Зависимость $R_0$ от температуры')
#plt.xlim((0, 0.061))

#plt.plot(T, R0_T, '*')

plt.show()