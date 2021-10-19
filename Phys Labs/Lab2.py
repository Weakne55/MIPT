# Отчёт по второй лабе
import numpy as np
import matplotlib.pyplot as plt


# Getting Data from txt
data20 = []
n = 0
with open('C:\Labs\Срабатывание счетчика за 20 секунд.txt', 'r') as inf:
    for line in inf:
        counter = [int(x) for x in line.split()[1:]]
        if n > 0:
            data20.extend(counter)
        else:
            n += 1


print(len(data20), "len(data(20))")

num_pulse = []
num_event = []
percentage = []

# Read quantities
with open('C:\Labs\Доля случаев.txt', 'r') as inf:
    for line in inf:
        num_pulse.extend([int(x) for x in line.split()[0:1]])
        num_event.extend([int(x) for x in line.split()[1:2]])
        percentage.extend([float(x) for x in line.split()[2:3]])

asas = []

for i in range(len(num_pulse)):
    for j in range(num_event[i]):
        asas.append(num_pulse[i])


print(asas, ' raspredelenie 10')

# Getting array with data within 40 sec
arr40 = []
for i in range(1, len(data20), 2):
    arr40.append(data20[i-1]+data20[i])

print(len(arr40), 'len(arr40)')

# Making set of quantities during the experiment
gist_data40_s = set(arr40)

# Number of every pulse during the experiment
number_of_pulse40 = []
for item in gist_data40_s:
    number_of_pulse40.append(arr40.count(item))

print(gist_data40_s, 'set of values')
print(number_of_pulse40)
print(sum(number_of_pulse40), 'number of pulse within 40 sec')
gist_data40_l = list(gist_data40_s)

# Make dictionary where we can see (number of pulses:number of cases)
help_me_pls = dict(zip(gist_data40_s, number_of_pulse40))

data_for_gist40 = []

# Make list with 0 cases for some pulses
for i in range(min(gist_data40_l), max(gist_data40_l)+1):
    if i in help_me_pls:
        # print(help_me_pls.get(i, 0))
        data_for_gist40.append(help_me_pls.get(i, 0))
    else:
        data_for_gist40.append(0)

print(data_for_gist40, 'list with number of cases')

# Make percentage of cases
sum_cases = sum(data_for_gist40)
percent_of_cases = []
for i in range(len(data_for_gist40)):
    percent_of_cases.append(data_for_gist40[i]/sum_cases)

print(percent_of_cases)  # gistogramm 40(2)


# 10 sec
mean_asas = np.mean(asas)
sigma_10 = np.sqrt((np.var(asas)))
print(mean_asas)
print(sigma_10)

# 40 sec
mean_arr40 = np.mean(arr40)
sigma_40 = np.sqrt((np.var(arr40)))
print(mean_arr40)
print(sigma_40)


# Make plot

# the histogram of the data
plt.hist(arr40, 54, density=True, histtype='step', alpha=0.5)
plt.hist(asas, 25, density=True, histtype='stepfilled', facecolor='g', alpha=0.35)

#Gauss
X10 = np.linspace(min(asas)-1, max(asas)+1, 200)
X40 = np.linspace(min(arr40)-1, max(arr40)+10, 200)

y10 = ((1 / (np.sqrt(2 * np.pi) * sigma_10)) *
     np.exp(-0.5 * (1 / sigma_10 * (X10 - mean_asas))**2))
plt.plot(X10, y10, '--', color='r')

y40 = ((1 / (np.sqrt(2 * np.pi) * sigma_40)) *
     np.exp(-0.5 * (1 / sigma_40 * (X40 - mean_arr40))**2))

plt.plot(X40, y40, '--', color='k')

#Poisson
#yP10 = np.exp(-mean_asas)*(mean_asas**


plt.show()
