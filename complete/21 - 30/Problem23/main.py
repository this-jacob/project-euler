import time

def main():

    start_time = time.time()
    abundantNums = []
    canBeAbundant = {}
    total = 0

    #calculate all abundant numbers that could possibly be used 14062
    for i in range(1, 20162):

        canBeAbundant[i] = False

        factors = []
        abund = 0

        #find all the factors for each i
        for x in range(1, i):
            if i % x == 0:
                abund += x

        #it is an abundant number
        if abund > i:
            abundantNums.append(i)

    print abundantNums
    print time.time() - start_time

    for each1 in abundantNums:
        for each2 in abundantNums:
            if each1 + each2 <= 20161:
                canBeAbundant[each1 + each2] = True
            else:
                break

    for i in range(1, 20162):
        if not canBeAbundant[i]:
            total += i

    print total
    print time.time() - start_time

if __name__ == '__main__':
    main()
