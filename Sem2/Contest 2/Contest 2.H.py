import matplotlib.pyplot as plt

x_all = []
y_all = []


def add(pos=int, x=float, y=float, x_arr=list, y_arr=list):
    x_arr.insert(pos, x)
    y_arr.insert(pos, y)


def area(coord_x=list, coord_y=list):
    first_sum = 0
    second_sum = 0
    for i in range(len(coord_x)-1):
        first_sum += coord_x[i] * coord_y[i+1]
        second_sum += coord_x[i+1] * coord_y[i]
    total_area = 0.5*abs(first_sum + coord_x[-1]*coord_y[0] - second_sum - coord_x[0]*coord_y[-1] )

    print(round(total_area, 5))

    # проверка
    # plt.figure(figsize=(12, 7))
    # plt.plot(coord_x, coord_y, color='blue', marker='o')
    # plt.grid(True)
    # plt.show()

    return


line = list(input().split())
while line[0] != 'end':
    if line[0] == 'add':
        add(int(line[1]), float(line[2]), float(line[3]), x_all, y_all)
    if line[0] == 'area':
        area(x_all, y_all)
    line = list(input().split())

# add 0 -1 3
# add 1 2 2
# add 2 -1 -1
# area
# add 2 3 -2
# area
# add 4 -2 1
# area
# 6.0 13.5 15.5
