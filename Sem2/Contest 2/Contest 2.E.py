n1, n2, n3 = map(int, input().split())
m1, m2, m3 = map(int, input().split())

a = -(n1/n2)
c = -(n3/n2)
b = -(m1/m2)
d = -(m3/m2)
if a-b != 0:
    px = (d-c)/(a-b)
    py = (a*d-b*c)/(a-b)
    print(round(px), round(py))
else:
    print('NO')


# n1x + n2y + n3 = 0
# n2y = -n1x-n3
# y = -n1/n2 x - n3/n2