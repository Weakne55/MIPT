import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df1 = pd.read_csv('40.8.csv')
df2 = pd.read_csv('51.9.csv')
df3 = pd.read_csv('61.2.csv')
df4 = pd.read_csv('83.8.csv')
df5 = pd.read_csv('133.6.csv')
df6 = pd.read_csv('311.6.csv')

plt.plot(df1['t (s)'], df1['V (mV)'], label='40.8,$торр$')
plt.plot(df2['t (s)'], df2['V (mV)'], label='51.9,$торр$')
plt.plot(df3['t (s)'], df3['V (mV)'], label='61.2,$торр$')
plt.plot(df4['t (s)'], df4['V (mV)'], label='83.8,$торр$')
plt.plot(df5['t (s)'], df5['V (mV)'], label='133.6,$торр$')
plt.plot(df6['t (s)'], df6['V (mV)'], label='311.6,$торр$')
plt.legend()
plt.xlim(0, 600)

plt.show()

plt.plot(df1['t (s)'], np.log(df1['V (mV)']), label='40.8,$торр$')
plt.plot(df2['t (s)'], np.log(df2['V (mV)']), label='51.9,$торр$')
plt.plot(df3['t (s)'], np.log(df3['V (mV)']), label='61.2,$торр$')
plt.plot(df4['t (s)'], np.log(df4['V (mV)']), label='83.8,$торр$')
plt.plot(df5['t (s)'], np.log(df5['V (mV)']), label='133.6,$торр$')
plt.plot(df6['t (s)'], np.log(df6['V (mV)']), label='311.6,$торр$')
plt.legend()
plt.xlim(0, 600)
plt.show()

# Dif = []
# ta = []
#
# def dif_coef(link, Dif, ta, V=420, LS = 9):
#     f = pd.read_csv(link)
#  #   plt.plot(f['t (s)'], np.log(f['V (mV)']/1000), label='$P_{\Sigma} = $'+link[:-4]+'$ торр$')
#     p, c = np.polyfit(f['t (s)'], np.log(f['V (mV)']/1000), deg=1, cov=True)
#     tau = -1 / p[0]
#     ta.append(tau)
#     p = np.poly1d(p)
#     X = np.linspace(0, f['t (s)'].tolist()[-1], 50)
#   #  plt.plot(X, p(X), '--')
#     D = V*LS / 2 / tau
#     Dif.append(D)
#     print(p)
#     print(c)
#
#
# dif_coef('40.8.csv', Dif, ta)
# dif_coef('51.9.csv', Dif, ta)
# dif_coef('61.2.csv', Dif, ta)
# dif_coef('83.8.csv', Dif, ta)
# dif_coef('133.6.csv', Dif, ta)
# dif_coef('311.6.csv', Dif, ta)
#
# P = [40.8, 51.9, 61.2, 83.8, 133.6, 311.6]
# P = np.array(P)
# epsP = 7.48/2/P
# sigt = np.array([2.615/10**11, 3.886/10**12, 5.621/10**12, 3.491/10**13, 9.176/10**13, 3.512/10**13]) ** 0.5
#
# p, c = np.polyfit(1/P, Dif, deg=1, cov=True)
# Dif = np.array(Dif)
# ta = np.array(ta)
# sigD = Dif * (0.00069 + (sigt*ta)**2)**0.5
# # plt.errorbar(1/P, Dif, sigD, epsP/P,'*')
#
# p = np.poly1d(p)
# Y = np.linspace(1/P[0], 1/P[-1], 50)
#
# plt.plot(Y, p(Y), '--')
# # plt.title('Рис. 5', loc='right')
# plt.xlabel('$1/P, торр^{-1}$')
# plt.ylabel('$D, см^2/c$')
# plt.legend()
# # plt.grid()
# #plt.xlim(0, 600)
# plt.show()