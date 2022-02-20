n = int(input())
A = [format(i, 'b') for i in range(2**n)]
b = list()
c = list()
for i in range(len(A)):
    if len(A[i]) < n:
        b.append('0' * (n - len(A[i])) + A[i])
    else:
        b.append(A[i])

print(A)
print(b)
def one(s):
    arr = list()
    for j in range(len(s)):
        if s[j] == '?':
            arr.append('1')
        else:
            arr.append(s[j])
    return ''.join(arr)


def zero(s):
    arr = list()
    for j in range(len(s)):
        if s[j] == '?':
            arr.append('0')
        else:
            arr.append(s[j])
    return ''.join(arr)


s = 0
k = 0
while k < n**2:
    a = input()
    if b[k] == one(a):
        c.append(one(a))
    elif b[k] == zero(a):
        c.append(zero(a))
    else:
        s = 1
        break
    k += 1

if s == 1:
    print()
    print('NO')
else:
    print()
    print('YES')
    for k in range(len(c)):
        print(c[k])
