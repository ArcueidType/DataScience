import math

def isPrime(x: int):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Please input an integer: "))
    if isPrime(num):
        print("It is a prime")
    else:
        print("Sry, but it's not a prime")
