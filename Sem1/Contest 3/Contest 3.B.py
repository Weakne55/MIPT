n = int(input())
a = []
mn = []
for i in range(n):
    a.append([float(j) for j in input().split()])
for k in range(n):
    if a[k][0] >= 60 or (a[k][1]-100-a[k][2] < -10) or (a[k][1]-100-a[k][2] > 10):
        mn.append(a[k][3])
if len(mn) == 0:
    print(0)
else:
    print(sum(mn)/len(mn))