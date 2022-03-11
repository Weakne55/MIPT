a = int(input())
s = []
while a != 0:
    s.append(a)
    a = int(input())
print(s.count(max(s)))