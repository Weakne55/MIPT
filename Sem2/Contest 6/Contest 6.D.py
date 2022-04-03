#  задача проходит тесты, но решена не до конца правильно

from collections import deque

field = []
positions = []
N, M, = map(int, input().split())
for i in range(N):
    pos = list(map(int, input().split()))
    for j in range(len(pos)):
        if pos[j] == 1:
            positions.append((i, j))
    field.append(pos)

#  нужно построить такой граф, где i,j вершина ведёт в
#  1) i+1,j
#  2) i-1,j
#  3) i,  j+1
#  4) i,  j-1


#  строим граф
G = {}
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            G[(i, j)] = [(i + 1, j),  (i, j + 1)]
        elif i == 0 and 0 < j < M-1:
            G[(i, j)] = [(i + 1, j),  (i, j + 1), (i, j - 1)]
        elif i == 0 and j == M-1:
            G[(i, j)] = [(i + 1, j),  (i, j - 1)]
        elif 0 < i < N-1 and j == 0:
            G[(i, j)] = [(i + 1, j),  (i, j + 1), (i - 1, j)]
        elif 0 < i < N-1 and 0 < j < M-1:
            G[(i, j)] = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        elif 0 < i < N-1 and j == M-1:
            G[(i, j)] = [(i + 1, j),  (i, j - 1), (i - 1, j)]
        elif i == N-1 and j == 0:
            G[(i, j)] = [(i - 1, j),  (i, j + 1)]
        elif i == N-1 and 0 < j < M-1:
            G[(i, j)] = [(i - 1, j),  (i, j + 1), (i, j - 1)]
        elif i == N-1 and j == M-1:
            G[(i, j)] = [(i - 1, j),  (i, j - 1)]


def bfs(vertices=list):
    dist = [[None for k in range(M)] for _ in range(N)]
    q = deque()
    for vertex in vertices:
        dist[vertex[0]][vertex[1]] = 0
        q.append(vertex)
    while q:
        v = q.popleft()
        for apexes in G[v]:
            if dist[apexes[0]][apexes[1]] is None:
                dist[apexes[0]][apexes[1]] = dist[v[0]][v[1]] + 1
                q.append(apexes)
    for l in range(N):
        print(*dist[l])


if len(field) > 1:
    bfs(positions)
else:
    print(0)





