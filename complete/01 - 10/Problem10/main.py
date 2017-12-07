import math

def main():

    nums = 1
    it = 2
    val = 0

    while nums < 2000000:

        flag = True

        for i in range(2, int(math.ceil( it ** 0.5)) + 1):
            if it % i == 0:
                flag = False

        if it ** 0.5 == math.ceil(it ** 0.5):
            flag = False

        if flag:
            val += it

        nums += 1
        it += 1

    print(val)


if __name__ == '__main__':
    main()
