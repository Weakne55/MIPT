x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
w, h = map(int, input().split())

if (w <= (x3 - x1) or w <= (x2 - x4)) and ( h <= (y3 - y1) or h <= (y2 - y4)):
    print('Yes')
elif w <= (x2 - x1) and ( h <= (y3 - y1) or h <= (y2 - y4)):
    print('Yes')
elif h <= (y2 - y1) and (w <= (x3 - x1) or w <= (x2 - x4)):
    print('Yes')
else:
    print('No')
