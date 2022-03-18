# N, M = map(int, input().split())

# names = []
# G = [[0] * N for _ in range(N)]
#
# # матрица смежности
# for _ in range(M):
#     v1, v2 = input().split()
#     for v in (v1, v2):
#         if v not in names:
#             names.append(v)
#     v1_index = names.index(v1)
#     v2_index = names.index(v2)
#     G[v1_index][v2_index] = 1
#     G[v2_index][v1_index] = 1
#
# # print(' ', *names)
# # for i, n in enumerate(names):
# #     print(n, *G[i])
#
#
# # вывод соседей
# for i, n in enumerate(names):
#     print(n, ':',
#           G[i].count(1),
#           [names[j] for j in range(N) if G[i][j] == 1])
#
# # граф через словарь


# # создание графа через словарь
# G = {}
# for _ in range(M):
#     v1, v2 = input().split()
#     for v in (v1, v2):
#         if v not in G:
#             G[v] = []
#     G[v1].append(v2)
#     G[v2].append(v1)
#
# for vert in G:
#     print(
#         vert, ':',
#         len(G[vert]),
#         G[vert]
#     )
def ind(name):
    return ord(name) - ord('A')


def name(ind):
    return chr(ord('A') + ind)

# for a in 'ABCDEFG':
#     print(a,':', ind(a), end='; ')
# for _ in range(10):
#     print(a,':', name(a), end='; ')


N,M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    v1,v2 = input().split()
    G[ind(v1)].append((ind(v2)))
    G[ind(v2)].append((ind(v1)))

# for i in range(N):
#     print(
#         name(i),':',
#         len(G[i]),
#         [name(j) for j in G[i]]
#     )

offset = [0]
edges = []
for edg in G:
    for e in edg:
        edges.append(e)
    offset.append(len(edges))

print(offset)
print(edges)

# выводим соседей
for i in range(N):
    print(
        name(i),':',
        offset[i+1] - offset[i],
        [name(j) for j in edges[offset[i]:offset[i+1]]]
    )