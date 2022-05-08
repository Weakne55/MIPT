stack = []
operations = {'+', '-', '*'}

current = input()

while current != '=':
    if current not in operations:
        stack.append(int(current))
    elif current == '+':
        stack[-2] += stack[-1]
        stack.pop()
    elif current == '-':
        stack[-2] -= stack[-1]
        stack.pop()
    elif current == '*':
        stack[-2] *= stack[-1]
        stack.pop()

    current = input()

print(stack[0])

