from random import randint
# в node можно запихнуть список, размер и вообще много чего
# FIFO список


def LinkedList():  # создаём двусвязный список
    return {
        'first': None,  # с пустым первым узлом
        'last': None  # и последним
    }


def Node(value):  # создаем узёл
    return {
        'value': value,  # создаем значение узла
        'next': None,  # ссылку на следующий узел
        'prev': None,  # и на предыдущий
    }


def Put(ll, data):  # добавляем в связный список новый узел справа
    node = Node(data)  # создаем сам узел
    if ll['first'] is None:  # если связный список пуст, то
        ll['first'] = ll['last'] = node  # объявляем новый узел первым и последним
    ll['last']['next'] = node  # если двусвязный список не пуст, то делаем ссылаем последний узел, но новосозданный
    node['prev'] = ll['last']  # ссылаем новый узел, на последний в списке
    ll['last'] = node  # говорим, что последний узел в списке теперь наш новосозданный узел


def Get(ll):  # получаем значение узла из списка слева
    if ll['first'] is None:  # если список пусть
        raise IndexError('Can`t get from empty Linked list')  # вызываем ошибку
    res = ll['first']['value']  # если нет, то присваиваем переменной значение первого узла
    ll['first'] = ll['first']['next']  # делаем первым узлом второй
    return res  # возвращаем присвоенное значение


def IsEmpty(ll):  # проверяем пустой ли список
    return ll['first'] is None  # если первый элемент пустой, то возвращаем True


def printlist(ll):  # печатаем список
    el = ll['first']  # присваиваем элементу первый узел
    while el is not None:  # пока узел не пуст
        print(el['value'], end=', ')  # печатаем его значение
        el = el['next']  # присваиваем элементу следущий узел
    print()  # пустая строка для нормального вывода


def insertdata(node, data):  # вставка значения в узел - изменение узла
    if node['next'] is None:  # если следующий после выбранного узла пустой, то
        Put(ll, data)  # добавляем слева узел с новыми данными
        return
    nd = Node(data)  # создаём узел
    nd['next'] = node['next']  # присваиваем новому узлу ссылку на следующий узел выбранного узла
    node['next'] = nd  #
    node['next']['prev'] = nd  #
    nd['prev'] = node  # АААААААААААААААААААААААААААААААААААААА


def removenode(node):  # удаляём узел
    if node['prev'] is None or node['next'] is None:  # если предыдущий или следующий узел пуст
        raise ValueError('Can`t remove first and last element')  # то вызываем ошибку
    node['prev']['next'] = node['next']  # для предыдущего следующий будет следующий нынешнего
    node['next']['prev'] = node['prev']  # а предыдущий следующего будет предыдущим нынешнего


ll = LinkedList()  # создаём связный список
for _ in range(10):  # проходим по 10 узлам
    x = randint(100, 900)  # добавляем в узел случайное число
    print(x, end=', ')  # выводим его
    Put(ll, x)  # добавляем его в узел

print()  # печатаем пустую строку для нормального вывода
printlist(ll)  # выводим список

el = ll['first']  # присваиваем переменной значение первого узла
while el is not None:  # пока узел не пуст
    if el['value'] % 2:  # если его значение нечетное, то
        insertdata(el, 2)  # вставляем после него 2
    el = el['next']  # переходим к следующему узлу
printlist(ll)  # выводим список

el = ll['first']  # присваиваем переменной первый узел
while el is not None:  # пока он не пуст
    if el['value'] % 2 == 0:  # если значение узла четное, то
        try:
            removenode(el)  # попробуем его удалить
        except ValueError as e:  # если не получится вернум ошибку
            pass
    el = el['next']  # перейдём к следующему узлу
printlist(ll)  #


while not IsEmpty(ll):  #
    print(Get(ll), end=', ')  #
