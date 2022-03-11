def hash_poly(s):
    h = 0
    for i in range(len(s)):
        h += ord(s[i]) * (91**(len(s)-i-1))
    return h % 100


def insert(table, key, value):
    j = hash_poly(key) % 10
    if not table[j]:
        table[j].append([str(hash_poly(key)), key, value])
    elif table[j][-1][1] == key:
        table[j][-1][2] = value
    else:
        table[j].append([str(hash_poly(key)), key, value])
    return


n = int(input())
hash_table = [[] for i in range(10)]
for i in range(n):
    k, val = input().split()
    insert(hash_table, k, val)

for l in range(len(hash_table)):
    if hash_table[l]:
        print(l)
        print('\n'.join(map(' '.join, hash_table[l])))

