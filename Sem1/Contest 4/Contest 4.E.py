item = int(input())


def n_sum(n):
    n_cube_root = int(round(n ** (1. / 3.), 2))
    for i in range(n_cube_root+1):
        division = n - i ** 3
        counter = i
        for j in range(int(round(division**(1./3.), 2))+1):
            if division == j**3:
                if j > counter:
                    print(counter, j)
                    return True
                else:
                    print(j, counter)
                    return True


if not n_sum(item):
    print('impossible')