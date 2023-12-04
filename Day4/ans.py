import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")

# delete the extra line
input.pop(-1)


def part1():
    totalPoints = 0
    for line in input:
        numbers = line.split("|")
        myNumbers = numbers[0].split(":")[1]
        myNumbers = re.findall("\\d+", myNumbers)
        winningNumbers = re.findall("\\d+", numbers[1])
        points = 0
        for number in myNumbers:
            if number in winningNumbers:
                points += 1 if points == 0 else points
        totalPoints += points

    print(totalPoints)
