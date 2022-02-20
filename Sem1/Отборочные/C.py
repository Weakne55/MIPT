n, a, b = map(int, input().split())
if b > a:
    a, b = b, a
r1 = a - b
r2 = n - a + b
print(min(r1, r2))