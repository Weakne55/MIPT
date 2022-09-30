n = int(input())
results = dict()
for _ in range(n):
    s = input().split(';')

    if s[0] not in results:
        results[s[0]] = [1, 0, 0, 0, 0]
    else:
        results[s[0]][0] += 1
    if s[2] not in results:
        results[s[2]] = [1, 0, 0, 0, 0]
    else:
        results[s[2]][0] += 1

    if int(s[1]) < int(s[3]):
        results[s[0]][3] += 1
        results[s[2]][1] += 1
    elif int(s[1]) == int(s[3]):
        results[s[0]][2] += 1
        results[s[2]][2] += 1
    elif int(s[1]) > int(s[3]):
        results[s[0]][1] += 1
        results[s[2]][3] += 1

for key in results:
    results[key][4] = results[key][1]*3 + results[key][2] \

for k,v in results.items():
    print(k, end=':')
    print(*v)

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15