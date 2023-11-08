import random

arr = []

lenArr = random.randint(2, 20)
for i in range(lenArr):
    arr.append(random.randint(0, 100))

print("Original array:", arr)

for i in range(1, lenArr):
    j = i
    while j >=1 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
    
print("After insertion sort:", arr)
        