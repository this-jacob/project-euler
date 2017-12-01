from time import time

def main():

    start = time()

    maxIntegrals = 0
    optimumPerimeter = 0

    for perimeter in range(4, 1001):
        integrals = 0

        for a in range(1, perimeter / 2):
            for b in range(a, perimeter / 2):
                for c in range(b, perimeter / 2):
                    if a + b + c == perimeter:
                        if a ** 2 + b ** 2 == c ** 2:
                            integrals += 1

        if integrals > maxIntegrals:
            optimumPerimeter = perimeter
            maxIntegrals = integrals
            print perimeter, maxIntegrals

    print optimumPerimeter
    print time() - start

if __name__ == '__main__':
    main()
