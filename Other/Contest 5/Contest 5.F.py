n = int(input())


def eratosthenes(N):                 # n - число, до которого хотим найти простые числа
    sieve = list(range(N + 1))
    sieve[1] = 0                     # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
            print(i)
    sieve1 = [x for x in sieve if x != 0]
    return sieve1


for k in range(len(eratosthenes(n))):
    print(eratosthenes(n)[k], end=' ')
