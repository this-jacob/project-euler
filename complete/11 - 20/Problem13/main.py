def main():

    #open the file
    f = open("numbers.txt")

    huge = long(0)

    numbers = [0 for i in range(100)]

    it = 0
    for line in f:
        numbers[it] = long(line)
        it += 1

    for each in numbers:
        huge += each

    print str(huge)[0:11]

if __name__ == '__main__':
    main()
