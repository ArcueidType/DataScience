s = input("Please input a sequence where each elements seperated by comma: ")
oriSe = s.split(",")
newSe = []
# for
# try:
#     for i in range(len(oriSe)-1, -1, -1):
#         newSe.append(oriSe[i])
#     print("new sequence: ", end="")
#     print(newSe)

# while
try:
    i = len(oriSe)-1
    while i >= 0:
        newSe.append(oriSe[i])
        i -= 1
    print("new sequence: ", end="")
    print(newSe)
except:
    print("The sequence should not be none")
