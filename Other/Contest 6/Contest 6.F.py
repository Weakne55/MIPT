def day_massiv_potrogat(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


def bit_sort(A):
    length = len(str(max(A)))
    rang = 10
    for i in range(length):
        B = [[] for _ in range(rang)]
        for x in A:
            figure = x // 10**i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A = A + B[k]
        day_massiv_potrogat(A)


bit_sort(list(map(int, input().split())))