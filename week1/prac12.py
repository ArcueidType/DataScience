s = input("please input a number: ")
try:
    num = int(s)
except ValueError:
    try:
        num = float(s)
    except:
        print("Input must be a number!")
        exit()

# A simple way?
# print(num ** (1/3))

# Newton Iteration
epsilon = 1e-6  # The precision can be changed arbitrarily
x = num
while(abs(num - x ** 3) >= epsilon):
    x = (2 * x + (num/(x*x)))/3.0
print("%.6f"%x)
