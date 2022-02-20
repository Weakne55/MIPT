N = int(input())
a = list(map(int, input().split()))
result = []
for i in range(1, N-1):
    if (a[i - 1] < a[i] and a[i] > a[i + 1]) or (a[i - 1] > a[i] and a[i] < a[i + 1]):
        result.append(i)

print(*result)