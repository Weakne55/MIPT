import requests


with open('dataset_3378_2.txt') as inf:
    url = inf.read().strip()
    file = requests.get(url)
    print(file.text.split())
