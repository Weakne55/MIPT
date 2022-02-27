from random import randint
# в node можно запихнуть список, размер и вообще много чего


def LinkedList():
    return {
        'first': None,
        'last': None
    }


def Node(value):
    return {
        'value': value,
        'next': None,
        'prev': None,  # add prev element
    }


def Put(ll, data):
    node = Node(data)
    if ll['first'] is None:
        ll['first'] = ll['last'] = node
    ll['last']['next'] = node
    node['prev'] = ll['last']
    ll['last'] = node


def Get(ll):
    if ll['first'] is None:
        raise IndexError('Can`t get from empty Linked list')
    res = ll['first']['value']
    ll['first'] = ll['first']['next']
    return res


def IsEmpty(ll):
    return ll['first'] is None


def printlist(ll):
    el = ll['first']
    while el is not None:
        print(el['value'], end=', ')
        el = el['next']
    print()


def insertdata(node, data):
    if node['next'] is None:
        Put(ll, data)
        return
    nd = Node(data)
    nd['next'] = node['next']
    node['next'] = nd
    node['next']['prev'] = nd
    nd['prev'] = node


def removenode(node):
    if node['prev'] is None or node['next'] is None:
        raise ValueError('Can`t remove first and last element')
    node['prev']['next'] = node['next']
    node['next']['prev'] = node['prev']


ll = LinkedList()
for _ in range(10):
    x = randint(100, 900)
    print(x, end=', ')
    Put(ll, x)

print()
printlist(ll)

el = ll['first']
while el is not None:
    if el['value'] % 2:
        insertdata(el, 2)
    el = el['next']
printlist(ll)

el = ll['first']
while el is not None:
    if el['value'] % 2 == 0:
        try:
            removenode(el)
        except ValueError as e:
            pass
    el = el['next']
printlist(ll)


while not IsEmpty(ll):
    print(Get(ll), end=', ')
