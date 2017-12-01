def main():

    rows = {}
    it = 0
    product = 0

    with open("numbers.txt") as f:
        numbers = f.read()

    for i in range(0, len(numbers) - 13):

        check = 1

        for x in range(0, 13):
            check *= int(numbers[i + x])

        if check > product:
            product = check

    print product



if __name__ == '__main__':
    main()
