n = int(input("Please input a positive integer: "))
listArr = []

if n == 1:
    listArr.append(1)
elif n == 2:
    listArr.append(2)
elif n == 3:
    listArr.append(3)
elif n == 4:
    listArr.append(4)
elif n > 4:
    while n > 4:
        listArr.append(3)
        n -= 3
    if n != 0:
        listArr.append(n)
else:
    print("Invalid input! ")
    exit(-1)
listArr.sort()
print(listArr)
