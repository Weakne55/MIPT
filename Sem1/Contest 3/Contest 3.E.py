d = {'.' : 1, '|' : 5, '@' : 0}

nums = input().split()
ans = 0

for i in range(len(nums)):
    x = 0
    deg = len(nums)-i-1
    for j in range(len(nums[i])):
        x += d[nums[i][j]]

    ans += (20**deg)*x

print(ans)