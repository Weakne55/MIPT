def read_graph(filename, oriented=False):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        if not oriented:
            G[v2].append(v1)
    return G


def dfs(G, start, used=None):
    if used is None:
        used = set()
    used.add(start)
    print(start, ' Зовёт друзей')
    for vertex in G[start]:
        if vertex not in used:
            dfs(G, vertex, used)
    print(start, ' Всех позвал')


if __name__ == "__main__":
    G = read_graph(input())
    dfs(G, 'A')
