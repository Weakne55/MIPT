import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def fit_function(x, k, b):
    return k * x + b


df_P2 = pd.read_csv('1_P2-.csv', sep=',')
# df_P2.plot(x='WL/nm', y='Abs')
# plt.xlabel('$Длина$ $волны, нм$')
# plt.ylabel('$D$', rotation='horizontal')
# plt.show()


columns = ['WL/nm', 'Abs']
filter_large = df_P2['WL/nm'] > 400
D_max = df_P2.loc[filter_large]['Abs'].max()

df_NAOH50 = pd.read_csv('3_NAOH50.csv')
df_NAH100 = pd.read_csv('4_NAH100.csv')
df_NAOH15 = pd.read_csv('5_NAOH15.csv')
df_NAOH20 = pd.read_csv('6_NAOH20.csv')
df_NAOH25 = pd.read_csv('7_NAOH25.csv')

orders = [df_NAOH50, df_NAH100, df_NAOH15, df_NAOH20, df_NAOH25]
k_opt = []
result_k = []
volume_naoh = [500, 1000, 1500, 2000, 2500]
naoh = np.array(volume_naoh, dtype=np.float64)
C = naoh * 0.3 / 3000
color = ['blue', 'red', 'black', 'orange', 'green']
i = 0


for data in orders:
    t = data['Time/sec'].values
    Dt = data['Abs'].values
    D0 = data.loc[0]['Abs']
    lnD = np.log(Dt)

    k = (1 / t) * np.log(D0 / Dt)
    res = k[np.logical_not(np.isnan(k))].mean()
    result_k.append(res)

    beta_opt, beta_cov = optimize.curve_fit(fit_function, t, lnD)
    # plt.plot(t, fit_function(t, *beta_opt), linestyle='--',color=color[i])
    k_opt.append(beta_opt[0])

    stroke = str(C[i]) + 'M NaOH'
    # plt.plot(t, lnD,color=color[i],alpha=0.5,label=stroke)
    i += 1


# plt.grid()
# for i in range(len(orders)):
#     t = orders[i]['Time/sec'].values
#     Dt = orders[i]['Abs'].values
    # stroke = str(C[i]) + 'M NaOH'
#     plt.plot(t, Dt, label=stroke)
# plt.xlabel('$t, с$')
# plt.ylabel('$ln(D)$')
# plt.legend()
# plt.show()

result = np.array(result_k, dtype=np.float64)

beta_opt, beta_cov = optimize.curve_fit(fit_function, np.log(C), np.log(result))
plt.plot(np.log(C), fit_function(np.log(C), *beta_opt),color='red')
plt.scatter(np.log(C), np.log(result))
plt.xlabel('$ln [OH]^-$')
plt.ylabel('$ln k$', rotation='vertical')
plt.grid()
plt.show()


n = beta_opt[0]
print(n)

beta_opt, beta_cov = optimize.curve_fit(fit_function, C, result)
plt.plot(C, fit_function(C, *beta_opt))
plt.scatter(C, result)
# plt.show()

print(beta_opt[0])
