p0, m0 = map(int, input().split())
# p - base
# m - mod
s0 = input()


def hash_poly(s, p, m):
    h = 0
    for i in range(len(s)):
        h += ord(s[i]) * (p**(len(s)-i-1))
    return h % m


print(hash_poly(s0, p0, m0))
