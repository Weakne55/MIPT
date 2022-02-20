n = int(input())
fib = [1, 1] + [0]*(n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]
print(fib[n])
# это неправильная задача(