# нужно перешать через dequeue

prog = input().split()
seq = input().split()
i = 0
for a in prog :
    while seq[i] != a :
        print(seq[i], end=' ')
        i += 1
    print(a, end=' ')
    i=0