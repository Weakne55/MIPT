c = int(input())
buf = [0]*(int(c//2))
bufbuf = []
a = 0
b = 0
abuf = 0
bbuf = 0
k = False
for i in range(int(c//2)):
    buf[i] = i+1
for i in buf:
    if c % i == 0:
        bufbuf.append(i)
for i in bufbuf:
    if (12*c-3*(i**3))/i >= 0:
        abuf = (3*i-((12*c-3*(i**3))/i)**0.5)/6
        bbuf = (3*i+((12*c-3*(i**3))/i)**0.5)/6
        if abuf > 0 and abuf % 1 == 0 and bbuf % 1 == 0:
            a, b = abuf, bbuf
            k = True
if c**(1/3) % 1 == 0:
    print(0, int(c**(1/3)))
elif (c/2)**(1/3)%1 == 0:
    print(int((c/2)**(1/3)),int((c/2)**(1/3)))
elif k == False:
    print('impossible')
else:
    print(int(a),int(b))