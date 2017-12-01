from time import time

def main():

    start = time()

    largestConPan = 0
    i = 1

    while i < 987654321:

        #reset local variablles
        num = ''
        r = 0

        #multiply by increasing numbers until the length of i is more than 9
        while len(num) < 9:
            r += 1
            num += str(i * r)

        #check if the numbers are pandigital
        if r >= 2:
            if len(num) == 9:
                if isPan(num):
                    if int(num) > largestConPan:
                        largestConPan = int(num)

        #increase our multiplicand
        i += 1

        if i % 10000 == 0:
            print i

    print largestConPan
    print time() - start

def isPan(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n)) + 1):
        if not str(i) in str(n):
            return False
    return True

if __name__ == '__main__':
    main()
