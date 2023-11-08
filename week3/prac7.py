def gcd(x: int, y: int):
    if x < y:
        x, y = y, x
    while y != 0:
        tmp = y
        y = x % y
        x = tmp
    return x

nums = input("Please input two nums seperated by space: ")
linums = nums.split(" ")

for i in range(len(linums)):
    linums[i] = int(linums[i])

print(gcd(linums[0], linums[1]))
    