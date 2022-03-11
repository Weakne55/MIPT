sm = int(input())

factorial = 1

for i in range(2, sm + 1):
    factorial *= i


counter = 0
a = str(factorial)[::-1]
for item in a:
    if item == '0':
        counter += 1
    else:
        break

print(counter)