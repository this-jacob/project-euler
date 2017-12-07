def main():

    #declare a 2d array
    numbers = [[0 for x in range(20)] for y in range(20)]

    #Open the file
    f =  open("numbers.txt")

    xbase = 0
    ybase = 0

    highest = 0

    #read in all the information
    for line in f:
        for num in line.split():

            #Fill the array with the nums
            numbers[xbase][ybase] = int(num)

            xbase += 1
            if xbase > 19:
                xbase = 0
                ybase += 1


    #check the horizontal
    for y in range(0, 20):
        for x in range(0, 17):
            if numbers[x][y] * numbers[x + 1][y] * numbers[x + 2][y] * numbers[x + 3][y] > highest:
                highest = numbers[x][y] * numbers[x + 1][y] * numbers[x + 2][y] * numbers[x + 3][y]


    #check the verticals
    for y in range(0, 17):
        for x in range(0, 20):
            if numbers[x][y] * numbers[x][y + 1] * numbers[x][y + 2] * numbers[x][y + 3] > highest:
                highest = numbers[x][y] * numbers[x][y + 1] * numbers[x][y + 2] * numbers[x][y + 3]

    #check the diagonals down
    for y in range(0, 17):
        for x in range(0, 17):
            if numbers[x][y] * numbers[x + 1][y + 1] * numbers[x + 2][y + 2] * numbers[x + 3][y + 3] > highest:
                highest = numbers[x][y] * numbers[x + 1][y + 1] * numbers[x + 2][y + 2] * numbers[x + 3][y + 3]

    #check the diagonals up
    for y in range(3, 20):
        for x in range(0, 17):

            print(x , y)

            if numbers[x][y] * numbers[x + 1][y - 1] * numbers[x + 2][y - 2] * numbers[x + 3][y - 3] > highest:
                highest = numbers[x][y] * numbers[x + 1][y - 1] * numbers[x + 2][y - 2] * numbers[x + 3][y - 3]

    #print out the highest
    print(highest)



if __name__ == '__main__':
    main()
