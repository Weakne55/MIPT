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


def check(G):

    def dfs_loop(G, vertex, p=-1):
        parent[vertex] = p
        color[vertex] = "GREY"
        for neighbour in G[vertex]:
            if color[neighbour] == "WHITE":
                if dfs_loop(G, neighbour, vertex):
                    return True
            elif color[neighbour] == "GREY":  # увидели вершину из которой вышел dfs, но ещё не вернулся
                loop.append(neighbour)  # добавили начало цикла
                loop.append(vertex)  # добавили конец цикла
                return True
        color[vertex] = "BLACK"
        return False

    loop = []
    for v in G:
        if dfs_loop(G,v):
            break
    # проверяем на ацикличность

    if loop:
        return True
    else:
        return False


def dfs(vertex):
    color[vertex] = "GREY"
    for neighbour in graph[vertex]:
        if color[neighbour] == "WHITE":
            dfs(neighbour)
    color[vertex] = "BLACK"
    order.append(vertex)
    return


# что требуется
# graph,dfs,tin,tout,color,parent
V, E = map(int, input().split())
graph = read_graph()
color = ["WHITE"] * V
parent = [-1] * V

order = []
if check(graph):
    print("NO")
else:
    color = ["WHITE"] * V
    for v in graph:
        if color[v] == "WHITE":
            dfs(v)
    print(*order[::-1])



