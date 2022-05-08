def secretary():
    abrakadabra = list(input().split())
    operations = {'#', '%'}
    stack = []

    if abrakadabra[0] in operations:
        print(0.0)
        return

    for i in range(len(abrakadabra)):
        if abrakadabra[i] not in operations:
            stack.append(float(abrakadabra[i]))
        elif abrakadabra[i] == '#':
            if stack:
                stack = [sum(stack)]
        elif abrakadabra[i] == '%':
            if len(stack) > 1:
                stack[-2] = stack[-2]*stack[-1]/100
                stack.pop()
            else:
                print(0.0)
        if i == len(abrakadabra) - 1:
            if stack:
                print(stack[-1])
            else:
                print(0.0)

secretary()