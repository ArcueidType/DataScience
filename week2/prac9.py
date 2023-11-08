import random
from math import sin
from math import cos

times = 10000000
inRealm = 0

i = times
while i > 0:
    x = random.uniform(2, 3)
    y = random.uniform(0, 21)
    if ((x*x) + 4*x*sin(x)) > y:
        inRealm += 1
    i -= 1

result =21 * (inRealm / times)
print("Estimated result: %.10f" % result)
print("Data volume:", times)
I = 4*(sin(3)-3*cos(3) + 2*cos(2) - sin(2)) + 9 - 8/3
print("Mathematical calculated result: %.10f" % I)
