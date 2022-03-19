def move_goblin(deq, goblin):
    goblin = goblin.split()
    if goblin[0] == '+':
        deq.append(int(goblin[1]))
        return deq
    elif goblin[0] == '*':
        ind = len(deq) - len(deq)//2
        deq.insert(ind, int(goblin[1]))
        return deq
    elif goblin[0] == '-':
        print(deq.pop(0))
        return deq

deq = []
N = int(input())

for i in range(N):
    x = input()
    move_goblin(deq, x)