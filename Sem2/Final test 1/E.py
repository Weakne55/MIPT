s = []
var = {}
operations = input().split()
if operations[-1] != '=':
    print('incorrect')
    exit(0)
for a in operations:
    if a not in ['+', '-', '*', '/', '='] and not a.isdigit():
        var[a] = 0
for i in range(len(var)):
    y = input().split()
    if y[0] in var.keys():
        var[y[0]] = y[1]
    else:
        print('incorrect')
        exit(0)
for x in operations:
    if x.isdigit():
        s.append(int(x))
    elif x in var.keys():
        s.append(int(var[x]))
    elif x == '+':
        if len(s) >= 2:
            s[-2] += s[-1]
            del s[-1]  # последний элемент
        else:
            print('incorrect')
            exit(0)
    elif x == '-':
        if len(s) >= 2:
            s[-2] -= s[-1]
            del s[-1]
        else:
            print('incorrect')
            exit(0)
    elif x == '*':
        if len(s) >= 2:
            s[-2] *= s[-1]
            del s[-1]
        else:
            print('incorrect')
            exit(0)
    elif x == '/':
        if len(s) >= 2:
            s[-2] //= s[-1]
            del s[-1]
        else:
            print('incorrect')
            exit(0)
if len(s) == 1:
    print(s[0])
else:
    print('incorrect')