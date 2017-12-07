import math

def main():

    num = 13195
    num = 600851475143
    it = 2
    primes = []
    factors = []

    #iterate until the low end prime factors have been found
    while it < int(math.ceil(num ** 0.5)) + 1:

        flag = True

        #Check all of the numbers that could go into that point
        for i in range(2, int(math.ceil( it ** 0.5)) + 1):
            if it % i == 0:
                flag = False

        #Flags square numbers
        if it ** 0.5 == math.ceil(it ** 0.5):
            flag = False

        #if the number is prime
        if flag:
            primes.append(it)

        it += 1

    #check all the primes to see if they go into the number
    for p in primes:

        if num % p == 0:
            factors.append(p)
            num /= p

    print(factors[::-1])


if __name__ == '__main__':
    main()
