A = list(input())


def braces(a):
    l = []
    if a[0] == ']' or a[0] == ')' or a[0] == '}':
        return print('NO')
    for i in range(len(a)):
        if a[i] == '[' or a[i] == '(' or a[i] == '{':
            l.append(a[i])
        elif a[i] == ']' and l[-1] == '[':
            l.pop()
        elif a[i] == '}' and l[-1] == '{':
            l.pop()
        elif a[i] == ')' and l[-1] == '(':
            l.pop()
    if len(l) == 0:
        print('YES')
    else:
        print("NO")


braces(A)
#
# # ([((()))])

# a = input()
#
# def is_correct_brackets(text):
#     while '()' in text or '[]' in text or '{}' in text:
#         text = text.replace('()', '')
#         text = text.replace('[]', '')
#         text = text.replace('{}', '')
#     return 'YES' if not text else 'NO'
#
#
# print(is_correct_brackets(a))