def day_massiv_potrogat(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


def count_sort(arr):
    count_arr = [0]*10
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
        day_massiv_potrogat(count_arr)
    for j in range(len(count_arr)):
        for k in range(count_arr[j]):
            print(j, end=' ')


count_sort(list(map(int, input().split())))