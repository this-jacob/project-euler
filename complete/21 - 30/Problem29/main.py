import time

def main():

    start_time = time.time()

    terms = []

    for a in range(2, 101):
        for b in range(2, 101):
            ab = a ** b
            if not ab in terms:
                terms.append(ab)

    print len(terms)
    print time.time() - start_time


if __name__ == '__main__':
    main()
