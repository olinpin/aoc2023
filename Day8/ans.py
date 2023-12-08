import re
from math import lcm


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1():
    wasteland = {}
    for line in lines.split("\n"):
        match = re.findall("\\w+", line)
        if len(match) == 0:
            continue
        wasteland[match[0]] = (match[1], match[2])
    next = "AAA"
    end = "ZZZ"
    index = 0
    while next != end:
        currIndex = index % len(instructions)
        i = 1 if instructions[currIndex] == "R" else 0
        next = wasteland[next][i]
        index += 1
    print(index)


def part2():
    wasteland = {}
    nexts = []
    ends = []
    for line in lines.split("\n"):
        match = re.findall("\\w+", line)
        aMatch = re.findall("..A ", line)
        zMatch = re.findall("..Z ", line)
        if len(match) == 0:
            continue
        wasteland[match[0]] = (match[1], match[2])
        if len(aMatch) > 0:
            nexts.append(match[0])
        elif len(zMatch) > 0:
            ends.append(match[0])
    endLength = len(ends)
    index = 0
    match = False
    doneBy = {}

    while not match:
        newNexts = []
        currIndex = index % len(instructions)
        i = 1 if instructions[currIndex] == "R" else 0
        for next in nexts:
            place = wasteland[next][i]
            if place in ends:
                doneBy[place] = index + 1
            else:
                newNexts.append(place)
        match = len(doneBy.keys()) == endLength
        nexts = newNexts
        index += 1
    print(lcm(*list(doneBy.values())))


fileInput = parseInput("input.in")
instructions, lines = fileInput.split("\n\n")
