def read_graph(E):  # читаем граф
    G = {}
    vertices = set()
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        if v1 not in G:
            G[v1] = {v2: w}
            vertices.add(v1)
        if v2 not in G:
            G[v2] = {v1: w}
            vertices.add(v2)
        G[v1][v2] = G[v2][v1] = w
    return G, vertices


n, m, s, f = map(int, input().split())
G, vertices = read_graph(m)
dist = {i: float('inf') for i in range(n)}  # словарь расстояний
dist[s] = 0  # расстояние до исходной вершины
while vertices:  # пока есть вершины в множестве вершин
    v = min(vertices, key=dist.get)  # выбираем вершину до которой ближе всего идти
    vertices.discard(v)  # удаляем её из множества
    for to in G[v]:  # для её дочерних вершин
        if dist[v] + G[v][to] < dist[to]:  # если расстояние до родительской вершины + длина пути
            # будут меньше чем уже существующее расстояние до дочерней вершины
            dist[to] = dist[v] + G[v][to]  # то заменяем исходное расстояние новым

v = f  # объявляем первую вершину
segue = [f]  # создаем список - наш путь по графу
while v != s:  # пока наша вершина не равна нужной
    for to in G[v]:  # для соседних вершин
        if dist[v] == dist[to] + G[to][v]:  # если расстояние до нашей вершины равно
            # расстоянию до дочерней вершины + стоимости перехода, то
            segue.append(to)  # добавляем эту вершину в наш путь по графу
            v = to  # меняем вершину на только что добавленную
            break

print(*segue[::-1])
