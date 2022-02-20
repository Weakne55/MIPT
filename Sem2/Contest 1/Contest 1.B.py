def dot_product(N, vector1, vector2):
    s = 0
    for i in range(N):
        s += vector1[i]*vector2[i]
    return s


n = 3
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

print(dot_product(n, vec1, vec2))