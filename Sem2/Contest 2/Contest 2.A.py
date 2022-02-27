import math
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
if r1+r2 >= r and r+r1 >= r2 and r+r2 >= r1:
    print('YES')
else:
    print('NO')