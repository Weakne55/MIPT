def add_edge(graph, v1, v2, weight):  # функция для добавления вершины в граф с учетом четности
    if (v1, 0) not in graph:
        graph[(v1, 0)] = {(v2, 1): weight}
        graph[(v1, 1)] = {(v2, 0): weight}
    else:
        graph[(v1, 0)][(v2, 1)] = weight
        graph[(v1, 1)][(v2, 0)] = weight


def create_graph():  # функция для создания графа
    for _ in range(size):
        v1, v2, weight = map(int, input().split())
        add_edge(graph, v1, v2, weight)
        add_edge(graph, v2, v1, weight)


def dijkstra(graph, start):  # стандартный алгоритм Дейкстра
    queue = deque([start])
    distances = dict()
    distances[start] = 0
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if (neigh_v not in distances
                    or
                    distances[cur_v] + graph[cur_v][neigh_v] < distances[neigh_v]
            ):
                distances[neigh_v] = distances[cur_v] + graph[cur_v][neigh_v]
                queue.append(neigh_v)
    return distances


def min_path(graph, start, finish):  # функция для вывода минимального пути из точки
    distances = dijkstra(graph, start)  # start в точку finish
    if finish not in distances:  # если конечная точка не в списке расстояний,
        return [(-1, 0)]  # то возвращаем специальное значение (не существует такого пути)
    cur_v = finish
    min_path = [finish]
    while cur_v != start:
        for neigh_v in graph[cur_v]:
            if distances[cur_v] == distances[neigh_v] + graph[neigh_v][cur_v]:
                min_path.append(neigh_v)
                cur_v = neigh_v
                break
    return min_path[::-1]


from collections import deque

order, size = map(int, input().split())  # размеры графа
graph = dict()
create_graph()

pairs = int(input())  # пары точек (start, finish), для которых нужна проверка,
dots = []  # существует ли между ними путь с четным числом ребер
for _ in range(pairs):
    dots.append(tuple(map(int, input().split())))

for i in range(pairs):  # считаем минимальный путь между точками, присвоив им одинаковую четность
    path = min_path(graph,
                    (dots[i][0], 0),
                    (dots[i][1], 0))
    print(*[dot[0] for dot in path])