Counter = dict()
a = int(input())  # длина массива
for i in range(a):
    b = int(input())
    if b not in Counter:
        Counter[b] = 1
    else:
        Counter[b] += 1

m = max(Counter.values())
for keys in Counter.keys():
    if m == Counter[keys]:
        print(keys)
