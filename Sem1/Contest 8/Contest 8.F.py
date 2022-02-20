N, M = map(int, input().split())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
counter = 0
if A1 <= A2:
    A1, A2 = A2, A1
for i in range(len(A1)):
    if A1[i] not in A2:
        counter +=  1
for i in range(len(A2)):
    if A2[i] not in A1:
        counter +=  1
if counter == 0:
    print('Yes')
else:
    print('No')
