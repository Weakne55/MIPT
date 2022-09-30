ins = input()
Arr = []
while ins != 'end':
    Arr.append(list(map(int, ins.split())))
    ins = input()

# print(Arr)

Barr = []
for i in range(len(Arr)):
    Barr.append([])
    for j in range(len(Arr[0])):
        Barr[i].append(0)

for i in range(len(Arr)):
    Arr[i].insert(0, Arr[i][-1])
    Arr[i].append(Arr[i][1])


# print(Arr)

Arr.insert(len(Arr), Arr[0])
Arr.insert(0, Arr[-2])

# print(*Arr, sep='\n')


for i in range(1, len(Arr)-1):
    for j in range(1, len(Arr[i])-1):
        Barr[i-1][j-1] = Arr[i][j-1] + Arr[i][j+1] + \
                     Arr[i+1][j] + Arr[i-1][j]

# print()

for i in range(len(Barr)):
    print(*Barr[i])

