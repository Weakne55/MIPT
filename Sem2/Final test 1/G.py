# a = list(input().split())
# stek =[]
# i = 0
# while int(a[i]) != 0:
#     if int(a[i]) > 0:
#         stek.append(int(a[i]))
#     else:
#         if stek != []:
#             if abs(int(a[i])) < stek[-1]:
#                 stek[-1] = stek[-1] + int(a[i])
#             else:
#                 stek.pop(-1)
#     i = i + 1
# if stek != []:
#     print(len(stek), stek[-1])
# else:
#     print('0', '-1')


a = list(map(int, input().split()))
s = []
for el in a:
    if el > 0:
        s.append(el)
    if len(s) > 0:
        if el < 0 and abs(el) < s[-1]:
            s[-1] += el
        elif el < 0 and abs(el) >= s[-1]:
            s.pop()

if len(s) == 0:
    print(0, -1)
else:
    print(len(s), s[-1])

