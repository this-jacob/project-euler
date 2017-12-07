from time import time

def main():

    start = time()
    total = 0

    for i in range(0, 1000001):
        if pal(i) and pal(int(str(bin(i))[2:])):
            total += i

    print(total)
    print(time() - start)

def pal(n):
    stri = str(n)
    if stri == stri[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
