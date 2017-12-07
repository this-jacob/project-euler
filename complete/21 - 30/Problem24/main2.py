import time

def main():

    start_time = time.time()

    number = ''
    index = 1000000
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    for fac in reversed(range(1, 10)):
        for ind in range(1, 10):
            if ind * fact(fac) >= index:
                ind -= 1

                n = s[ind]
                number += str(n)
                s.pop(ind)

                index -= ind * fact(fac)

                break

    number += str(s[0])

    print(number)
    print(time.time() - start_time)

def fact(n):
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


if __name__ == '__main__':
    main()
