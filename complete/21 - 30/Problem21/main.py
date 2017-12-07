import time, math

def main():

    start_time = time.time()

    amicableSum = []
    factors = []

    for i in range(1, 10001):

        value1 = 0
        value2 = 0

        #get the factors of the first number
        factors = getFactors(i)
        for each in factors:
            value1 += each

        #get the factors of the second number
        factors = getFactors(value1)
        for each in factors:
            value2 += each

        #check if the numbers are amicable sums
        if not value1 == i:
            if i == value2:
                amicableSum.append(i)

    #output
    total = 0
    for each in amicableSum:
        total += each
    print(total)
    print(time.time() - start_time)


def getFactors(num):

    factors = [1]

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)

    return factors

if __name__ == '__main__':
    main()
