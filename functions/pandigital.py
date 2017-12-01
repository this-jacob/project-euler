def isPandigitalZero(number):

    check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for each in check:
        if not each in str(number): return False

    return True

def isPandigital(number):

    check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for each in check:
        if not each in str(number): return False

    return True

if __name__ == '__main__':
    print isPandigital(123456789)
