n = int(input())
x = 0
y = 0
for _ in range(n):
    s = input().split()
    if s[0] == 'север':
        y += int(s[1])
    elif s[0] == 'юг':
        y -= int(s[1])
    elif s[0] == 'запад':
        x -= int(s[1])
    elif s[0] == 'восток':
        x += int(s[1])

print(x, y)