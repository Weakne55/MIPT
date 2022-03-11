k = int(input())


def simple(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            print(i)
        else:
            i += 1
    return n


print(simple(k))