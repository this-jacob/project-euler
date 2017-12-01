def main():

    checks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = 1
    flag = False

    while not flag:

        perfect = True

        for eachChk in checks:
            if not num % eachChk == 0:
                perfect = False

        if perfect:
            flag = True

        num += 1

    print num - 1
    raise SystemExit


if __name__ == '__main__':
    main()
