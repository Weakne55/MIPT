import numpy as np
import pandas as pd



mat_d = dict()
with open('matr.txt', 'r') as f:
    lines = f.readlines()
    mat_d[lines[0][0]] = np.array(lines[0][1:].split())
    for i in range(1, len(lines)):
        lin = lines[i].split()
        label = lin[0]
        values = np.array(lin[1:], dtype='float32')
        mat_d[label] = values

mat = pd.DataFrame(mat_d).set_index('i')


def replace(A, B, i):
    return i + mat[A][B]

def gap(i):
    return i - 2

def red_metr(s1, s2):
    M = len(s1)
    N = len(s2)
    field = np.zeros((M+1, N+1))
    path1 = ''
    path2 = ''
    # for i in range(M+1):
    #     field[i][0] = i*2
    #
    # for j in range(N+1):
    #     field[0][j] = j*2

    for i in range(1, M+1):
        for j in range(1, N+1):
            repl = replace(s1[i-1], s2[j-1], field[i-1][j-1])
            ins1 = gap(field[i-1][j])
            ins2 = gap(field[i][j-1])
            m = max(0, repl, ins1, ins2)
            field[i, j] = m
    return field

def deconv(s1, s2, field):
    i = len(s1)
    j = len(s2)
    ans1 = ''
    ans2 = ''
    while i != 0 or j != 0:
        if field[i, j] == 0:
            print('gone to zero')
            return ans1[::-1], ans2[::-1]

        if i > 0 and j > 0 and field[i, j] == replace(s1[i-1], s2[j-1], field[i-1, j-1]):
            ans1 += s1[i-1]
            ans2 += s2[j-1]
            i -= 1
            j -= 1
            continue

        elif j > 0 and field[i, j] == gap(field[i, j-1]):
            ans1 += '_'
            ans2 += s2[j-1]
            j -= 1
            continue

        elif i > 0 and field[i, j] == gap(field[i-1, j]):
            ans1 += s1[i-1]
            ans2 += '_'
            i -= 1

    return ans1[::-1], ans2[::-1]

s1 = 'SKAYRKPQI'
s2 = 'SKAZYVPPI'

f = red_metr(s1, s2)
p1, p2 = deconv(s1, s2, f)


print(f)
print('\n')
print(p1)
print(p2)



