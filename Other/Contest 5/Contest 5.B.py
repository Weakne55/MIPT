def cycle_shift(arr, N):
    n = arr[0]
    for i in range(N - 1):
        arr[i] = arr[i + 1]
    arr[-1] = n
    return arr