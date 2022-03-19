n = int(input())
a = list(map(int, input().split()))


def add_to_heap(heap: list, el):
    heap.append(el)
    shift_up(heap, len(heap) - 1)


def shift_up(heap: list, ind: int()):
    """"ind - номер последнего элемента в куче"""
    if ind == 0:
        return
    parent = (ind - 1) // 2
    if heap[parent] > heap[ind]:
        heap[parent], heap[ind] = heap[ind], heap[parent]
        shift_up(heap, parent)


h = []  # куча
for x in a:
    add_to_heap(h, x)

print(*h)