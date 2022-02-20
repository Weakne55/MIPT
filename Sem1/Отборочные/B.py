n = int(input())
mat = [i for i in range(1, n+1)]
if len(mat) == 2:
    print(*mat[::-1])
else:
    if len(mat) % 2 == 0:
        for i in range(len(mat)//2):
            print(mat[i], end=' ')
            print(mat[len(mat)-i-1], end=' ')
    else:
        for i in range(len(mat)//2):
            print(mat[i], end=' ')
            print(mat[len(mat)-i-1], end=' ')
        print(mat[len(mat)//2])