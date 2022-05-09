def add_edge(graph, v1, v2, weight):  # добавление взвешенного ребра в граф
    if v1 not in graph:
        graph[v1] = {v2: weight}
    else:
        graph[v1][v2] = weight


def create_graph():  # функция для считывания графа
    for _ in range(size):
        v1, v2, weight = map(int, input().split())
        add_edge(graph, v1, v2, weight)
        add_edge(graph, v2, v1, weight)


def dijkstra(graph, start, distances):  # алгоритм Дейкстра под данную задачу
    queue = deque([start])
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if neigh_v not in distances:  # если вершина не посещена, то записываем вершину, из
                distances[neigh_v] = [start,  # которой пришли в нее (start) и расстояние от нее
                                      distances[cur_v][1]
                                      +
                                      graph[cur_v][neigh_v]]
                queue.append(neigh_v)  # добавляем вершину в очередь

            elif (distances[neigh_v][0] > distances[cur_v][0]  # если эта вершина уже посещена, но расстояние
                  +  # от вершины start до нее меньше записанного, то
                  graph[cur_v][neigh_v]  # изменяем значение вершины, из которой пришли
            ):  # в нее на start, а расстояние – на
                distances[neigh_v][0] = start  # расстояние от вершины start
                distances[neigh_v][1] = distances[cur_v][1] + graph[cur_v][neigh_v]
                queue.append(neigh_v)  # добавляем вершину в очередь


from collections import deque

centeres = list(map(int, input().split()))  # список главных городов (+ размеры графа)
order = centeres.pop(0)  # число городов
size = centeres.pop(0)  # число дорог

graph = dict()  # создаем граф
create_graph()

distances = dict()  # создаем список расстояний, для главных городов расстояние равно 0
for center in centeres:
    distances[center] = [center, 0]

for center in centeres:  # запускаем алгоритм Дейкстра из каждой вершины графа, соответствующей
    dijkstra(graph, center, distances)  # главному городу

for vertex in range(order):  # печатаем значение главного города для каждого города, если
    if vertex in distances:  # такого не оказалось (компонента связности без главного города), то
        print(distances[vertex][0])  # печатаем -1
    else:
        print(-1)