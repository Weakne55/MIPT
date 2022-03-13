def search(table, key):
    for arr in table:
        if arr:
            for i in range(len(arr)):
                if arr[i][1] == key:
                    return arr[i][2]
    return 'KeyError'