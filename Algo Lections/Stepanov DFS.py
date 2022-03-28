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
            dfs(neighbour, vertex)
        elif color[neighbour] == "GREY":
            print("CYCLE")
    tout[vertex] += 1
    print(vertex, end=' ')
    color[vertex] = "BLACK"
    return


# что требуется
# graph,dfs,tin,tout,color,parent
V, E = map(int, input().split())
graph = read_graph()
tin = [0] * V
tout = [0] * V
color = ["WHITE"] * V
parent = [-1] * V

for v in graph:
    if tin[v] == 0:
        dfs(v)
print(tout)