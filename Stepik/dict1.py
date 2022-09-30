words = dict()

with open('dataset_3363_3 (2).txt') as text:
    line = sorted(list(text.read().lower().strip().split()))
    for elem in line:
        if elem.lower() in words:
            words[elem.lower()] += 1
        else:
            words[elem.lower()] = 1

max = max(words.values())

for key, value in words.items():
    if value == max:
        val = value
        print(key, value)
        break

with open('dataset_3363_3 (2).txt') as text:
    line = sorted(list(text.read().strip().split()))
    for elem in line:
        if elem.lower == val:
            print(elem, max)
            break