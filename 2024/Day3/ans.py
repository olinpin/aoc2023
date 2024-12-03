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

def part1oneline():
    print(sum([int(a) * int(b) for line in input for a,b in re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)]))

def part2():
    res = 0
    multiply = True
    for line in input:
        search = re.findall("(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", line)
        for do, dont, a, b in search:
            if do != '':
                multiply = True
            if dont != '':
                multiply = False
            if multiply and a != '' and b != '':
                res += int(a) * int(b)
    print(res)
