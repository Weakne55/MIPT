lst = [1, 3, 5, 7]


def modify_list(l):
    for i in range(len(l)):
        if l[i] % 2 != 0:
            l.remove(l[i])
            if i != 0:
                i -= 1

    for i in range(len(l)):
        l[i] = l[i]/2



modify_list(lst)
print(lst)









