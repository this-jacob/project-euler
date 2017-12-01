#
#   Find the sum of all 0 to 9 pandigital numbers with this property.
#

def main():

    c = 0
    num = '1234567890'
    finalSum = 0

    for swappingTime in range(0, 9):
        for cycleTime in range(0, 10):
            #Cycle the numbers
            num = cycleArray(num)

            #Check for agreeance with the problem
            if checkPandigital(num):
                finalSum += int(num)

        swapCharacters(num, swappingTime)

    print finalSum
    return

def cycleArray(number):

    numberList = list(number)
    bufferChar = numberList[0]

    #Move the numbers one to the left
    for each in range(1, len(numberList)):
        numberList[each - 1] = numberList[each]

    #place what started at the beginning at the end
    numberList[9] = bufferChar

    #Format from a list into a string
    numberList = ''.join(numberList)

    return numberList

def swapCharacters(number, base):

    numberList = list(number)
    bufferChar = numberList[base]
    numberList[base] = numberList[base + 1]
    numberList[base + 1] = bufferChar

    return ''.join(numberList)

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
