from collections import deque


def read_graph(V, E):
    graph = {}
    for i in range(V):
        graph[i] = []
    for j in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    return graph


n, m, = map(int, input().split())
g = read_graph(n, m)


def bfs(G, vertex):
    dist = [None for _ in range(len(G))]
    parents = [None for _ in range(len(G))]
    dist[vertex] = 0
    q = deque()
    q.append(vertex)
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] is None:
                dist[to] = dist[v] + 1
                parents[to] = v
                q.append(to)
            elif to == vertex:
                loop = [v]  # конец цикла
                prev = parents[v]
                while prev is not None:
                    loop.append(prev)
                    prev = parents[prev]
                return loop[::-1]
    return []


cycles = []
for v in g:
    cycle = bfs(g, v)
    if cycle:
        cycles.append(cycle)

if not cycles:
    print('NO CYCLES')
else:
    cycles.sort(key=len)
    print(*cycles[0])