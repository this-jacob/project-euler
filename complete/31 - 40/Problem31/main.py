from time import time

def main():

    start = time()

    total = 0
    coins  = [1, 2, 5, 10, 20, 50, 100, 200]

    def changer(index, value):

        currentCoin = coins[index]

        if index == 0:
            if value % currentCoin == 0:
                total += 1
            return

        while(value >= 0):
            changer(index - 1, value)
            value -= currentCoin

    changer(len(coins) - 1, 200)

    print total
    print time() - start

if __name__ == '__main__':
    main()
