def levensteinInstruction(s1, s2, InsertCost, DeleteCost, ReplaceCost):
    def m(a, b):
        if a == b:
            return 0
        else:
            return 1

    N = len(s1)
    M = len(s2)
    D = [[0] * (M + 1) for i in range(N + 1)]
    for i in range(N + 1):
        for j in range(M + 1):
            if i == j == 0:
                D[i][j] = 0
            elif i == 0 and j > 0:
                D[i][j] = j * InsertCost
            elif i > 0 and j == 0:
                D[i][j] = i * DeleteCost
            else:
                D[i][j] += min(D[i - 1][j] + DeleteCost, D[i][j - 1] + InsertCost, D[i - 1][j - 1] + ReplaceCost * m(s1[i - 1], s2[j - 1]))

    return D[-1][-1]


a, b, c = map(int, input().split())
s11 = input()
s22 = input()
D = levensteinInstruction(s11, s22, a, b, c)
print(D)
