a = int(input())
b = int(input())
c = int(input())

s = [a, b, c]
b1 = max(s)
a1 = min(s)
s.remove(a1)
s.remove(b1)
c1 = s[0]

if a1 + c1 > b1:
    if c1**2 + a1**2 - b1**2 > 0:
        print('acute ')
    elif c1**2 + a1**2 - b1**2 == 0:
        print('right ')
    elif c1**2 + a1**2 - b1**2 < 0:
        print('obtuse')
    else:
        print('impossible')
else:
    print('impossible')