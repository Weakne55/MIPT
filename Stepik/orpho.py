n = int(input())
words = set()
for _ in range(n):
    words.add(input().lower())
fails = set()

l = int(input())
for _ in range(l):
    s = input().lower().split()
    for el in s:
        if el not in words:
            fails.add(el)

print(*fails, sep='\n')