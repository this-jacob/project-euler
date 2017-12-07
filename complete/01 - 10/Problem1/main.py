def main():

    total = 0

    for i in range(0, 1000):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i

    print(total)

if __name__ == '__main__':
    main()
