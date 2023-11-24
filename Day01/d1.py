with open("input.txt", "r") as inputFile:
    inp = list(map(int, inputFile.read().strip()))
    summ, summ2 = 0, 0
    step = len(inp)//2
    for i in range(len(inp)):
        if inp[i] == inp[(i + 1)%len(inp)]:
            summ += inp[i]
        if inp[i] == inp[(i + step)%len(inp)]:
            summ2 += inp[i]

    print(summ)
    print(summ2)