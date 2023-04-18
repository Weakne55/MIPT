class Node:
    s = ['A', 'T', 'G', 'C']  # alphabet

    def __init__(self):
        self.next = [None] * 4
        self.value = None

root = Node()


def add(S):
    cur = root
    for c in S:
        if cur.next[c] is None:
            cur.next[c] = Node()
        cur = cur.next[c]
    cur.value = True


def get(S):
    cur = root
    for c in S:
        if cur.next[c] is None:
            return None
        cur = cur.next[c]
    return cur.value


add('ATTGCTAC')
get('ATTGCTAC')
#ATTGCTAC