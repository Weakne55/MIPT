import matplotlib.pyplot as plt
import numpy as np
lст = 0.8206
mст = 0.993
mпр = 0.192
M = 3.542
l1 = 0.40
l2 = 0.15
m1 = 1.041
m2 = 1.316
L = l1 + l2
J0 = M*l1*l1
print(J0)
Jст = mст*((lст**2)/12) + (((L/2)-l2)**2) + mпр*(l1**2) + mпр*(l2**2)
print(Jст)
Jгр = J0 -Jст
arr = []
# b1 = l1 - np.sqrt((Jгр-m2*(l2+i)**2)/m1)
for i in range(int((lст-L)*100/2)):
    arr.append(l1 - np.sqrt((Jгр-m2*(l2+i)**2)/m1))

print(*arr)
