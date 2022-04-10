def read_graph(E):
    G = {}
    for i in range(E):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    return G


def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


V, E = map(int, input().split())
used = set()
G = read_graph(E)
dfs(0, G, used)
