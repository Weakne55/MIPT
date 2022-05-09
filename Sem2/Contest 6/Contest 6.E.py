from collections import deque

letters = 'abcdefgh'
numbers = '12345678'

graph = dict()
for l in letters:
    for n in numbers:
        graph[l + n] = set()


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]

        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)

        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

red, green = input().split()

distances_red = {v: None for v in graph}
distances_red[red] = 0
distances_green = {v: None for v in graph}
distances_green[green] = 0

queue_red = deque([red])
queue_green = deque([green])


def bfs(start_v, queue, distances):
    while queue:
        cur_v = queue.popleft()
        for neighbour_v in graph[cur_v]:
            if distances[neighbour_v] is None:
                distances[neighbour_v] = distances[cur_v] + 1
                queue.append(neighbour_v)


bfs(red, queue_red, distances_red)
bfs(green, queue_green, distances_green)

min_dist = []
for vertex in graph:
    if distances_green[vertex] == distances_red[vertex]:
        min_dist.append(distances_green[vertex])

if min_dist:
    print(min(min_dist))
else:
    print(-1)