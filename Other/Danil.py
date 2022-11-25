s = input()
pr = ''

nucleotids = ['A', 'U', 'G', 'C']

proteins = {
    'UUU':'F',      'CUU':'L',      'AUU':'I',      'GUU':'V',
    'UUC':'F',      'CUC':'L',      'AUC':'I',      'GUC':'V',
    'UUA':'L',      'CUA':'L',      'AUA':'I',      'GUA':'V',
    'UUG':'L',      'CUG':'L',      'AUG':'M',      'GUG':'V',
    'UCU':'S',      'CCU':'P',      'ACU':'T',      'GCU':'A',
    'UCC':'S',      'CCC':'P',      'ACC':'T',      'GCC':'A',
    'UCA':'S',      'CCA':'P',      'ACA':'T',      'GCA':'A',
    'UCG':'S',      'CCG':'P',      'ACG':'T',      'GCG':'A',
    'UAU':'Y',      'CAU':'H',      'AAU':'N',      'GAU':'D',
    'UAC':'Y',      'CAC':'H',      'AAC':'N',      'GAC':'D',
    'UAA':'Stop',   'CAA':'Q',      'AAA':'K',      'GAA':'E',
    'UAG':'Stop',   'CAG':'Q',      'AAG':'K',      'GAG':'E',
    'UGU':'C',      'CGU':'R',      'AGU':'S',      'GGU':'G',
    'UGC':'C',      'CGC':'R',      'AGC':'S',      'GGC':'G',
    'UGA':'Stop',   'CGA':'R',      'AGA':'R',      'GGA':'G',
    'UGG':'W',      'CGG':'R',      'AGG':'R',      'GGG':'G',
}

for i in range(3, len(s)+1, 3):
    if s[i-3:i] in proteins.keys():
        if proteins[s[i-3:i]] == 'Stop':
            break
        else:
            pr += proteins[s[i-3:i]]
    elif s[i-3:i].count('-') == 2:
        pr += 'Gap'
    elif s[i-3:i].count('-') == 1:
        for j in range(1, len(nucleotids)):
            if proteins[s[i-3:i-1] + nucleotids[0]] != proteins[s[i-3:i-1] + nucleotids[j]]:
                pr += 'Gap'
                break
            pr += proteins[s[i-3:i-1] + 'A']
            break

print(pr)

# AUGUAAGCCAUGGC-C--UAAAUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA