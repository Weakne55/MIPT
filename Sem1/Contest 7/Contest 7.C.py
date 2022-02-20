k = int(input())
m = int(input())


def ledder(K, M):
    n = K + M - 1

    def led(L, N):
        if L == N:
            return L
        else:
            return 2*L + led(L+1, N)

    return led(K, n)


print(ledder(k, m))

