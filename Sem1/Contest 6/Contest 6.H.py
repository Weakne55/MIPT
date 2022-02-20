def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


N = int(input())
a = list()
for i in range(N):
    a.append(int(input()))
b = qsort([item for item in a if item % 2 == 0])



m = 0
for k in range(len(a)):
    if a[k] % 2 == 0:
        a[k] = b[m]
        m += 1

print(*a)