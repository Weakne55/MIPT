arr = list(map(int, input().split()))

def selection(data):
    data_copy = []
    for item in data:
        data_copy.append(item)
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e

        if data != data_copy:
            print(*data)
            data_copy.clear()
            for item in data:
                data_copy.append(item)
        else:
            continue


selection(arr)