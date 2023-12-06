import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")
fileInput = fileInput.split("\n")



def possible(time, distance):
    possibilities = 0
    for x in range(time):
        if distance < (time-x)*x:
            possibilities += 1
    return possibilities


def part1():
    times = list(map(int, re.findall("\\d+", fileInput[0])))
    distances = list(map(int, re.findall("\\d+", fileInput[1])))
    races = zip(times, distances)

    total = []
    for t, d in races:
        possibilities = possible(t, d)
        total.append(possibilities)

    res = total[0]
    for x in total[1:]:
        res *= x
    print(res)
