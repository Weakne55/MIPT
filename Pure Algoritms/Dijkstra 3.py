from queue import Queue
import heapq


def read_graph(E):
    G = {}
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        if v1 not in G:
            G[v1] = {v2: w}
        if v2 not in G:
            G[v2] = {v1: w}
        G[v1][v2] = G[v2][v1] = w
    return G


def dejkstra(G, start):
    heap = []
    distances = {v: float('+inf') for v in G}

    distances[start] = 0

    heapq.heappush(heap, (0, start))
    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        for neighbor in G[v]:
            tmp = distances[v] + G[v][neighbor]
            if distances[neighbor] > tmp:
                heapq.heappush(heap, (tmp, neighbor))
                distances[neighbor] = tmp
    return distances


n, m, s, f = map(int, input().split())
G = read_graph(m)
print(dejkstra(G, 0))
