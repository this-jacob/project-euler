import time

def main():

    start = time.time()

    size = 21
    number = 1

    #Initialize the matrix
    matrix = [[0 for x in range(size)] for y in range(size)]

    #fill the ones
    for i in range(0, size):
        matrix[0][i] = 1
        matrix[i][0] = 1

    #continue until the final square has been calculated
    while matrix[size - 1][size - 1] == 0:

        for i in range(number, size):
            matrix[number][i] = matrix[number][i - 1] + matrix[number - 1][i]
            matrix[i][number] = matrix[number - 1][i] + matrix[number][i - 1]

        number += 1

    elapsed = (time.time() - start)

    print(matrix[size - 1][size - 1])
    print(elapsed)

if __name__ == '__main__':
    main()
