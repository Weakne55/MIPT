from collections import deque


def read_graph(E):
    G = {}
    for i in range(E):
        v1, v2, w = map(int, input().split())
        if v1 not in G:
            G[v1] = {v2: w}
        if v2 not in G:
            G[v2] = {v1: w}
        G[v1][v2] = w
        G[v2][v1] = w
    return G

# print(min(G[s], key=G[s].get))


n, m, s, f = map(int, input().split())
G = read_graph(m)
dist = {i: float('inf') for i in range(n)}
dist[s] = 0
q = deque()
q.append(s)
while q:
    v = q.popleft()
    for to in G[v]:
        if dist[v] + G[v][to] < dist[to]:
            dist[to] = dist[v] + G[v][to]
            q.append(to)

print(dist)
