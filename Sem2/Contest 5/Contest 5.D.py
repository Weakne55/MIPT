def read_graph():
    G = {}
    for i in range(E):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
            G[v1].append(v2)
    for j in range(V):
        if j not in G:
            G[j] = []
    return G


def dfs(vertex, p=-1):
    tin[vertex] += 1
    parent[vertex] = p
    color[vertex] = "GREY"
    for neighbour in graph[vertex]:
        if color[neighbour] == "WHITE":
            if dfs(neighbour, vertex):
                return True
        elif color[neighbour] == "GREY":  # увидели вершину из которой вышел dfs, но ещё не вернулся
            loop.append(neighbour)  # добавили начало цикла
            loop.append(vertex)  # добавили конец цикла
            return True
    tout[vertex] += 1
    color[vertex] = "BLACK"
    return False


# что требуется
# graph,dfs,tin,tout,color,parent
V, E = map(int, input().split())
graph = read_graph()
tin = [0] * V
tout = [0] * V
color = ["WHITE"] * V
parent = [-1] * V
loop = []

for v in graph:
    if dfs(v, 0):
        break

cycle = []
if loop:
    current = loop[1]
    while current != loop[0]:  # идём в обратном порядке: от последней вершины к первой
        cycle.append(current)  # добавили вершину
        current = parent[current]  # посмотрели кто её родитель
    cycle.append(loop[0])  # добавили начало цикла - первую вершину
    cycle.reverse()  # развернули список
    print(*cycle)
else:
    print('YES')

