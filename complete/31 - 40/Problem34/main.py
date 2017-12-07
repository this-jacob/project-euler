from time import time

def main():

    start = time()

    high = fac(10)
    summ = 0

    for i in range(3, high):
        if digitsFact(i) == i:
            summ += i

    print(summ)
    print(time() - start)

def digitsFact(n):

    stri = str(n)
    total = 0

    for i in range(0, len(stri)):
        total += fac(int(stri[i]))

    return total

def fac(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

if __name__ == '__main__':
    main()
