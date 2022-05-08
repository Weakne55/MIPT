N = int(input())
G_in = {i: [] for i in range(N)}
G_out = {j: [] for j in range(N)}
S = [[int(x) for x in input().split()] for _ in range(N)]


for i in range(len(S)):
    for j in range(len(S[i])):
        if S[i][j] != 0:
            G_out[i].append(j)
            G_in[j].append(i)


for k in range(N):
    if not G_in[k]:
        print(k+1, end=' ')

print()

for m in range(N):
    if not G_out[m]:
        print(m+1, end=' ')




