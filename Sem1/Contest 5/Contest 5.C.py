def reverse_array(arr, N):
    if N == 1:
        return arr
    else:
        for i in range(N//2):
            n_for_i = arr[i]
            arr[i] = arr[N-1-i]
            arr[N-1-i] = n_for_i
        return arr