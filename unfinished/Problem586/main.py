from time import time
import math, itertools

def main():

    start = time()

    n = 10 ** 15
    r = 40
    total = 0

    for i in itertools.count(1, 1):

        thisK = 0

        for b in xrange(1, int(math.ceil(math.sqrt(i))) + 1):
            for a in xrange(b, int(math.ceil(math.sqrt(i))) + 1):
                if ((a ** 2) + (3 * a * b) + (b ** 2)) == i:
                    thisK += 1
                if thisK > r:
                    break

        if thisK == r:
            total += 1

        if i % 1000 == 0:
            print i

        if i == n:
            print total
            print time() - start
            return

if __name__ == '__main__':
    main()
