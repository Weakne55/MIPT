def swtich(a, b):
    a,b = b,a
    return a,b

a, b = map(int, input().split())
print(a, b)
a,b = swtich(a, b)
print(a, b)