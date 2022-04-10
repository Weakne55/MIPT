import operator


def read_graph(E):
    G = {}
    G_inv = {}
    for i in range(E):
        v1, v2 = map(int, input().split())
        for v in (v1, v2):
            if v not in G:
                G[v] = []
                G_inv[v] = []
        G[v1].append(v2)
        G_inv[v2].append(v1)
    return G, G_inv


def dfs(G, vertex, color, tin, tout):
    global tin_counter
    global tout_counter
    color[vertex] = 'GRAY'
    tin[vertex] += tin_counter
    tin_counter += 1
    for v in G[vertex]:
        if color[v] == 'WHITE':
            dfs(G, v, color, tin, tout)
        if color[v] == 'GRAY':
            print(vertex, 'CYCLE')
            continue
        if color[v] == 'BLACK':
            continue
    color[vertex] = 'BLACK'
    tout[vertex] += tout_counter
    tout_counter += 1


V, E = map(int, input().split())
G, G_inv = read_graph(E)
tin_counter = 1
tout_counter = 1
tin = {}
tout = {}
color = {}

for i in range(V):
    tin[i] = 0
    tout[i] = 0
    color[i] = 'WHITE'

dfs(G, 0, color, tin, tout)

sorted_values_tin = sorted(tin.items(), key=operator.itemgetter(1))
sorted_tint = {k: v for k, v in sorted_values_tin}

print(sorted_tint.keys())

sorted_values_tout = sorted(tout.items(), key=operator.itemgetter(1))
sorted_tout = {k: v for k, v in sorted_values_tout}

print(sorted_tout.keys())

# print('-----------------------------------')
#
# tin_counter = 1
# tout_counter = 1
# tin = {}
# tout = {}
# color = {}
#
# for i in range(V):
#     tin[i] = 0
#     tout[i] = 0
#     color[i] = 'WHITE'
#
# dfs(G_inv, 10, color, tin, tout)
#
# sorted_values_tin = sorted(tin.items(), key=operator.itemgetter(1))
# sorted_tint = {k: v for k, v in sorted_values_tin}
#
# print(sorted_tint.keys())
#
# sorted_values_tout = sorted(tout.items(), key=operator.itemgetter(1))
# sorted_tout = {k: v for k, v in sorted_values_tout}
#
# print(sorted_tout.keys())


# 11 13
# 0 1
# 1 2
# 2 3
# 3 1
# 2 4
# 4 5
# 5 6
# 6 4
# 5 7
# 7 8
# 8 9
# 9 7
# 8 10