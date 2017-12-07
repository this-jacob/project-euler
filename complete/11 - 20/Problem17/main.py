def main():

    num = 1000
    totalLetters = 0

    for i in range(1, 1001):
        totalLetters += makeWordsLength(i)

    print(totalLetters)

#function for returning the string version of a number without spaces
def makeWordsLength(n):

                    #n = unchanging value passed from main
    number = ''     #number = letters for a string
    num = n         #temp var used for computing the values

    hund = False

    #check the one thousands place
    if num == 1000:
        return len('onethousand')

    #check the hundreds place
    if num >= 100:
        number += 'hundred'
        hund = True

        if num >= 900:
            number += 'nine'
            num -= 900
        elif num >= 800:
            number += 'eight'
            num -= 800
        elif num >= 700:
            number += 'seven'
            num -= 700
        elif num >= 600:
            number += 'six'
            num -= 600
        elif num >= 500:
            number += 'five'
            num -= 500
        elif num >= 400:
            number += 'four'
            num -= 400
        elif num >= 300:
            number += 'three'
            num -= 300
        elif num >= 200:
            number += 'two'
            num -= 200
        else:
            number += 'one'
            num -= 100

    #check the tens place
    if num >= 20:

        if num >= 90:
            number += 'ninety'
            num -= 90
        elif num >= 80:
            number += 'eighty'
            num -= 80
        elif num >= 70:
            number += 'seventy'
            num -= 70
        elif num >= 60:
            number += 'sixty'
            num -= 60
        elif num >= 50:
            number += 'fifty'
            num -= 50
        elif num >= 40:
            number += 'forty'
            num -= 40
        elif num >= 30:
            number += 'thirty'
            num -= 30
        elif num >= 20:
            number += 'twenty'
            num -= 20

    #check the teens
    if num == 19:
        number += 'nineteen'
        num -= 19
    elif num == 18:
        number += 'eighteen'
        num -= 18
    elif num == 17:
        number += 'seventeen'
        num -= 17
    elif num == 16:
        number += 'sixteen'
        num -= 16
    elif num == 15:
        number += 'fifteen'
        num -= 15
    elif num == 14:
        number += 'fourteen'
        num -= 14
    elif num == 13:
        number += 'thirteen'
        num -= 13
    elif num == 12:
        number += 'twelve'
        num -= 12
    elif num == 11:
        number += 'eleven'
        num -= 11
    elif num == 10:
        number += 'ten'
        num -= 10

    #check the ones
    if num == 9:
        number += 'nine'
    elif num == 8:
        number += 'eight'
    elif num == 7:
        number += 'seven'
    elif num == 6:
        number += 'six'
    elif num == 5:
        number += 'five'
    elif num == 4:
        number += 'four'
    elif num == 3:
        number += 'three'
    elif num == 2:
        number += 'two'
    elif num == 1:
        number += 'one'

    if n % 100 == 0:
        hund = False

    if hund:
        number += 'and'

    print (number)

    return len(number)

if __name__ == '__main__':
    main()
