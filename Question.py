import numpy as np

abc = np.array([[100, 200, 300, 400, 500, 550], [600, 700, 800, 900, 1000]], dtype=object)
arr = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
arr1 = [1, 2, 3, 4, 5, 6]
print(arr[0])

def transform(X, a=1):
    Y = np.ndarray(np.copy(X))
    Y[:, 1::2] = a
    # result = np.concatenate((X, b), axis=1)
    return Y


def encode(array):
    b = np.array([], dtype=int)
    c = np.array([], dtype=int)
    b = np.append(b, array[0])
    cnt = 1  # счетчик символов на единице
    for i in range(0, len(array) - 1):  # итератор проходит по всем индексам символов кроме предпоследнего
        if array[i] == array[i + 1]:  # сравниваем символ по текущему индексу со следующим
            cnt += 1  # если символы одинаковые, то увеличиваем счетчик
        else:
            c = np.append(c, cnt)  # если разные, то выводим значение счетчика
            b = np.append(b, array[i + 1])  # выводим следующий символ
            cnt = 1  # счетчик текущего символа на единице
    c = np.append(c, cnt)
    return b, c


# print(transform(abc))
print(encode(arr))
