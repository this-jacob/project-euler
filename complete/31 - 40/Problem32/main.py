from time import time

def main():

    start = time()

    products = []
    total = 0

    for m1 in range(1, 2000):
        for m2 in range(1, 2000):
            product = m1 * m2

            if len(str(m1) + str(m2) + str(product)) == 9:
                if isPan(str(m1) + str(m2) + str(product)):
                    if not product in products:
                        print m1, m2, product
                        products.append(product)

    for each in products:
        total += each

    print total
    print time() - start

def isPan(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n)) + 1):
        if not str(i) in str(n):
            return False
    return True

if __name__ == '__main__':
    main()
