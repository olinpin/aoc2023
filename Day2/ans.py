import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")

# input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")


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
