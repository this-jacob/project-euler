def main():

    o = 0

    for i in range(1, 1001):
        o+= i ** i

    print(str(o)[-10:])

if __name__ == '__main__':
    main()
