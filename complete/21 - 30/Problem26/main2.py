from time import time

def main():

    start_time = time()

    for divisor in range(2, 1001):
        print divisor, str(1.0 / divisor)

    print time() - start_time

if __name__ == '__main__':
    main()
