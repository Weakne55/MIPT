sx, sy = map(int, input().split())
sobx, soby = map(int, input().split())
n = int(input())
holes = []
for n in range(n):
    a, b = map(int, input().split())
    holes.append(a), holes.append(b)


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def probability(sx,sy,sobx,soby,holes=list):
    for i in range(0, len(holes) - 1, 2):
        if distance(sx, sy, holes[i], holes[i + 1]) < distance(sobx, soby, holes[i], holes[i + 1])/2:
            print(int(i/2+1))
            return
    print(-1)


probability(sx,sy,sobx,soby,holes)