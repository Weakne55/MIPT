import heapq

n, m = map(int, input().split())
graph = {i: {} for i in range(n)}
for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = w
    graph[v2][v1] = w


def dijkstra(G, start):
    heap = []
    distances = {v: float('+inf') for v in G}
    used = set()
    distances[start] = 0
    heapq.heappush(heap, (0, start))
    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        if v not in used:
            used.add(v)
            for neighbor in G[v]:
                tmp = distances[v] + G[v][neighbor]
                if distances[neighbor] > tmp:
                    heapq.heappush(heap, (tmp, neighbor))
                    distances[neighbor] = tmp
    return distances


path_sum = []
for v in graph:
    path_sum.append(sum(dijkstra(graph, v).values()))


print(path_sum.index(min(path_sum)))
