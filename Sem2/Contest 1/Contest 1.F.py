N = int(input())
h = []
for i in range(N):
    h.append(int(input()))

arr_help = [0]*(N)
try:
    arr_help[1] = abs(h[0] - h[1])
except:
    pass
else:
    for i in range(2, N):
        if (arr_help[i-1] + abs(h[i] - h[i-1])) < (arr_help[i-2] + 3*abs(h[i] - h[i-2])):
            arr_help[i] = arr_help[i-1] + abs(h[i] - h[i-1])
        else:
            arr_help[i] = (arr_help[i-2] + 3*abs(h[i] - h[i-2]))

print(arr_help[N-1])