import matplotlib.pyplot as plt

# решение задачи из контеста
# ---------------------------------------------------
x1, y1, x2, y2 = map(float, input().split())
x0, y0 = map(float, input().split())

A1 = y2-y1
B1 = x1-x2
C1 = y1*(x2-x1) + x1*(y1-y2)

A2 = B1
B2 = -A1
C2 = y0*A1 - x0*B1

if A1 == 0:
    x = -(C2/A2)
    y = -(C1/B1)
elif B1 == 0:
    x = -(C1/A1)
    y = -(C2/B2)
elif A1 == 0 and B1 == 0:
    x = 0
    y = 0
else:
    y = (C1*A2 - C2*A1)/(B2*A1-B1*A2)
    x = -y*(B1/A1)-C1/A1

xf = 2*x - x0
yf = 2*y - y0
print(round(xf, 5), round(yf, 5))
# ---------------------------------------------------


plt.plot((x1, x2), (y1, y2), 'o-r')
plt.plot(x0, y0, color='orange', marker='o')
plt.plot(x, y, color='blue', marker='o')
plt.plot(xf, yf, color='black', marker='o')
plt.grid(True)
plt.show()

# 0 3 5 7
# 4 4

