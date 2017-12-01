def main():

    longest = 0
    startingNumber = 1

    #check every number under 1 000 000
    for startNum in range(1, 1000001):

        col = startNum
        chainLen = 0

        #continue until the colatz number is 0, calculating the length as you go
        while not col == 1:
            #even
            if col % 2 == 0:
                chainLen += 1
                col /= 2
            #odd
            else:
                chainLen += 1
                col *= 3
                col += 1

        #if the length is longer than the previous operations
        if chainLen > longest:
            longest = chainLen
            startingNumber = startNum

    #print the index to start
    print startingNumber



if __name__ == '__main__':
    main()
