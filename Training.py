lst = [0, 1, 2, 3, 4, 5, 6]

def modify_list(l):
    for item in l:
        if item % 2 != 0:
            l.remove(item)
    for i in range(len(l)):
        l[i] = l[i]//2




print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               #[1]
