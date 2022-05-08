n = int(input())
words = dict()

for i in range(n):
    w = input().lower()
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

print(max(words, key=words.get), words[max(words, key=words.get)])
