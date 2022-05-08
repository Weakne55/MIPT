from collections import deque

field = []
positions = []

N, M = map(int, input().split())

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

for i in range(N):
    pos = list(input())
    for j in range(len(pos)):
        if pos[j] == 'X':
            positions.append((i, j))
    field.append(pos)

print(*field, sep='\n')

#  нужно построить такой граф, где i,j вершина ведёт в
#  1) i+1,j
#  2) i-1,j
#  3) i,  j+1
#  4) i,  j-1

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


# for elem in positions:
#     G[elem] = []

G_final = {}

for v in G:
    if v not in positions:
        if v not in G_final:
            G_final[v] = []
        for node in G[v]:
            if node not in positions:
                G_final[v].append(node)

for e in G_final:
    if G_final[e]:
        print(e, G_final[e])


def bfs(start_v):  # функция для поиска в ширину
    distances[start_v[0]][start_v[1]] = 0
    queue = deque([start_v])  # очередь для записи вершин
    while queue:
        cur_v = queue.popleft()  # текущая вершина
        for neighbour_v in G_final[cur_v]:
            # если вершина не посещена, добавляем ее в соответствующие списки
            if (distances[neighbour_v[0]][neighbour_v[1]] is None
                or  # или если обход с другой вершины дает меньшее значение, то обновляем его
                distances[cur_v[0]][cur_v[1]] + 1 < distances[neighbour_v[0]][neighbour_v[1]]
               ):
                distances[neighbour_v[0]][neighbour_v[1]] = distances[cur_v[0]][cur_v[1]] + 1
                queue.append(neighbour_v)

distances = [[None for _ in range(M)] for _ in range(N)]  # список расстояний

bfs((x2, y2))
print(distances[x1][y1])


# 5 7
# 3 5
# 1 1
# XXXXXXX
# X X   X
# X XXX X
# X   X X
# XXXXXXX