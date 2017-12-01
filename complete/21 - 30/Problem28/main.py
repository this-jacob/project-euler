from time import time

def main():

    start = time()

    SIZE = 1001

    step = SIZE - 1
    stepsTaken = 0

    total = SIZE ** 2
    sumation = 0

    while total > 1:
        sumation += total
        total -= step
        stepsTaken += 1

        if stepsTaken == 4:
            step -= 2
            stepsTaken = 0

    print sumation + 1
    print time() - start

if __name__ == '__main__':
    main()
