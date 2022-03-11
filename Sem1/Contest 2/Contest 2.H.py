import sys

a = int(input())
l1 = []
l2 = []
s = 0

while a != 0:
    l1.append(a)
    a = int(input())

if len(l1) < 2:
    print(-1)
    sys.exit(0)

for i in range(1, len(l1)):
    if l1[i-1] % 2 != 0:
        l2.append(l1[i])

if len(l2) == 0:
    print(-1)
    sys.exit(0)

print(sum(l2))