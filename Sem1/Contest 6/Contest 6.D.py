def day_massiv_potrogat(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


def bubble_sort(arr):
    N = (len(arr)-1)*len(arr)/2
    for j in range(int(N)):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                day_massiv_potrogat(arr)
                continue


bubble_sort(list(map(int, input().split())))
