import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def approximate_function(link=str, E_eq=0, color_dots=None, color_curve=None, marker_dots='.', lab=None, method='lm', sign='+'):
    """"link должна иметь вид С:\home\lab\measure1.txt"""
    with open(link, 'r') as file:
        lines = file.readlines()[6:]
    t0 = list()
    E0 = list()
    I0 = list()
    for l in lines:
        t0.append(np.float64(l.split()[0]))
        E0.append(np.float64(l.split()[1]))
        I0.append(np.float64(l.split()[2]))
    t = np.array(t0)
    e = np.array(E0) - E_eq
    I = np.array(I0)

    def fit_function1(x, b, k):
        return - b*np.exp(-k * x) + b

    def fit_function2(x, b, k):
        return b*np.exp(k * x) - b

    if sign == '-':
        beta_opt, beta_cov = optimize.curve_fit(fit_function2, e, I, method=method)
        plt.plot(e, fit_function2(e, *beta_opt), color=color_curve, label=lab)
        plt.scatter(e, I, marker=marker_dots, color=color_dots, s=3, alpha=0.6)
        print(beta_opt)
        return beta_opt, beta_cov

    beta_opt, beta_cov = optimize.curve_fit(fit_function1, e, I, method=method)
    plt.plot(e, fit_function1(e, *beta_opt), color=color_curve, label=lab)
    plt.scatter(e, I, marker=marker_dots, color=color_dots, s=3, alpha=0.4)
    return beta_opt, beta_cov


fig, ax = plt.subplots()
opt1, cov1 = approximate_function('11.3 эл-ды/11.3-400_1.txt', 256.59, 'blue', 'blue', lab='$V(K_3[Fe(CN)_6]) = 1 ml$', method='trf', sign='-')
opt2, cov2 = approximate_function('11.3 эл-ды/11.3-400_2.txt', 281.85, 'black', 'black', lab='$V(K_3[Fe(CN)_6]) = 3 ml$', sign='-')
opt3, cov3 = approximate_function('11.3 эл-ды/11.3-400_3.txt', 294.01, 'red', 'red', lab='$V(K_3[Fe(CN)_6]) = 5 ml', sign='-')
opt4, cov4 = approximate_function('11.3 эл-ды/11.3-400_4.txt', 301.15, 'green', 'green', lab='$V(K_3[Fe(CN)_6]) = 7 ml$', sign='-')
opt5, cov5 = approximate_function('11.3 эл-ды/11.3-400_5.txt', 306.41, 'purple', 'purple', lab='$V(K_3[Fe(CN)_6]) = 9 ml$', sign='-')
opt51, cov51 = approximate_function('11.3 эл-ды/11.3-400_5+rate.txt', 306.35, 'grey', 'grey', lab='$V(K_3[Fe(CN)_6]) = 9 ml + rate$', sign='-')
opt10, cov10 = approximate_function('11.3 эл-ды/11.3+400_1.txt', 256.94, 'blue', 'blue', lab='$V(K_3[Fe(CN)_6]) = 1 ml$', method='trf')
opt20, cov20 = approximate_function('11.3 эл-ды/11.3+400_2.txt', 280.68, 'black', 'black', lab='$V(K_3[Fe(CN)_6]) = 3 ml$')
opt30, cov30 = approximate_function('11.3 эл-ды/11.3+400_3.txt', 293.55, 'red', 'red', lab='$V(K_3[Fe(CN)_6]) = 1 ml$')
opt40, cov40 = approximate_function('11.3 эл-ды/11.3+400_4.txt', 299.98, 'green', 'green', lab='$V(K_3[Fe(CN)_6]) = 1 ml$')
opt50, cov50 = approximate_function('11.3 эл-ды/11.3+400_5.txt', 306.41, 'purple', 'purple', lab='$V(K_3[Fe(CN)_6]) = 1 ml$')




plt.grid()
plt.ylim((-23, 3))
plt.xlim((-400, 400))
#plt.legend(ncol=2, fontsize=10)
plt.title('Рис. 6', loc='right')
plt.xlabel('$E, mV$')
plt.ylabel('$I, mkA')
plt.show()


