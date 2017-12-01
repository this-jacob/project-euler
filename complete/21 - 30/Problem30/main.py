from time import time

def main():

    start = time()

    matches = []
    total = 0

    for i in range(1, 355000):
        if findPowerSum(i) == i:
            matches.append(i)

    for i in matches:
        total += i

    print total
    print time() - start

def findPowerSum(i):

    stri = str(i)

    a = 0

    for x in range(0, len(stri)):
        a += int(stri[x]) ** 5

    return a

if __name__ == '__main__':
    main()
