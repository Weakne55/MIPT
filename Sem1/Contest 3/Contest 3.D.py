a = list(map(int, input()))
s = 0
for i in range(len(a)):
    s += a[i]*((-10)**(len(a)-i-1))
print(s)