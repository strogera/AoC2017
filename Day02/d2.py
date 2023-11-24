from itertools import permutations

with open("input.txt", "r") as inputFile:
    inp = [list(map(int, line.strip().split('\t'))) for line in inputFile.readlines()]
    print(sum(max(x) - min(x) for x in inp))
    summ2 = 0
    for line in inp:
        for x, y in permutations(line, 2):
            if x % y == 0:
                summ2 += x//y
    print(summ2)
