def matryoshka(n):

    def verh(m):
        if m > 1:
            print('verh matryoshki', m)
            verh(m - 1)
        elif m == 1:
            print('matryoshechka')

    def niz(k):
        if k < n:
            print('niz matryoshki', k+1)
            niz(k+1)

    verh(n)
    niz(1)


matryoshka(int(input()))