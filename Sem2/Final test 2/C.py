def dfs(vertex, used, friends):
    friends[0] += 1
    used.add(vertex)
    for sosed in range(N):
        if a[vertex][sosed] == 1 and sosed not in used:
            dfs(sosed, used, friends)
        if a[sosed][vertex] == 1 and sosed not in used:
            dfs(sosed, used, friends)


N, S = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(N)]

used = set()
friends = [-1]
dfs(S, used, friends)
print(*friends)