import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1():
    lines = inputFile.split("\n")
    allNums = 0
    for line in lines:
        data = re.findall("[-]?\\d+", line)
        if len(data) == 0:
            continue
        data = list(map(int, data))
        iters = [data]
        while not all(num == 0 for num in iters[-1]):
            data = [data[i+1] - data[i] for i in range(len(data)-1)]
            iters.append(data)
        allNums += sum([num[-1] for num in iters])
    print(allNums)


inputFile = parseInput("input.in")
