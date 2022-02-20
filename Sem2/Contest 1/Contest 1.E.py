N = int(input())
a = [[0]*N]*N
for i in range(N):
    a[i] = list(input().split())

for i in range(N):
    for j in range(i, N):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for i in range(N):
    print(*a[i])