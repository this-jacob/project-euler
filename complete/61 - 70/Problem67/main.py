from time import time

def main():

    start_time = time()

    numbers = []

    #specific variables to change the problem
    PATH = "triangle.txt"
    MAXIND = 99


    #open the triangle
    with open(PATH) as f:
        for line in f:
            numbers.append([int(n) for n in line.strip().split(' ')])


    for row in reversed(range(0, MAXIND)):
        for col in range(0, MAXIND):
            if numbers[row + 1][col] > numbers[row + 1][col + 1]:
                numbers[row][col] += numbers[row + 1][col]
            else:
                numbers[row][col] += numbers[row + 1][col + 1]

    print numbers[0][0]

    print time() - start_time

if __name__ == '__main__':
    main()
