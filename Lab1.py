# Отчёт по первой лабе
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Getting Data from txt

with open('C:\Labs\Data20.txt', 'r') as inf:
    V20 = [float(x) for x in inf.readline().split(" ")]   # type = float within list
    I20 = [float(x) for x in inf.readline().split(" ")]   #list comprehension [str(x) for x in lst]

with open('C:\Labs\Data30.txt', 'r') as inf:
    V30 = [float(x) for x in inf.readline().split(" ")]
    I30 = [float(x) for x in inf.readline().split(" ")]

with open('C:\Labs\Data50.txt', 'r') as inf:
    V50 = [float(x) for x in inf.readline().split(" ")]
    I50 = [float(x) for x in inf.readline().split(" ")]

#Transform V into mV
def mlV(V):
    mV = [x*1000 for x in V]
    return mV

#Calculation R

def Res(I,V):
    R = []
    for i in range(1,len(I)):
        R.append(V[i]/I[i])
    return R



#Making curves on plot


plt.plot(I20, mlV(V20))
plt.plot(I30, mlV(V30))
plt.plot(I50, mlV(V50))

plt.xlabel(r'$I_а$, мA')
plt.ylabel(r'$V_в$, мВ')
plt.legend(loc='best', fontsize=12)

plt.xlim([0, 150])
plt.ylim([0, 4000])

plt.show()
