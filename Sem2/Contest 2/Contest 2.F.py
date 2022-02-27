# n = int(input())
# k1 = dict()
# k2 = dict()
# k3 = dict()
# k4 = dict()
# for i in range(n):
#     x, y = map(float, input().split())
#     if x >= 0 <= y:
#         if y / x in k1.keys():
#             k1[y / x] += 1
#         else:
#             k1[y / x] = 1
#     elif x <= 0 <= y:
#         if y / x in k2.keys():
#             k2[y / x] += 1
#         else:
#             k2[y / x] = 1
#     elif x <= 0 >= y:
#         if y / x in k3.keys():
#             k3[y / x] += 1
#         else:
#             k3[y / x] = 1
#     elif x >= 0 >= y:
#         if y / x in k4.keys():
#             k4[y / x] += 1
#         else:
#             k4[y / x] = 1
#
# print(max(max(k1.values()), max(k2.values()), max(k3.values()), max(k4.values())))
#

x_plus = []
y_plus = []
x_minus = []
y_minus = []

pp = []
mp = []
mm = []
pm = []

N = int(input())
for i in range(N):
    x = [int(a) for a in input().split()]
    if x[0] > 0:
        if x[1] == 0:
            x_plus.append(x)
        elif x[1] > 0:
            pp.append(x)
        else:
            pm.append(x)
    elif x[0] < 0:
        if x[1] == 0:
            x_minus.append(x)
        elif x[1] > 0:
            mp.append(x)
        else:
            mm.append(x)
    elif x[0] == 0:
        if x[1] > 0:
            y_plus.append(x)
        else:
            y_minus.append(x)

res = max(len(x_plus), len(x_minus), len(y_plus), len(y_minus), 1)

for i in range(len(pp) - 1):
    k = pp[i][1]/pp[i][0]
    count = 1
    for j in range(i+1, len(pp)):
        m = pp[j][1]/pp[j][0]
        if m == k:
            count += 1
    res = max(res, count)

for i in range(len(pm) - 1):
    k = pm[i][1]/pm[i][0]
    count = 1
    for j in range(i+1, len(pm)):
        m = pm[j][1]/pm[j][0]
        if m == k:
            count += 1
    res = max(res, count)

for i in range(len(mp) - 1):
    k = mp[i][1]/mp[i][0]
    count = 1
    for j in range(i+1, len(mp)):
        m = mp[j][1]/mp[j][0]
        if m == k:
            count += 1
    res = max(res, count)

for i in range(len(mm) - 1):
    k = mm[i][1]/mm[i][0]
    count = 1
    for j in range(i+1, len(mm)):
        m = mm[j][1]/mm[j][0]
        if m == k:
            count += 1
    res = max(res, count)

print(res)
