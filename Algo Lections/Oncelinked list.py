from random import randint


def LinkedList():
    return {
        'first': None,
        'last': None
    }



def Node(value):
    return {
        'value': value,
        'next': None
    }


def Put(ll, data):
    node = Node(data)
    if ll['first'] is None:
        ll['first'] = ll['last'] = node
    ll['last']['next'] = node
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
    el =ll['first']
    while el is not None:
        print(el['value'],end=', ')
        el = el['next']
    print()



ll =LinkedList()
for _ in range(10):
    x = randint(100,900)
    print(x, end=', ')
    Put(ll,x)

print()
printlist(ll)
while not IsEmpty(ll):
    print(Get(ll), end=', ')