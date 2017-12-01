def main():

    for i in range (1001, 3339):

        a = i
        b = a + 3330
        c = b + 3330

        flag = False
        flag2 = False

        for eachNum in str(a):
            if not (eachNum in str(b) or eachNum in str(c)):

                for eachOtherNum in str(b):
                    if not eachOtherNum in str(c):
                        flag = True

        if flag:
            for eachNum in str(a):
                if isPrime(int(eachNum)):
                    flag2 = True

        if flag2:
            if isPrime(a) and isPrime(b) and isPrime(c):
                print(str(a) + str(b) + str(c))

    return

def isPrime(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return True
    return False

if __name__ == '__main__':
    main()
