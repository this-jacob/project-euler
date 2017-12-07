def main():

    squareSum = 0       #(1 + 2)^2  square of the sums
    sumSquare = 0       #1^2 + 2^2  sum of the squares

    for i in range(1, 101):
        sumSquare += i ** 2
        squareSum += i

    squareSum = squareSum ** 2

    print(str(squareSum - sumSquare))

if __name__ == '__main__':
    main()
