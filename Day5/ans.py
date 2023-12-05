import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in").split("\n")



def part1():
    seeds = re.findall("\\d+", fileInput[0])
    input = fileInput[2:]
    seedMap = {}
    used = []
    for line in input:
        mapRange = re.findall("\\d+", line)
        if len(mapRange) == 0:
            if line != '':
                used = []
            continue
        dest = int(mapRange[0])
        sourceStart = int(mapRange[1])
        length = int(mapRange[2])
        sourceEnd = sourceStart + length - 1
        for seed in seeds:
            if seed in used:
                continue
            category = seedMap.setdefault(seed, [int(seed)])[-1]
            if category >= sourceStart and category <= sourceEnd:
                seedMap[seed].append(category - sourceStart + dest)
                used.append(seed)

    l = [loc[-1] for loc in seedMap.values()]
    print(min(l))
