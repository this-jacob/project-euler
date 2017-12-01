#
#   Find the sum of all 0 to 9 pandigital numbers with this property.
#

from itertools import permutations

def main():

    finalSum = 0

    for each in list(permutations('1234567890', 10)):
        if checkPandigital(str(int(''.join(each)))):
            finalSum += int(''.join(each))

    print finalSum
    return

def checkPandigital(number):

    divisors = [2, 3, 5, 7, 11, 13, 17]
    string = number

    for i in range(1, 8):
        substring = string[i:i+3]

        if int(substring) % divisors[i - 1] != 0:
            return False

    return True

if __name__ == '__main__':
    main()
