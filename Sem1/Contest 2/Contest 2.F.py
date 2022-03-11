import sys

a = b = int(input())
i = 0

if a == 0:
    sys.exit(0)

while a % 2 == 0:
    i += 1
    a //= 2

if 2**i == b:
    print('YES')
else:
    print('NO')