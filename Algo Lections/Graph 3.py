from dfs import read_graph

# Выделение сильных компаонент сввязности


def invert(G):
    G_inv = {}
    for v1 in G:
        for v2 in G[v1]:
            if v1 not in G_inv:
                G_inv[v1] = []
            if v2 not in G_inv:
                G_inv[v2] = []

            G_inv[v2].append(v1)
    return G_inv


def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, stack)
    stack.append(vertex)


if __name__ == "__main__":
    G = read_graph(input())
    N = 0
    used = {}
    stack = []
    for vertex in G:
        if vertex not in used:
            dfs(G, vertex, used, stack)

    print(stack)

    used = {}
    while len(stack) != 0:
        comp = []
        vertex = stack.pop()
        if vertex not in used:
            dfs(invert(G), vertex, used, comp)
            N += 1
            print(comp)

