dct = {'a':1,'b':2,'c':3}

dt = {dct[x]: x for x in dct}
d = dict(zip(dct.values(), dct.keys()))


a = [x*x for x in range(50) if x*x % 10 == 1]
print(a)


