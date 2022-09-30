pupils = {i: [] for i in range(1, 12)}
with open('dataset_3380_5 (3).txt') as text:
    for line in text:
        s = line.strip().split()
        pupils[int(s[0])].append(int(s[2]))

for j in range(1, len(pupils) + 1):
    if len(pupils[j]) > 0:
        print(j, round(sum(pupils[j]) / len(pupils[j]),5))
    else:
        print(j, '-')
