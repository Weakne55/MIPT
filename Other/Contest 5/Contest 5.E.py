n = int(input())
a = [i+1 for i in range(1, n)]
b = []
c = []
d = []
e = []
print(a)
for j in range(2, len(a), 2):
    b.append(a[j])
print(b)
for k in range(4, len(a), 3):
    if a[k] in b:
        continue
    else:
        c.append(a[k])
print(c)
for f in range(8, len(a), 5):
    if (a[f] in c) or (a[f] in b):
        continue
    else:
        d.append(a[f])
print(d)
for s in range(12, len(a), 7):
    if (a[s] in d) or (a[s] in c) or (a[s] in b):
        continue
    else:
        e.append(a[s])
print(e)
d.extend(e)
c.extend(d)
b.extend(c)
for item in sorted(b):
    if item in a:
        a.remove(item)
print(a)
