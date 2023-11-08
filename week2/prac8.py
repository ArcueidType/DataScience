import random

times = 10000
inRealm = 0
# Monte Carlo
# i = times
# while i > 0:
#     x = random.uniform(0, 1)
#     y = random.uniform(0, 1)
#     if x*x + y*y < 1:
#         inRealm += 1
#     i -= 1

# pi = 4.0*(inRealm/times)
# print("pi = %.10f" % pi)
# print("Data volume:", times)

# i = 1
# pi = 0
# while i <= times:
#     if i%2 == 1:
#         pi += (1/(2*i -1))
#     else:
#         pi -= (1/(2*i -1))
#     i += 1
# pi *= 4
# print("Result: %.10f" % pi)
# print("Acumulated items:", times)

pi = 1
temp = 1
i = 1
while i < times:
    temp = temp * (i/(2*i+1))
    pi += temp
    i += 1
pi *= 2
print("Result: %.10f" % pi)
print("Acumulated items:", times)
