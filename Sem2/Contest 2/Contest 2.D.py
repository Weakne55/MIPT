import matplotlib.pyplot as plt
x1, y1, x2, y2 = map(float, input().split())
x0, y0 = map(float, input().split())

a, b = y2 - y1, x1 - x2
c = y1*(x2-x1) - x1*(y2-y1)
mod = (x0*a + y0*b + c) if (x0*a + y0*b + c) > 0 else -(x0*a + y0*b + c)
znam = (a**2 + b**2) **(0.5)
res = mod/znam # расстояние до прямой
y_line = (x0*(y2-y1) + y1*(x2-x1) - x1*(y2-y1))/(x2-x1) if x2-x1 != 0 else (x0*(y2-y1) + y1*(x2-x1) - x1*(y2-y1))
x_line = (y0*(x2-x1) - y1*(x2-x1) + x1*(y2-y1))/(y2-y1) if y2-y1 != 0 else (y0*(x2-x1) + y1*(x2-x1) - x1*(y2-y1))
print(res)
print(y_line)
print(x_line)

lenght = x_line - x0 if x_line > x0 else x0 - x_line
print(lenght)
height = y_line - y0 if y_line > y0 else y0 - y_line

len1 = (lenght**2 - res**2)**(0.5)
hig1 = (height**2 - res**2)**(0.5)






plt.plot((x1, x2), (y1, y2), 'o-r')
plt.plot(x0, y0, color='orange', marker='o')
plt.plot(x0, y_line, color='blue', marker='o')
plt.plot(x_line, y0, color='green', marker='o')
# plt.plot(x_p, y_p, color='red', marker='o')
plt.grid(True)
plt.show()

# уравнение прямой
# ax + by + c = 0
# (x-x1)*(y2-y1) = (y-y1)*(x2-x1)
# x*(y2-y1) - x1*(y2-y1) = y*(x2-x1) - y1*(x2-x1)
# x*(y2-y1) - y*(x2-x1) + y1*(x2-x1) - x1*(y2-y1)  = 0

# у нас есть координаты точки и расстояние до прямой
# 0 3 5 7
# 4 4

