with open('dataset_3363_4 (1).txt', 'r') as students:
    with open('result.txt', 'a') as results:
        mid1 = 0
        mid2 = 0
        mid3 = 0
        counter = 0
        for line in students:
            person = list(line.split(';'))
            mid = 0
            mid1 += int(person[1])
            mid2 += int(person[2])
            mid3 += int(person[3])
            for i in range(1, 4):
                mid += int(person[i])
            counter += 1
            results.write(str(round(mid/3, 9))+'\n')
        results.write(str(round(mid1/counter, 9))+' ')
        results.write(str(round(mid2/counter, 9))+' ')
        results.write(str(round(mid3/counter, 9)))
