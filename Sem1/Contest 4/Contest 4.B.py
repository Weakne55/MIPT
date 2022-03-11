k = int(input())

if k > 1:
    for i in range(2, int(k / 2) + 1):
        if (k % i) == 0:
            print(0)
            break
    else:
        print(1)

else:
    print(0)

