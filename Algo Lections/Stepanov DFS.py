N, M = map(int, input().split())


def read_graph():
    G = {}
    for j in range(M):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    for i in range(N):
        if i not in G:
            G[i] = []
    return G


def dfs(v,graph,stack,color):
    color[v] = "GREY"
    for vertex in graph[v]:
        if color[vertex] == "BLACK":
            continue
        elif color[vertex] == "GREY":
            loop.append(vertex)
            loop.append(v)
            continue
        elif color[vertex] == "WHITE":
            stack[vertex] = v
            if dfs(vertex, graph, stack, color):
                return True
    color[v] = "BLACK"
    return False


graph = read_graph()  # список вершин в которых есть ребро из v
color = ["WHITE"]*N  # список цветов
parent = [-1]*N  # список родителей
cycle = []
loop = []

for vertex in graph:
    if dfs(vertex, graph, parent, color):
        break

cycle = []
if loop:
    current = loop[1]
    while current != loop[0]:
        cycle.append(current)
        current = parent[current]
    cycle.append(loop[0])
    cycle.reverse()
    print(*cycle)
else:
    print('YES')