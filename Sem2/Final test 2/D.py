def dfs(num, used, g):
    global sum
    used[num] = 1
    for cell in g[num]:
        sum += cell[1]
        if used[cell[0]] == 0:
            dfs(cell[0], used, g)
n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    g[u].append([v, c])
    g[v].append([u, c])
used = [0 for i in range(n)] 
answer = [] 
for i in range(len(used)):
    if used[i] == 0:
        sum = 0
        dfs(i, used, g)
        answer.append(sum // 2) 
answer.sort()
for num in answer:
    print(num)