import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")


def part1():
    possible = 0
    for line in input:
        line = line.split(": ")
        if len(line) == 1:
            continue
        id = int(line[0].split()[1])
        line = line[1].split("; ")
        possible += isGamePossible(id, line)

    print(possible)


def isGamePossible(gameID, line):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    for cubes in line:
        match = re.findall("(\\d+) (\\w+)", cubes)
        for num, col in match:
            num = int(num)
            if col == "red":
                if num > maxRed:
                    return 0
            elif col == "green":
                if num > maxGreen:
                    return 0
            elif col == "blue":
                if num > maxBlue:
                    return 0
    return gameID


def part2():
    power = 0
    for line in input:
        line = line.split(": ")
        if len(line) == 1:
            continue
        line = line[1].split("; ")
        power += fewestPossible(line)

    print(power)


def fewestPossible(line):
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for cubes in line:
        match = re.findall("(\\d+) (\\w+)", cubes)
        for num, col in match:
            num = int(num)
            if col == "red":
                maxRed = max(maxRed, num)
            elif col == "green":
                maxGreen = max(maxGreen, num)
            elif col == "blue":
                maxBlue = max(maxBlue, num)
    power = maxRed * maxBlue * maxGreen
    return power
