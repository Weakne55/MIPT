def poly_hash(p, mod, s):
    value = 0
    for pose, elem in enumerate(s):
        value += ord(elem) * p ** pose
    return value % mod
