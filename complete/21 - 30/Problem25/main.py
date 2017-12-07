import time

def main():

    start_time = time.time()

    fone = 1
    ftwo = 1
    f = 2
    index = 2

    while len(str(f)) < 1000:
        f = fone + ftwo
        ftwo = fone
        fone = f
        index += 1

    print(index)
    print(time.time() - start_time)

if __name__ == '__main__':
    main()
