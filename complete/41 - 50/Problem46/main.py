import math
import time

def main():

    start = time.time()

    nextComposite = 8
    primes = [2, 3, 5]

    while True:

        truthiness = False

        nextComposite = generateNextComposite(nextComposite)
        for each in generatePrimes(primes[-1], nextComposite - 2):
            primes.append(each)

        for eachPrime in primes:
            for i in range(1, math.ceil(nextComposite ** 0.5) - 1):
                if eachPrime + (2 * (i ** 2)) == nextComposite:
                    truthiness = True

        if not truthiness:
            print(nextComposite)
            print(time.time() - start)


    return

#generate prime numbers between a low number (the most recent prime number) and a high number (the next composite)
def generatePrimes(min, max):

    primes = []

    for x in range(min, max + 1):
        truthiness = False

        for i in range(2, math.ceil(x ** 0.5) + 1):
            if x % i == 0:
                truthiness = True

        if not truthiness:
            if x > min:
                primes.append(x)

    return primes

#generate the next composite number by iterating until finding an odd composite
def generateNextComposite(num):

    i = num + 1
    while not oddComposite(i):
        i += 1
    return i

#returns true if the number is odd and composite
def oddComposite(num):

    if num % 2 == 0:
        return False

    for i in range(2, math.ceil(num ** 0.5) + 2):
        if num % i == 0:
            return True
    return False

#Boiling da plate
if __name__ == '__main__':
    main()
