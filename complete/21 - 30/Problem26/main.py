from time import time
import math

def main():

    start_time = time()

    d = 0
    dlen = 0

    #main loop to check all numbers
    for divisor in range(2, 11):

        dividend = 1
        remainders = []
        remainder = 0

        while not repeated(remainder, remainders):
            if not dividend == 0:
                if goesIn(dividend, divisor):
                    for mult in reversed(range(1, dividend + 1)):
                        if divisor * mult <= dividend:
                            remainder = dividend - (divisor * mult)
                            remainders.append(remainder)
                            print remainders
                            dividend = remainder
                            print dividend
                else:
                    dividend *= 10
            else:
                break

        if len(remainders) > dlen:
            dlen = len(remainders)
            d = divisor


    print d
    print time() - start_time

def repeated(r, remainders):
    if r in remainders:
        return True
    else:
        return False

def goesIn(dividend, divisor):
    if dividend / divisor >= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
