from datetime import datetime

N = int(input())
data = [input() for i in range(N)]

data.sort(key=lambda date: datetime.strptime(date, '%d %B %Y %H:%M'))

for item in data:
    print(item)