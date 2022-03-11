import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

delta_p = []
T = []
T_np = np.array(T)


def sigma(p, r):
    sigma_T = []
    for i in range(len(p)):
        sigma_T.append(np.float64(p[i]*r/2))
    sigma_T_np = np.array(sigma_T)

    def fit_function(x, k):
        return k*x

    beta_opt_sigma, beta_cov_sigma = optimize.curve_fit(fit_function, T, sigma_T_np)

    plt.figure(figsize=(12, 7))
    plt.plot(T, fit_function(T, *beta_opt_sigma), color='red', label='linear fit')
    plt.scatter(T, sigma_T_np, marker='o', color='blue', s=5)
    plt.grid()
    plt.show()

    q = np.empty(len(sigma_T_np), dtype=np.float64)
    for j in range(len(q)):
        q[j] = -T_np[j]*beta_opt_sigma[0]

    beta_opt_q, beta_cov_q = optimize.curve_fit(fit_function, T, q)

    plt.figure(figsize=(12, 7))
    plt.plot(T, fit_function(T, *beta_opt_q), color='red', label='linear fit')
    plt.scatter(T, q, marker='o', color='blue', s=5)
    plt.grid()
    plt.show()

    UF = np.empty(len(sigma_T_np), dtype=np.float64)
    for k in range(len(q)):
        UF[k] = sigma_T_np[k] - T_np[k] * beta_opt_sigma[0]

    beta_opt_UF, beta_cov_UF = optimize.curve_fit(fit_function, T, UF)

    plt.figure(figsize=(12, 7))
    plt.plot(T, fit_function(T, *beta_opt_UF), color='red', label='linear fit')
    plt.scatter(T, UF, marker='o', color='blue', s=5)
    plt.grid()
    plt.show()


sigma(delta_p, T_np)

