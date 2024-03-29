from random import randint
# FIFO список


def LinkedList():  # создаем односвязный список
    return dict(first=None, last=None)



def Node(value):  # создаем узел
    return dict(value=value, next=None)


def Put(ll, data):  # функция добавления узла справа
    node = Node(data)  # создаём новый узел
    if ll['first'] is None:  # если первого узла нет, то
        ll['first'] = ll['last'] = node  # создаем новый узел, который сразу первый и последний
    ll['last']['next'] = node  # если список не пуст, то нынешний последний ссылается на новый узел
    ll['last'] = node  # новый созданный узел становится последним


def Get(ll):  # получаем первый узел
    if ll['first'] is None:  # если список пуст
        raise IndexError('Can`t get from empty Linked list')  # вызываем ошибку
    res = ll['first']['value']  # если не пуст, то присваиваем перменной значение первого узла
    ll['first'] = ll['first']['next']  # и делаем второй узел первым
    return res  # возвращаем переменную, которой присвоили значение исходного первого узла


def IsEmpty(ll):  # проверка что список пуст
    return ll['first'] is None  # возвращает True, если первого узла нет


def printlist(ll):  # вывод списка
    el = ll['first']  # присваиваем элементу первый узел
    while el is not None:  # пока элемент не пуст
        print(el['value'], end=', ')  # печатаем значение этого узла
        el = el['next']  # присваиваем элементу значение следующего узла
    print()  # печатаем строку, чтобы красиво было



ll = LinkedList()  # создаём связный список
for _ in range(10):  # делаем в нём 10 узлов
    x = randint(100, 900)  # добавляем в узел рандомное значение
    print(x, end=', ')  # печатаем это значение
    Put(ll, x)  # добавляем в связный список узел с таким значением

print()
printlist(ll)  # выводим список
while not IsEmpty(ll):  # пока первый элемент не является пустым
    print(Get(ll), end=', ')  # забираем оттуда элементы слева
