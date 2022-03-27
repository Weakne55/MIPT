def read_graph():
    G_inv = {}
    G = {}
    N = int(input())
    M = int(input())
    for j in range(M):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
            if v not in G_inv:
                G_inv[v] = []
        G_inv[v2].append(v1)
        G[v1].append(v2)
    return G, G_inv


def dfs(G, vertex, used):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used)


G, G_inv = read_graph()
used = set()
used_inv = set()
dfs(G_inv, 0, used_inv)
dfs(G, 0, used)

if used == set(G.keys()) and used_inv == set(G_inv.keys()):
    print('YES')
else:
    print('NO')




