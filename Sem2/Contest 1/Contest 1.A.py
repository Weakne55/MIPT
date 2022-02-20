a = int(input())
m = a
c = 0

while a != 0:
    a = int(input())
    if m < a:
        m = a
        c = 0
    if a == m:
        c += 1
print(c)
# не прошел 1 тест
