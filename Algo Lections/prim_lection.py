def push(heap, start, end, weight):
    node = ({'start': start,
             'end': end,
             'weight': weight,
             'id': len(heap)})
    heap.append(node)
    shift_up(heap, node['id'])
    return node


def pop(heap):
    node = heap[0]
    heap[0] = heap[-1]
    heap[0]['id'] = 0
    heap.pop()
    if len(heap) > 0:
        shift_down(heap, 0)
    return node


def shift_up(heap, id):
    if id == 0:
        return
    parent = (id - 1) // 2
    if heap[parent]['weight'] > heap[id]['weight']:
        heap[parent], heap[id] = heap[id], heap[parent]
        heap[parent]['id'], heap[id]['id'] = heap[id]['id'], heap[parent]['id']
        shift_up(heap, parent)


def shift_down(heap, id):
    m = min([heap[id]['weight']] + [x['weight'] for x in heap[2 * id + 1:2 * id + 3]])
    if heap[id]['weight'] == m:
        return
    if heap[2 * id + 1]['weight'] == m:
        nxt = 2 * id + 1
        heap[nxt], heap[id] = heap[id], heap[nxt]
        heap[nxt]['id'], heap[id]['id'] = heap[id]['id'], heap[nxt]['id']
        shift_down(heap, nxt)
        return
    nxt = 2 * id + 2
    heap[nxt], heap[id] = heap[id], heap[nxt]
    heap[nxt]['id'], heap[id]['id'] = heap[id]['id'], heap[nxt]['id']
    shift_down(heap, nxt)


def read_graph():
    N, M = map(int, input().split())
    G = {}
    for _ in range(M):
        v1, v2, w = input().split()
        if v1 not in G:
            G[v1] = {}
        if v2 not in G:
            G[v2] = {}
        G[v1][v2] = float(w)
        G[v2][v1] = float(w)
    return G


def prim(G):
    start = None
    used = set()
    tree = []
    heap = []
    Verts = {}
    for v in G:
        if start is None:
            start = v
        Verts[v] = push(heap, 0, v, float('+inf'))
    Verts[start]['weight'] = 0
    shift_up(heap, Verts[start]['id'])

    while len(heap) != 0:
        q = pop(heap)
        used.add(q['end'])
        tree.append((q['start'], q['end'], q['weight']))
        for v in G[q['end']]:
            if v not in used:
                if Verts[v]['weight'] > G[q['end']][v]:
                    Verts[v]['start'] = q['end']
                    Verts[v]['weight'] = G[q['end']][v]
                    shift_up(heap, Verts[v]['id'])

    return tree


G = read_graph()
print(prim(G))
