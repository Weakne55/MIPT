# def gvozdi(n=list):
#     counter = 0
#     arr = sorted(n)
#     if len(arr) == 2:
#         print(arr[0]-arr[1])
#     else:
#         for i in range(1, len(arr)-1):
#             if arr[i]-arr[i-1] > arr[i+1]-arr[i]:
#                 counter += arr[i+1]-arr[i]
#             else:
#                 counter += arr[i]-arr[i-1]
#         print(counter)
#
#
# gvozdi(list(map(int, input().split())))
#
#

lst = list(map(int, input().split()))
n = len(lst)
lst.sort()
d = [0] * n
d[1] = lst[1] - lst[0]
if n > 2:
    d[2] = lst[2] - lst[0]
    for i in range(3, n):
        d[i] = min(d[i - 2], d[i - 1]) + lst[i] - lst[i - 1]
print(d[n - 1])
