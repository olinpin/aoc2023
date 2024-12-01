import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1(lines):
    total = 0
    for line in lines:
        pattern, numbers = line.split(" ")
        numbers = list(map(int, re.findall("\\d+", numbers)))
        pattern = [*pattern]
        total += rec(pattern, numbers)

    print(total)


cache = {}
def rec(pattern, numbers):
    key = (pattern, numbers)
    if key in cache:
        return cache[key]
    if pattern == "":
        return int(numbers == ())
    if numbers == ():
        return int("#" not in pattern)

    res = 0
    if pattern[0] in ".?":
        res += rec(pattern[1:], numbers)
    if pattern[0] in "#?":
        if numbers[0] <= len(pattern):
            if "." not in pattern[:numbers[0]]:
                if numbers[0] == len(pattern) or pattern[numbers[0]] != "#":
                    res += rec(pattern[numbers[0]+1:], numbers[1:])
    cache[key] = res
    return res


def part2():
    total = 0
    for line in fileInput.splitlines():
        pattern, numbers = line.split()
        numbers = tuple(map(int, re.findall("\\d+", numbers)))
        pattern = "?".join([pattern] * 5)
        numbers *= 5
        total += rec(pattern, numbers)
    print(total)


fileInput = parseInput("input.in")
