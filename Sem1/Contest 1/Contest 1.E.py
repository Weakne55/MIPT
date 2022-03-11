l = int(input())
a = input()
animal = dict(zip(["monkey", "parrot", "elephant"], [90, 10, 300]))
for key in animal:
    if a == key:
        if l//animal[key] == 0:
            print(1)
        else:
            print(l//animal[key])