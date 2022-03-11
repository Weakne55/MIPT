y = int(input())
if y%4 !=0 :
    print("NO")
elif y%100 !=0:
    print("YES")
elif y%400 != 0:
    print("NO")
else:
    print("YES")