import re
from itertools import groupby


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1():
    total = 0
    for line in fileInput.splitlines():
        pattern, numbers = line.split(" ")
        numbers = list(map(int, re.findall("\\d+", numbers)))
        pattern = [*pattern]
        total += rec(pattern, numbers)

    print(total)


def rec(pattern, numbers):
    qm = [i for i, ch in enumerate(pattern) if ch == "?"]
    res = 0
    if len(qm) > 0:
        i = pattern.index("?")
        dotPattern = pattern[:]
        dotPattern[i] = "."
        res += rec(dotPattern, numbers)
        htPattern = pattern[:]
        htPattern[i] = "#"
        res += rec(htPattern, numbers)
    else:
        groups = [sum(1 for _ in gb) for label, gb in groupby(pattern) if label == "#"]
        return 1 if groups == numbers else 0
    return res


fileInput = parseInput("input.in")
