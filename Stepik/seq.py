import requests

with open('dataset_3378_3 (1).txt') as inf:
    url = inf.read().strip()
    file = requests.get(url)
    while not file.text.startswith('We'):
        file = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + file.text)
    else:
        print(file.text)