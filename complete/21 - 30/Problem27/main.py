from time import time
import math

def main():

    start_time = time()

    n = 0
    count = 0
    afin = 0
    bfin = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0

            while isPrime(abs((n * n) + (a * n) + b)):
                n += 1

            if n > count:
                afin = a
                bfin = b
                count = n
        print(a)

    print(afin * bfin)
    print(time() - start_time)

def isPrime(n):
    for i in range(2, int(math.ceil(n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
