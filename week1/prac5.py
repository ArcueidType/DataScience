s = input("Please input three numbers seperated by space: ")
numstr = s.split(" ")
nums = []
for num in numstr:
    try:
        nums.append(int(num))
    except ValueError:
        try:
            nums.append(float(num))
        except:
            print("Wrong input")
            exit()
nums.sort()
print("Result: ", end="")
print(nums)
