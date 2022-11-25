def create(namespace, parent):
    scopes[namespace] = {'parent':parent,'variables':set()}


def add(namespace, var):
    scopes[namespace]['variables'].add(var)


def get(namespace, var):
    if namespace == None:
        print(None)
        return
    if var in scopes[namespace]['variables']:
        print(namespace)
        return
    else:
         get(scopes[namespace]['parent'],var)

scopes = {'global':{'parent':None,'variables':set()}}

n = int(input())

for i in range(n):

    command, name, v = input().split()

    if command == 'create':
        create(name, v)

    elif command == 'add':
        add(name, v)    

    elif command == 'get':
        get(name, v)


