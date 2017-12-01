from time import time

def main():

    start = time()

    #declare variables
    longestWord = 'a'
    triangles = [-1]
    last = 0
    triN = 0
    total = 0

    #read file
    f = open("words.txt")
    words_data = f.read()
    words = []
    words = words_data.split('\",\"')

    #Remove leading and trailing quotes
    words[0] = words[0][1:]
    words[len(words) - 1] = words[len(words) - 1][:-1]

    #calculate triangle numbers using the longest possible word
    while last < 15 * 26:
        triN += 1
        last = (0.5) * triN * (triN + 1)
        triangles.append(int(last))

    triangles.pop(0)
    print triangles

    #calculate word values
    for each in words:
        print each ,
        if int(wordVal(each)) in triangles:
            total += 1

    print total
    print time() - start

def wordVal(n):
    ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']
    val = 0
    for i in range(0, len(n)):
        for x in range(0, len(ALPHA)):
            if ALPHA[x] == n[i].lower():
                val += x + 1

    return val

if __name__ == '__main__':
    main()
