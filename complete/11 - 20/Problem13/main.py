def main():

    #open the file
    f = open("numbers.txt")

    huge = 0

    numbers = [0 for i in range(100)]

    it = 0
    for line in f:
        numbers[it] = line
        it += 1

    for each in numbers:
        huge += int(each)

    print(str(huge)[0:10])

if __name__ == '__main__':
    main()
