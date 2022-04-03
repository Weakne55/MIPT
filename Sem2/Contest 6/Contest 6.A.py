from collections import deque


def read_graph(V,E):
    graph = {}
    for i in range(V):
        graph[i] = []
    for j in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


n, m, s, e = map(int, input().split())
G = read_graph(n, m)
dist = [None for _ in range(n)]
dist[s] = 0
q = deque()
q.append(s)
while q:
    v = q.popleft()
    for to in G[v]:
        if dist[to] is None:
            dist[to] = dist[v] + 1
            q.append(to)
print(dist[e])


