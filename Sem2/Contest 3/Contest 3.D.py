def remove(table, key):
    for arr in table:
        if arr:
            for i in range(len(arr)):
                if arr[i][1] == key:
                    c = arr[i][2]
                    arr.remove(arr[i])
                    return c
    return 'KeyError'


example_table = [
    [], [],
    [
        [32, 'ONLY', 'pal;cw'],
        [62, 'INDUSTRY', 'lfow'],
        [72, 'LETRASET', 'awdwad'],
        [32, 'BEEN', 'lkawdk']
    ],
    [], [], [], [], [], [], [],
]

v1 = remove(example_table, 'BEEN')  # v1 == 'lkawdk'
v2 = remove(example_table, 'PRODUCT')  # v2 == 'KeyError'

print(*example_table)