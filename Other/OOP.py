# isinstance(object,class) проверить отношение объекта к выбранному классу
# type() проверить тип объекта - к какому классу принадлежит

#                       Работа с Атрибутами Класса
# Class.__dict__ какие атрибуты есть у класса
# getattr(Person,'name_of_attribute', 'Return_if_there_no_attribute') ->
# Выдаёт объект присвоенный атрибуту 'name_of_attribute'
# setattr(obj, name, value)
# del Class.attribute - удаляет атрибут класса
# delattr(Class,attr)

#                       Работа с Атрибутами Экземпляра класса
# У экземпляров класса можно так же смотреть атрибуты через __dict__
# можно добавлять новые атрибуты
# Каждый экземпляр класса представляет из себя пространство имён
# можно вызвать функцию через getattr(Class,'func')()
# self - ссылается на содаваемый экземпляр класса.self необходим для того, чтобы вызывать функции класса для экземпляров
# __init__(self) - инициализатор объекта класса. позволяет созданному объекту сразу иметь какие-то свойства
# __del__(self) - финализатор класса
# __new__(cls)
# cls ссылается на текущий экземпляр класса
# __new__() -> адрес нового созданного объекта
# return super().__new__(cls)
# super() - ссылка на базовый класс
# начиная с версии 3 все классы автоматически и неявно от класса object
# и из этого базового класса мы и вызываем метод __new__()
# метод super() возвращает ссылку на базовый класс object и в этом классе вызываем метод __new__()
# и этот метод __new__ запускает создание нового экземпляра класса и возвращает адрес нового созданного объекта
#
# Паттерн Singleton
# __instance которой является ссылкой на экземпляр класса


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, pwd, port):
        self.user = user
        self.pwd = pwd
        self.port = port


# Пример @classmethod, который позволяет работать только с методами класса


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    # @staticmathod методы,которые не имеют доступа ни к атрбутам класса,ни к атрибутам его экземпляров

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


# attrubite - публичное свойство (public)
# _attribute - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах) - явно не ограничивает доступ извне
# __attribute - режим доступа private (служит для обращения только внутри класса)

# интерфейсные методы - сеттеры и геттеры


from accessify import private, protected


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

    # Геттеры и сеттеры необходимы чтобы не нарушалась внутренняя логика работы алгоритма класса. И чтобы
    # взаимодействие с классом и его объектами осуществлялось только через разрешенные публичные методы и свойства

    # можно обойти ограничение на использование метода вне класса, напрямую обращаясь к нему через
    # _Point__check_value()
    # но с помощью accesify можно наложить более строгие ограничения и убрать эту возможность

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # для изменения перменных внутри класса, а не экземпляра необходимо происывать classmethod и использовать cls а
    # не self

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == 'x':
            raise ValueError("никаких иксов в программе")
        else:
            return object.__getattribute__(self, item)

    # здесь рассмотрена работа метода __getattribute__ и его возможность запрещать атрибуты

    def __setattr__(self, key, value):
        print("__setattr__")
        if key == 'z':
            raise AttributeError("никаких z в коде")
        else:
            # self.x = value неправильный вызов, так как он вызовёт рекурсию
            # self.__dict__[key] = value  правильный вызов
            return object.__setattr__(self, key, value)

    # здесь рассмотрена работа метода __setattr__, который вызывается при задании атрибута
    # его так же можно испольщовать для запрещения некоторых атрибутов

    def __getattr__(self, item):
        print("__getattr__" + item)

    # вызывается при обращении к несуществующему атрибуту экземпляра класса
    # можно при обращении к неправильному атрибуту менять поведениие программы, не выдавать ошибку, а делать что-то ещё

    def __delattr__(self, item):
        print("__delattr__" + item)
        object.__delattr__(self, item)

    # автоматически вызывается при удалении свойства item (не важно существует оно или нет)


# Паттерн моносостояния
# Общий атрибут - изменение атрибута влечёт за собой это изменение во всех классах

class ThreaData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


# Свойство property

class Man:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # @property
    # def old(self):
    #     return self.__old

    # @old.setter
    # def get_old(self, old):
    #     self.__old = old

    # @old.deleter
    # def old(self):
    #     del self.__old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)


# Класс property() имеет методы getter,setter,deleter
# Можно не явно писать, а навесить декоратор @property перед геттером

# пример создания нормального класса
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('Должен быть хоть один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('Можно использовать только буквенные символы')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Возраст должен быть числом больше 20')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight