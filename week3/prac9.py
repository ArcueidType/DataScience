import random

A = []
lenArr = random.randint(2, 20)
for i in range(lenArr):
    A.append(random.randint(0, 100))

B = []
for i in range(lenArr):
    cur = 1
    for j in range(lenArr):
        if(j == i):
            continue
        else:
            cur *= A[i]
    B.append(cur)
    
print("A = {}".format(A))
print("B = {}".format(B))
