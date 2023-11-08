s = input("Please input four numbers seperated by space: ")
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
nums.sort(reverse=True)
print("Result: ", end="")
print(nums)
