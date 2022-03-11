nums = int(input())
ans = ''
x = nums
mums = nums
deg = 0

while x != 0:
    x //= 60
    deg += 1


A = []

for i in range(deg):
    if mums<60 and i == deg-1:
        A.append(mums)
    elif mums<60 and i != deg-1:
        A.append(0)
    else:
        n = mums//(60**(deg-i-1))
        A.append(n)
        mums -= n*60**(deg-i-1)

    dec = A[i] // 10
    ed = A[i] - 10 * dec
    ans = ans + '<' * dec + 'v' * ed + '.'

print(ans[:-1])