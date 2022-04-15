def read_graph(E):
    G = {}
    vertices = set()
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        if v1 not in G:
            G[v1] = {v2: w}
            vertices.add(v1)
        if v2 not in G:
            G[v2] = {v1: w}
            vertices.add(v2)
        G[v1][v2] = G[v2][v1] = w
    return G, vertices


n, m, s, f = map(int, input().split())
G, vertices = read_graph(m)
dist = {i: float('inf') for i in range(n)}
dist[s] = 0
while vertices:
    v = min(vertices, key=dist.get)
    vertices.discard(v)
    for to in G[v]:
        if dist[v] + G[v][to] < dist[to]:
            dist[to] = dist[v] + G[v][to]

v = f
segue = [f]
while v != s:
    for to in G[v]:
        if dist[v] == dist[to] + G[to][v]:
            segue.append(to)
            v = to
            break

print(*segue[::-1])