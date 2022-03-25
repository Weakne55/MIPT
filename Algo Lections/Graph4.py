from dfs import read_graph
from collections import deque


def bfs(G, start):
    d = deque()
    d.append(start)
    used = {}
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
    G = read_graph(input())
    N = 0
    bfs(G, 'A')
    used = set()
    for v in G:
        if v not in used:
            bfs(G, v, used)
            N += 1
    print(N)
