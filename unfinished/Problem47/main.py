import math
import time

def main():

    finished = False
    it = 2
    primes = [2]
    factorization = {}

    while not finished:
        #increment the iterator
        it += 1

        #do prime factorization
        for each in primes:
            if it % each == 0:
                it = it / each

            throughArray(it)


        #check for satisfaction of rules

    return

#generate the next prime number after currentHighest and return it
def generateNextPrime(currentHighest):
    nextPrime = -1
    it = currentHighest

    while nextPrime == -1:
        it += 1
        isComposite = False

        for i in range(2, math.ceil(it ** 0.5) + 1):
            if it % i == 0:
                isComposite = True

        if not isComposite:
            nextPrime = it
    return nextPrime


if __name__ == '__main__':
    print(generateNextPrime(449))
