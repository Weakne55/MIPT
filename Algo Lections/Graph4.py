from collections import deque


def read_graph():
    G_inv = {}
    G = {}
    N = int(input())
    M = int(input())
    for j in range(M):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
            if v not in G_inv:
                G_inv[v] = []
        G_inv[v2].append(v1)
        G[v1].append(v2)
    print(G)
    print(G_inv)
    return G, G_inv


def bfs(G, start):
    d = deque()
    d.append(start)
    used = set()
    while len(d) != 0:
        vert = d.popleft()
        if vert in used:
            continue
        used.add(vert)
        print(vert, 'Горит')
        for v in G[vert]:
            if v not in used:
                d.append(v)


if __name__ == "__main__":
    G = read_graph()[0]
    N = 0
    bfs(G, 0)
    used = set()
    for v in G:
        if v not in used:
            bfs(G, v, used)
            N += 1
    print(N)
