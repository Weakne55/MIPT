cards = list(input().split())

alignment = [cards[0]]
buyback = []

for i in range(1, len(cards)):
    if (cards[i][0] == alignment[-1][0]
            and abs(int(cards[i][1]) - int(alignment[-1][1])) <= 2):
        buyback.append(alignment[-1])
        buyback.append(cards[i])
        alignment.pop()
        while len(alignment) > 1:
            if alignment[-1][0] == alignment[0][0]:
                buyback.append(alignment[-1])
                buyback.append(alignment[0])
                alignment.pop()
                alignment.pop(0)
            else:
                break
    alignment.append(cards[i])


print(len(buyback))