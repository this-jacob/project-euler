from time import time
import math

def main():

    start = time()
    count = 1       #to account for two since it is never captured

    for i in range(2, 1000001):
        if prime(i):
            if circPrime(i):
                print(i)
                count += 1

    print(count)
    print(time() - start)

def circPrime(n):

    stri = str(n)
    perms = []

    #create the permutations
    for i in range(0, len(stri)):
        perms.append(stri[1:] + stri[0])
        stri = stri[1:] + stri[0]

    #check them all for prime
    for each in perms:
        if not prime(int(each)):
            return False
    return True

def prime(n):
    for i in range(2, int(math.ceil( n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
