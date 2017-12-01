def main():

    fact = 1
    total = 0

    for i in range(1, 101):
        fact *= i

    for num in str(fact):
        total += int(num)

    print total
    
if __name__ == '__main__':
    main()
