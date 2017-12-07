from time import time

def main():

    start = time()

    numerators = []
    grandNum = 1
    denomenators = []
    grandDen = 1

    for num in range(10, 100):
        for den in range(10, 100):
            #break for trivial numbers
            if not str(den)[1] == '0':

                 #check if the last num and first den are the same
                 if str(num)[1] == str(den)[0]:
                     if float(num) / float(den) == float(str(num)[:1]) / float(str(den)[1:]) and float(num) / float(den) < 1:
                         numerators.append(num)
                         denomenators.append(den)

    for i in range(0, 4):
        grandNum *= numerators[i]
        grandDen *= denomenators[i]


    print(grandNum , grandDen)
    print(time() - start)

if __name__ == '__main__':
    main()
