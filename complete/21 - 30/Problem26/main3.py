from time import time

def main():

    start = time()

    highestLen = 0

    for i in range(1, 1001):
        newLen = len(divideBy(1, i))
        if newLen > highestLen:
            finalI = i
            highestLen = newLen

    print finalI
    print time() - start

def divideBy(n, div):
    ins = []

    while True:

        n *= 10
        n %= div

        if n in ins:
            break
        ins.append(n)
    return ins




if __name__ == '__main__':
    main()
