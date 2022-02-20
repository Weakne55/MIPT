n = int(input())


def slg(N):
    arr = list()
    if N % 2 == 0:
        arr.append(N//2)
        arr.append(N//2 - 1)
        arr.append(1)
    else:
        arr.append((N-1)//2+1)
        arr.append(1)
        arr.append((N-1)//2-1)
    sm = 0
    for elem in arr:
        if arr.count(elem) == 2 or elem == 0:
            sm += 1
    if sm != 0:
        print(-1)
    else:
        print(*arr)

slg(n)