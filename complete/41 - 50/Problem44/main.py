#
#   Find the two pentagonal numbers with pentagonal differences and sums
#

from itertools import combinations

def main():

    pentagonals = []
    iterator = 0
    solved = False

    while not solved:
        iterator += 1
        pentagonals.append(generatePentagonal(iterator))

        #Check all the pentagonal additions up to the new pentagonal
        for each in list(combinations(pentagonals, 2)):
            #Check sum
            if each[0] + each[1] == pentagonals[-1]:
                #Check differences
                if abs(each[0] - each[1]) in pentagonals:
                    print each[0]
                    print each[1]
                    solved = True

    return

def generatePentagonal(n):

    return int((n * (3 * n - 1)) / 2)

if __name__ == '__main__':
    main()
