def main():
    currentFib = 1
    lastFib = 0
    temp = 0
    total = 0

    while currentFib < 4000000:
        #calculates the fib number
        temp = currentFib
        currentFib = lastFib + currentFib
        lastFib = temp

        #add to the sum if it is even
        if currentFib % 2 == 0:
            total += currentFib

    print(total)


if __name__ == '__main__':
    main()
