import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("input.in").split("\n")[:-1]

def part1():
    res = 0
    for line in input:
        search = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
        for a, b in search:
            res += int(a) * int(b)
    print(res)
