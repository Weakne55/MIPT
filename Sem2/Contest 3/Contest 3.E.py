S = input()
T = input()


# 91
# mod = 1000000321


def Rabin_Karp(s, t):
    occurrences = []
    # находим хэш строки S
    h = 0
    for l in range(len(s)):
        h += ord(s[l]) * (91 ** (len(s) - l - 1))
    s_h = h % 1000000321

    t_h = 0  # создаем значение полиномиальной хэш функции

    # находим хэши подстрок строки T и сравниваем их со строкой S
    for i in range(0, len(t) - len(s) + 1):
        t_compare = t[i:len(s) + i]  # получаем префикс T с длиной как у S [aa]
        if i == 0:  # если i == 0
            for j in range(len(t_compare)):  # считаем значение полиномиальной хэш функции для префикса
                t_h += ord(t_compare[j]) * (91 ** (len(t_compare) - j - 1))
            t_h %= 1000000321
            if t_h == s_h:
                occurrences.append(i)
        else:  # если i != 0  то
            t_h *= 91  # умножаем строку на p
            t_h += ord(t_compare[len(s) - 1])  # добавляем модуль элемента len(s)-1 - последнего элемента в новой
            # строке  b из ab
            t_h -= ord(t[i - 1]) * (91 ** (
                len(t_compare)))  # вычитаем модуль прошлого первого элемента умноженного на p в степени длины S
            # получаем окончательный хэш для сравнениия с хэшем строки S
            t_h %= 1000000321
            if t_h == s_h:
                occurrences.append(i)
    if not occurrences:
        print(-1)
    else:
        print(" ".join(map(str, occurrences)))


Rabin_Karp(S, T)

# это решение не проходит два теста по времени
# решение этой задачи можно посмотреть здесь
# https://github.com/Sergei-Volkov/informatics_contests/blob/master/contest_14_hashes.ipynb
