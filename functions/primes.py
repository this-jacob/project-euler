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
