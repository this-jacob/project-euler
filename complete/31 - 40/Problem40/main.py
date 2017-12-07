from time import time

def main():

    start = time()

    num = 1
    decimal = ''

    #generate the string
    while len(decimal) <= 1000000:
        decimal += str(num)
        num += 1

    #multiply the numbers
    total = int(decimal[0]) * int(decimal[9]) * int(decimal[99]) * int(decimal[999]) * int(decimal[9999]) * int(decimal[99999]) * int(decimal[999999])

    print(total)
    print(time() - start)

if __name__ == '__main__':
    main()
