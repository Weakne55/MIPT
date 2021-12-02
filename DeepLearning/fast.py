from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt


def grad_descent_v2(f, df, low=None, high=None, callback=None):
    """
    Реализация градиентного спуска для функций с несколькими локальным минимумами,
    но с известной окрестностью глобального минимума.
    Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param low: float — левая граница окрестности
    :param high: float — правая граница окрестности
    :param callback: callalbe -- функция логирования
    """
    difference = high - low
    diff1 = difference / 3
    diff2 = difference / 6
    low1 = low
    high1 = high-2*diff1

    low2 = low+diff1
    high2 = high-diff1

    low3 = low+2*diff1
    high3 = high

    low4 = low+diff2
    high4 = high - 3*diff2

    low5 = low+3*diff2
    high5 = high - diff2

    epsilon = 0.01
    minimals = list()
    def find_local_min(f, df, low_local, high_local, iters=5000, lr=0.05):
        #функция для нахождения минимума функции f на промежутке (low_local, high_local)
        x0 = np.random.uniform(low_local, high_local)
        x = x0
        np.linspace(f(low_local), f(high_local),1)
        for i in range(iters):
            xhelp = x
            x = x - lr*df(x)
            if xhelp-x < epsilon:
                continue
            x.np.clip()
        callback(x, f(x))

        return x
    for i in range(10):
        minimals.append(find_local_min(f, df, low1, high1, 400))

        minimals.append(find_local_min(f, df, low2, high2, 400))

        minimals.append(find_local_min(f, df, low3, high3, 400))


    best_estimate = np.argmin(minimals)
    #Найдите общий минимум по всем запускам. Возможно, вы захотите
    #использовать np.argmin

    return best_estimate

