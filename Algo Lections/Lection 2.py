def add_to_heap(heap: list, el):
    heap.append(el)
    shift_up(heap, len(heap) - 1)


def shift_up(heap: list, ind: int()):
    if ind == 0:
        return
    parent = (ind - 1) // 2
    if heap[parent] > heap[ind]:
        heap[parent], heap[ind] = heap[ind], heap[parent]
        shift_up(heap, parent)


def pop_from_heap(heap: list):
    if len(heap) == 0:
        raise IndexError('Heap is empty. Can`t get element from it')
    res = heap[0]
    el = heap.pop()
    if len(heap) > 0:
        heap[0] = el
        shift_down(heap, 0)
    return res


def shift_down(heap: list, ind: int, size=None):
    if size is None:
        size = len(heap)
    else:
        print(size, end=' ')
    m = heap[ind]
    if (2 * ind + 1 < size) and (heap[2 * ind + 1] < m):
        m = heap[2 * ind + 1]
    if (2 * ind + 2 < size) and (heap[2 * ind + 2] < m):
        m = heap[2 * ind + 2]
    if heap[ind] == m:
        return
    if heap[2 * ind + 1] == m:
        heap[ind], heap[2 * ind + 1] = heap[2 * ind + 1], heap[ind]
        shift_down(heap, 2 * ind + 1, size)
        return
    heap[ind], heap[2 * ind + 2] = heap[2 * ind + 2], heap[ind]
    shift_down(heap, 2 * ind + 2, size)


def hipify(h: list):
    for i in range((len(h) - 2) // 2, -1, -1):
        shift_down(h, i)


def heap_sort(h):
    hipify(h)
    print(h)
    for i in range(1, len(h)):
        h[0], h[-i] = h[-i], h[0]
        shift_down(h, 0, size=len(h) - i)


from random import randint

a = [randint(100, 999) for _ in range(10)]
print(a)

h = []
for x in a:
    add_to_heap(h, x)
hipify(a)

print(a)

print(h)

while len(h):
    print(pop_from_heap(h), end=', ')
