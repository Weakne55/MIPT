import numpy as np
import matplotlib.pyplot as plt
x = list()

with open('C:\Labs\Карпович Гуревич\\11.3+400_1.txt', 'r') as inf:
    x.append([x for x in inf.readlines().split()])
print(x)
