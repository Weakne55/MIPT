# import matplotlib.pyplot as plt

N = int(input())
X = []
Y = []
for i in range(N):
    a, b = map(float, input().split())
    X.append(a)
    Y.append(b)

x0, y0 = map(float, input().split())


def inPolygon(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and
                (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
            c = 1 - c
    return 'YES' if c else 'NO'

ghm = 0

for j in range(N):
    if x0 == X[j] and y0 == Y[j]:
        ghm += 1

if ghm == 1:
    print('YES')

else:
    print(inPolygon(x0, y0, X, Y))

