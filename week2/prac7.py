c = int(input("Input a positive integer: "))

g = c / 3
count = 0

while(abs(c - g ** 3) > 1e-11):
    g = (2 * g + (c/(g*g)))/3.0
    count += 1
    
print("Result: %.11f" % g)
print("Loop times:", count)