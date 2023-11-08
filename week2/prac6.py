c = int(input("Input a positive integer: "))

g = c / 4
count = 0

while abs(c - g*g) > 1e-11:
    g = (g + c/g) / 2
    count += 1

print("Result: %.11f" % g)
print("Loop times:", count)