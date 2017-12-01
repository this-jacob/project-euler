import time

global bump
bump = 1

def main():

    start_time = time.time()

    number = [0, 1, 2, 3]

    i = 0

    while i < 100:
        number = nextOrder(number)
        print number
        i += 1

    print number
    print time.time() - start_time

def nextOrder(n):

    #global bump

    strNum = ''
    intNum = 0
    num = n
    l = len(n) - 1
    checks = 0

    for i in range(len(n)):
        strNum += str(n[i])

    intNum = int(strNum)

    #iterate through every number in the array
    for x in range(1, len(n)):
        i = l - x
        if n[i] < n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            return n

        elif n[i] > n[i + 1]:
            for y in range(0, i):
                if not n[i - y] > n[i - y - 1]:

                    n.insert(i - y - 2, n[l])
                    n.pop()
                    return n

    #bump
    #print 'Bumping'
    #print n
    n.insert(i - checks, n[l])
    #print n
    n.pop()
    #print n
    #raw_input()

    return n


if __name__ == '__main__':
    main()
