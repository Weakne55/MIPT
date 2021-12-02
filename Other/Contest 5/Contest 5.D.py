def dot_product(N, v1, v2):
    result = []
    for i in range(N):
        result.append(v1[i]*v2[i])
    return sum(result)