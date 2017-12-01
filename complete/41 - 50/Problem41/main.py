from time import time
import math

def main():

    start = time()

    largestPanPrime = 0

    for n in reversed(xrange(1, 987654322)):
        if isPan(n):
            if prime(n):
                print n
                print time() - start
                raw_input()

        if n % 100000 == 0:
            print n

def isPan(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n)) + 1):
        if not str(i) in str(n):
            return False
    return True

def prime(n):
    for i in range(2, int(math.ceil(n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
