import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

delta_p = [376 - 149.4, 374.2 - 149.4, 371.2 - 149.4, 369.3 - 149.4, 366.8 - 149.4, 365 - 149.4, 362.8 - 149.4]
T = [30 + 273, 35 + 273, 40 + 273, 45 + 273, 50 + 273, 55 + 273, 59.9 + 273]
delta_p_np = np.array(delta_p, dtype=np.float64)
T_np = np.array(T, dtype=np.float64)
R = 0.522


def sigma(p, r, t):

    sigma_T = []
    for i in range(len(p)):
        sigma_T.append(np.float64(p[i] * (r / 2)))
    sigma_T_np = np.array(sigma_T)

    eps = 1.7
    errors = sigma_T_np * eps / 100

    def fit_function(x, k, a0):
        return a0 + k * x

    beta_opt_sigma, beta_cov_sigma = optimize.curve_fit(fit_function, t, sigma_T_np)
    print(beta_opt_sigma)
    print(beta_cov_sigma)

    plt.figure(figsize=(12, 7))
    plt.errorbar(T, sigma_T_np, errors, 0.1, '.', label='Кресты погрешностей')
    plt.plot(t, fit_function(t, *beta_opt_sigma), color='red', label='Метод наименьших квадратов')
    plt.scatter(t, sigma_T_np, marker='o', color='blue', s=5)
    plt.ylabel('$\sigma$, дин/см')
    plt.title('Зависимость поверхностного натяжения от температуры')
    plt.xlabel('T, K')
    plt.legend()
    plt.grid()
    plt.show()

    q0 = []
    for j in range(len(sigma_T_np)):
        q0.append(-t[j] * beta_opt_sigma[0])
    q = np.array(q0, dtype=np.float64)

    beta_opt_q, beta_cov_q = optimize.curve_fit(fit_function, t, q)

    UF = np.empty(len(sigma_T_np), dtype=np.float64)
    for k in range(len(q)):
        UF[k] = sigma_T_np[k] - t[k] * beta_opt_sigma[0]

    beta_opt_UF, beta_cov_UF = optimize.curve_fit(fit_function, t, UF)

    plt.figure(figsize=(12, 7))
    plt.plot(t, fit_function(t, *beta_opt_UF), color='red', label='$ U/F = (σ-T∙ dσ/dT  )$',linestyle='dashed')
    plt.scatter(t, UF, marker='o', color='blue', s=20)
    plt.plot(t, fit_function(t, *beta_opt_q), color='black', label='$ q = -T∙ dσ/dT$')
    plt.scatter(t, q, marker='x', color='green', s=20)
    plt.legend()
    plt.grid()
    plt.show()


sigma(delta_p_np, R, T_np)
