# Отчёт по первой лабе
import numpy as np
import matplotlib.pyplot as plt

# Getting Data from txt
with open('C:\Labs\Data20.txt', 'r') as inf:
    V20 = [float(x) * 1000 for x in inf.readline().split(" ")]  # type = float within list
    I20 = [float(x) * 5 for x in inf.readline().split(" ")]  # list comprehension [str(x) for x in lst]

with open('C:\Labs\Data30.txt', 'r') as inf:
    V30 = [float(x) * 1000 for x in inf.readline().split(" ")]
    I30 = [float(x) * 5 for x in inf.readline().split(" ")]

with open('C:\Labs\Data50.txt', 'r') as inf:
    V50 = [float(x) * 1000 for x in inf.readline().split(" ")]
    I50 = [float(x) * 5 for x in inf.readline().split(" ")]



# Calculation V=RI
def mid(V, I):
    VI = []
    for i in range(len(I)):
        VI.append(V[i] * I[i])
    return np.mean(VI)


def findR(V, I):
    R = mid(V, I) / mid(I, I)
    return R


R20 = findR(V20, I20)
R30 = findR(V30, I30)
R50 = findR(V50, I50)
print(R20)
print(R30)
print(R50)


# Error
def errors(V, I, R):
    randEr = (1 / 3) * np.sqrt(((mid(V, V)) / (mid(I, I))) - R ** 2)
    print(randEr, "rand")
    sysEr = randEr / R
    print(sysEr, "sys")
    fulEr = np.sqrt(sysEr ** 2 + randEr ** 2)
    return fulEr



print(errors(V20, I20, R20), "full")
print(errors(V30, I30, R30), "full")
print(errors(V50, I50, R50), "full")


def ErrorUP(V):
    A = []
    for v in V:
        A.append(v * 1.0003)
    return A


def ErrorDown(V):
    A = []
    for v in V:
        A.append(v * 0.9997)
    return A


# Making plot
plt.xlim([0, 750])
plt.ylim([0, 4000])
plt.grid(True)

# Titles
plt.xlabel(r'$I_а$, мA')
plt.ylabel(r'$V_в$, мВ')

# Making dots on plot
plt.plot(I20, V20, 'og', label='$l$ = 20 см,\n $k$ = 2.1154$\pm$0.0036')
plt.plot(I30, V30, '^b', label='$l$ = 30 см,\n $k$ = 3.1269$\pm$0.0025')
plt.plot(I50, V50, 'dr', label='$l$ = 50 см,\n $k$ = 5.2647$\pm$0.0112')

# Making curves on plot
x = np.arange(0, 750, 0.01)
plt.plot(x, R20 * x, 'k')
plt.plot(x, R30 * x, 'k')
plt.plot(x, R50 * x, 'k')

# Errors on plot
plt.plot(I20, ErrorUP(V20), '_k')
plt.plot(I20, ErrorDown(V20), '_k')

plt.plot(I30, ErrorUP(V30), '_k')
plt.plot(I30, ErrorDown(V30), '_k')

plt.plot(I50, ErrorUP(V50), '_k')
plt.plot(I50, ErrorDown(V50), '_k')

def Apr(V,m,b):
    a = []
    for i in V:
        a.append(i*m+b)
    return a


#plt.plot(x,Apr(x,m,b) )

plt.legend(loc='best', fontsize=12, )
plt.show()