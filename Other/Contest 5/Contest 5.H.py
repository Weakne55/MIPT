massive = list(map(int, input().split()))


def min (i, array):
    minim = array[i]
    for j in range(i, len(array)):
        if minim > array[j]:
            minim = array[j]
    return minim


def monotone(arr):
    counter = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            counter += 1
    if counter == len(arr)-1:
        return True
    else:
        return False



for k in range(len(massive)):
    for l in range(k, len(massive)):
        if monotone(massive):
            break
        else:
            if min(k, massive) == massive[l]:
                massive[k], massive[l] = massive[l], massive[k]
                print(*massive)
            else:
                continue
