def hash(s=str):
    return s

target = input()
text = input()

indexes = []

for i in range(0, len(text) - len(target) + 1):
    if hash(target) == hash(text[i:i+len(target)]):
        indexes.append(i)

if indexes:
    print(' '.join(map(str, indexes)))
else:
    print('Empty')