def main():

    power = 1000
    total = 0
    value = 2 ** power

    for char in str(value):
        total += int(char)

    print(total)

if __name__ == '__main__':
    main()
