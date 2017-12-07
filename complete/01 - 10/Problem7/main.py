import math

def main():

    primes = 1
    it = 2

    while primes < 10001:

        flag = True

        for i in range(2, int(math.ceil( it ** 0.5)) + 1):
            if it % i == 0:
                flag = False

        if it ** 0.5 == math.ceil(it ** 0.5):
            flag = False

        if flag:
            print(it)
            primes += 1

        it += 1


if __name__ == '__main__':
    main()
