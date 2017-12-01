def main():

    pal = []
    high = 0

    for x in range(100, 999):
        for y in range(100, 999):

            num = str(x * y)

            if num == num[::-1]:
                pal.append(num)

    for each in pal:
        if each > high and len(each) >= 6:
            high = each
            print each

    print high


if __name__ == '__main__':
    main()
