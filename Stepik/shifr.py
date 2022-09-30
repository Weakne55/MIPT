s1 = input()
s2 = input()
trans = dict(zip(s1, s2))

forward = input()
backward = input()
f = ''
b = ''

for c in forward:
    if c in trans:
        f += trans[c]
    else:
        f += c

for w in backward:
    if w in trans.values():
        for k, v in trans.items():
            if v == w:
                b += k
    else:
        b += w

print(f)
print(b)