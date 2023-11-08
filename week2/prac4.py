def squareRoot(c: int):
    g = 0
    for i in range(c + 1):
        if i * i > c:
            g = i - 1
            break
    while abs(c - g*g > 1e-4):
        g += 1e-5
    print("Result: %.8f" % g)
    
if __name__ == '__main__':
    squareRoot(2)