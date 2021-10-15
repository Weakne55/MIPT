k = int(input())

def check(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
    else:
        return True


def simple(n):
    cout = 1
    N = 2
    while cout <= n:
        if check(N):
            cout += 1
            N += 1
        else:
            N += 1
    return N-1


print(simple(k))