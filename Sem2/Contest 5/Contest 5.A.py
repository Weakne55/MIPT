n = int(input())
S = [[int(x) for x in input().split()] for _ in range(n)]


def Sim(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != M[j][i] or M[i][i] != 0:
                return print('NO')
    return print('YES')

Sim(S)