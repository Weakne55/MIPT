n = input()
a = list(map(int, n))
for i in range(len(a)):
    print(a[i], "*10^", len(a)-i-1, sep='', end='')
    if i != len(a)-1:
        print(" + ", end='')