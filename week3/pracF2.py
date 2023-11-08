import time

start = time.time()
for i in range(3):
    print("The code is executing!")
    time.sleep(0.5)
end = time.time()

print("This program lives {} seconds until killed".format(end - start))
