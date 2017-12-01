def main():

    for a in range(1, 333):
        for b in range(1, 499):
            for c in range(1, 997):
                if a + b + c ==  1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        print a * b * c



if __name__ == '__main__':
    main()
