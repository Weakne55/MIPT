N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

counter = 0
n = int(input())
if n < N:
    for item in a:
        if item > a[n]:
            counter += 1
    print(counter)