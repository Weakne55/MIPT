import matplotlib.pyplot as plt

x1, y1, x2, y2, x3, y3 = map(int, input().split())
x0, y0 = map(int, input().split())

x4 = 2*x0 - x1
x5 = 2*x0 - x2
x6 = 2*x0 - x3

y4 = 2*y0 - y1
y5 = 2*y0 - y2
y6 = 2*y0 - y3

print(x4, y4, x5, y5, x6, y6)

plt.figure(figsize=(12, 7))
plt.plot((x1, x2, x3, x1), (y1, y2, y3, y1), 'o-r')
plt.plot(x0, y0, color='orange', marker='o')
plt.plot((x4, x5, x6, x4), (y4, y5, y6, y4), 'o-b')
plt.grid(True)
plt.show()

# 1 0 -1 0 0 5
# 0 0

# 1 7 -2 -5 7 8
# 0 0
