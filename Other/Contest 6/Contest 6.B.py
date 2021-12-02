def day_massiv_potrogat(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for k in range(1, i+1):
            if arr[i-k] > arr[i-k+1]:
                arr[i-k+1], arr[i-k] = arr[i-k],  arr[i-k+1]
                day_massiv_potrogat(arr)
            else:
                continue


insertion_sort(list(map(int, input().split())))
