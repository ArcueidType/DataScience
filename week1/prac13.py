s = input("Please input a positive integer: ")
try:
    num = int(s)
    assert num > 0

except:
    print("Input must be a positive integer!")
    exit()

result = 1
for i in range(num, 0, -1):
    result *= i
print(result)
