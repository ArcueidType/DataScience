num = float(input("Please input a num: "))
decimal = num % int(num)
integer = int(num)

liint = []

while integer != 0:
    liint.append(str(integer % 2))
    integer //= 2

liint.reverse()

print("".join(liint), end="")

print(".", end="")

cnt = 0
while decimal != 0 and cnt < 10:
    decimal *= 2
    if decimal >= 1:
        print(1, end="")
        decimal = decimal % int(decimal)
        cnt += 1
    else:
        print(0, end="")
        cnt += 1

print()
