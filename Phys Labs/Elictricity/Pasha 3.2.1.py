import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
ctg = lambda x: 1/np.tan(x)
w = lambda x: 2*pi*x
r = 10 # Om

dx = 0.1

nu1 = 1000 # Hz
C1 = 0.5 * 10**(-6) #Farad
R1 = np.array([0, 50, 100, 150, 200, 300, 450, 600, 1000, 2000, 3000])
x1 = np.array([2.4, 2.2, 1.9, 1.8, 1.6, 1.3, 0.9, 0.8, 0.5, 0.3, 0.2])
x01 = np.array([5, 5, 5, 5, 5, 5, 4.9, 5, 5.1, 6, 6.4])
psi1 = pi * x1 / x01
dpsi1 = ((dx/x1)*2 + (dx/x01)**2)**0.5 * psi1
y1 = ctg(psi1)
dy1 = dpsi1 / np.sin(psi1)**2
x1 = w(nu1)*C1*(R1 + r)
R_theor = np.linspace(10, 3010, 100)
x_t1 = w(nu1)*C1*(R_theor)
psi_t1 = pi/2 - np.arctan(x_t1)
y_t1 = ctg(psi_t1)
x_app1 = np.linspace(0, 9.5)
p1 = np.polyfit(x1, y1, deg=1)
p1 = np.poly1d(p1)


R2 = R1
L = 50 * 10**(-3) #Gn
R_l = 31 # Om
x2 = np.array([2.2, 2, 1.8, 1.6, 1.4, 1.1, 0.8, 0.7, 0.4, 0.3, 0.2])
x02 = np.array([4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 5.6, 6.8])
psi2 = pi * x2 / x02
dpsi2 = ((dx/x2)**2 + (dx/x02)**2)**0.5 * psi2
y2 = ctg(psi2)
dy2 = dpsi2 / np.sin(psi2)**2
x2 = (R1 + r + R_l)/w(nu1)/L
x_t2 =(R_theor+R_l)/(w(nu1)*L)
psi_t1 = pi/2 - np.arctan(x_t1)
y_t2 = ctg(psi_t1)
x_app2 = np.linspace(0, 10)
p2 = np.polyfit(x2, y2, deg=1)
p2 = np.poly1d(p2)

dnu = 5

nu_0 = np.array([950, 960, 970, 980, 990, 1010, 1020, 1040, 1060, 1080])
rel_nu_0 = nu_0/1010
dnu_0 = ((dnu/nu_0)**2 + (dnu/1010)**2)(1/2) * rel_nu_0
x_RLC_1 = np.array([1, 0.8, 0.7, 0.5, 0.3, 0, 0.3, 0.7, 0.9, 1.1])
x_RLC_01 = np.array([4.8, 4.7, 4.7, 4.6, 4.6, 5, 5, 4.8, 4.7, 4.6])
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

nu_100 = np.array([900, 940, 960, 970, 980, 990, 1010, 1020, 1040, 1060, 1080, 1100, 1120])
rel_nu_100 = nu_100/1010
dnu_100 = ((dnu/nu_100)**2 + (dnu/1010)**2)(1/2) * rel_nu_100

x_RLC_2 = np.array([0.8, 0.5, 0.4, 0.3, 0.2, 0.1, 0, 0.1, 0.2, 0.3, 0.5, 0.5, 0.7])
x_RLC_02 = np.array([5.6, 5.8, 5.8, 5.8, 5.8, 5.8, 5, 5.2, 5.1, 5, 5, 4.8, 4.7])
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