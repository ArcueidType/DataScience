s = input("Please input a str: ")
prev = s[0]
for i in range(1, len(s)):
    if s[i] == prev:
        print("yes")
        exit()
    else:
        prev = s[i]
print("no")
