import random

def selectSort(arr: list):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
    return arr


def mergeSort(arr: list):
    if len(arr) == 1:
        return arr
    liLeft = mergeSort(arr[0 : (len(arr)//2)])
    liRight = mergeSort(arr[(len(arr)//2) : len(arr)])
    i, j = 0, 0
    liResult = []
    while i < len(liLeft) and j < len(liRight):
        if liLeft[i] < liRight[j]:
            liResult.append(liLeft[i])
            i += 1
        else:
            liResult.append(liRight[j])
            j += 1
    if i < len(liLeft):
        for num in liLeft:
            liResult.append(num)
    if j < len(liRight):
        for num in liRight:
            liResult.append(num)
    return liResult


length = 10
for i in range(5):
    liDisordered = []
    for j in range(length):
        liDisordered.append(random.randint(0, 300))
    length += random.randint(1, 10)
    print("NO.{} array originally looked: \n{}".format(i, liDisordered))
    # print("NO.{} array after sorted: \n{}".format(i, selectSort(liDisordered)))
    print("NO.{} array after sorted: {}".format(i, mergeSort(liDisordered)))
