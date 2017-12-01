import math

def main():

    divs = 0
    num = 0
    triangle = 0

    while divs < 500:

        #reset the variables for the new num-th triangle number
        num += 1
        divs = 0
        triangle = 0

        #calculate the num-th triangle number
        for i in range(0, num + 1):
            triangle += i

        #find the number of factors of the triangle
        for i in range(1, int(math.ceil(triangle ** 0.5)) + 1):
            if triangle % i == 0:
                divs += 2

    print triangle



if __name__ == '__main__':
    main()
