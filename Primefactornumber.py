from cmath import sqrt
import numbers
import math 

def prime(x):

    lx = []

    while x % 2 == 0:
        x = x // 2
        lx.append(2)
        if x == 1:
            print(lx)
            return

    for i in range(3, x + 1, 2):
        while (x % i == 0):
            x = x //  i
            lx.append(i)

    if x > 2:
        lx.append(x)

    print(lx)

prime(900)