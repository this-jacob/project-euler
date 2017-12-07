from re import *

def main():

    names = []
    total = 0

    #read in the data from the file and prep the regular expression to find names
    f = open("names.txt")
    f_data = f.read()
    names_reading = compile('"\w*"')

    #Find all the names
    for each in names_reading.findall(f_data):
        names.append(each[1:-1])

    #sort the names alphabetically
    names.sort()

    #iterate through the names to calculate their value
    for i in range(0, len(names)):

        nameVal = 0

        #use the length of the name and check their value
        for x in range(0, len(names[i])):

            val = letterVal(names[i][x])
            nameVal += val

        nameVal *= (i + 1)
        total += nameVal

    print(total)

def letterVal(letter):

    letter = letter.lower()

    if letter == 'a':
        return 1
    elif letter == 'b':
        return 2
    elif letter == 'c':
        return 3
    elif letter == 'd':
        return 4
    elif letter == 'e':
        return 5
    elif letter == 'f':
        return 6
    elif letter == 'g':
        return 7
    elif letter == 'h':
        return 8
    elif letter == 'i':
        return 9
    elif letter == 'j':
        return 10
    elif letter == 'k':
        return 11
    elif letter == 'l':
        return 12
    elif letter == 'm':
        return 13
    elif letter == 'n':
        return 14
    elif letter == 'o':
        return 15
    elif letter == 'p':
        return 16
    elif letter == 'q':
        return 17
    elif letter == 'r':
        return 18
    elif letter == 's':
        return 19
    elif letter == 't':
        return 20
    elif letter == 'u':
        return 21
    elif letter == 'v':
        return 22
    elif letter == 'w':
        return 23
    elif letter == 'x':
        return 24
    elif letter == 'y':
        return 25
    elif letter == 'z':
        return 26
    else:
        return 0

if __name__ == '__main__':
    main()
