d = {'v' : 1, '<' : 10, '' : 0}

nums = input().split('.')
ans = 0

for i in range(len(nums)):
    x = 0
    deg = len(nums)-i-1
    for j in range(len(nums[i])):
        x += d[nums[i][j]]

    ans += (60**deg)*x

print(ans)