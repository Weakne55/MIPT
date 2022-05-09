# Bellman–Ford

n, m, s = map(int, input().split())

edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

dist = {i: float('+inf') for i in range(n)}
dist[s] = 0


for _ in range(n - 1):
    for x, y, weight in edges:
        if dist[x] != float('+inf') and dist[y] > dist[x] + weight:
            dist[y] = dist[x] + weight

for x, y, weight in edges:
    if dist[x] != float('+inf') and dist[y] > dist[x] + weight:
        dist[y] = float('+inf')


print(*dist.values())
