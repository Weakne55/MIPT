# ???? не проходит часть тестов

n, m, s = map(int, input().split())

edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

dist = {i: float('+inf') for i in range(n)}
dist[s] = 0

# for _ in range(n-1):
#     for x, y, w in edges:
#         dist[y] = min(dist[y], dist[x] + w)

for _ in range(n - 1):
    for x, y, weight in edges:
        if dist[x] != float('+inf') and dist[y] > dist[x] + weight:
            dist[y] = dist[x] + weight

for x, y, weight in edges:
    if dist[x] != float('+inf') and dist[y] > dist[x] + weight:
        dist[y] = float('+inf')

for i in range(len(dist)):
    if abs(dist[i]) == float('+inf'):
        dist[i] = 'UDF'

print(*dist.values())


# order, size, start = map(int, input().split())
#
# edges = []
# for _ in range(size):
#     edges.append(list(map(int, input().split())))
#
# distances = [10 ** 10] * order
# distances[start] = 0
#
# for _ in range(order - 1):
#     for v1, v2, weight in edges:
#         if (distances[v1] != 10 ** 10
#                 and
#                 distances[v2] > distances[v1] + weight
#         ):
#             distances[v2] = distances[v1] + weight
#
# for v1, v2, weight in edges:
#     if (distances[v1] != 10 ** 10
#             and
#             distances[v2] > distances[v1] + weight
#     ):
#         distances[v2] = -10 ** 10
#
# for i in range(len(distances)):
#     if (abs(distances[i]) >= 10 ** 10):
#         distances[i] = 'UDF'
#
# print(*distances)