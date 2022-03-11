a = list(input())
a.append('a')
n = 1
sm = ''

for i in range(len(a)):
    if '1234567890'.find(a[i]) != -1:
        sm += a[i]
    else:
        if sm == '':
            continue
        else:
            n *= int(sm)
            sm = ''
print(n)