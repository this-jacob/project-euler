import time

def main():

    start_time = time.time()
    totalMax = 0
    routes = 0
    path = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #path = [0, 0, 0, 0]
    MAXROWS = 15

    #open the triangle
    f = open("smallnumbers.txt")

    #declare a 2d array
    numbers = []

    #populate the array with the triangle
    for line in f:
        numbers.append([int(n) for n in line.strip().split(' ')])

    print numbers

    #brute force check all of the routes
    while not path[MAXROWS - 1] == MAXROWS - 1:
        #check to find the value of the current path
        localMax = 1
        row = 0
        for each in path:
            localMax += numbers[row][each]
            row += 1


        #bump the values of the path up if necessary
        bumpInd = 0
        bump = False

        if path[MAXROWS - 1] == path[MAXROWS - 2]:
            path[MAXROWS - 1] += 1
        else:
            #tick up
            for i in reversed(range(0, MAXROWS - 1)):
                if path[i - 1] == i - 1:
                    bumpInd = i
                    bump = True
                    break

        if bump:
            for i in range(bumpInd, MAXROWS):
                path[i] = bumpInd


        print path

        #check if the local max is greater than the totalMax
        if localMax > totalMax:
            totalMax = localMax


    f.close()

    print totalMax
    print time.time() - start_time

if __name__ == '__main__':
    main()
