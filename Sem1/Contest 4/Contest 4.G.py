a, b = map(int, input().split())
# a - сумма чисел
# b - количество чисел
def arr(a, b):
    array = [1] * b
    for i in range(1, b + 1):
        for j in range(1, 10):
            array[-i] = j
            if sum(array) == a:
                print(*array, end='', sep='')
                return


if a > b*9 or a < b*1 or b < 1:
    print('impossible')
else:
    arr(a, b)
