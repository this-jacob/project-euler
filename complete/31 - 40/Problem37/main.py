from time import time
import math

def main():

    start = time()
    truncatablePrimes = []
    i = 8
    summ = 23

    while len(truncatablePrimes) < 10:
        i += 1
        if prime(i):
            if truncate(i):
                truncatablePrimes.append(i)
                print(i)

    for primes in truncatablePrimes:
        summ += primes

    print(truncatablePrimes)
    print(summ)
    print(time() - start)

def truncate(n):
    s = str(n)

    if s[0] == '1':
        return False
    if s[len(s) - 1] == '1':
        return False

    for i in range(0, len(s)):
        if not prime(int(s[i:])):
            return False
        if not prime(int(s[:len(s) - i])):
            return False

    return True

def prime(n):
    for i in range(2, int(math.ceil(n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
