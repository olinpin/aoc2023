import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()



def part1(seeds):
    seedMap = {}
    used = []
    for line in fileInput:
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

    print(min([loc[-1] for loc in seedMap.values()]))


def part2():
    i = 0
    seedRanges = []
    while int(len(seedsPart1)/2) > i:
        seedRanges.append(range(seedsPart1[i*2], seedsPart1[i*2] + seedsPart1[i*2+1]))
        i += 1

    for group in fileInput[1:]:
        lines = group.split("\n")[1:]
        lines.pop(-1)
        # get the ranges and delete the first line (the one with the title of the map)
        mapRange = [[int(x) for x in re.findall("\\d+", line)] for line in lines]
        # create the transformation ranges
        ranges = [(range(destStart, destStart + length), range(sourceStart, sourceStart + length)) for destStart, sourceStart, length in mapRange]
        newSeedRanges = []
        for seedRange in seedRanges:
            skipped = False
            for sourceRange, destRange in ranges:
                if seedRange.stop <= destRange.start or destRange.stop <= seedRange.start:
                    skipped = True
                    continue
                offset = sourceRange.start - destRange.start
                intersection = range(max(destRange.start, seedRange.start), min(seedRange.stop, destRange.stop))
                splitRange1 = range(seedRange.start, intersection.start)
                splitRange2 = range(intersection.stop, seedRange.stop)
                if splitRange1.start < splitRange1.stop:
                    # append if it's a valid range
                    seedRanges.append(splitRange1)
                if splitRange2.start < splitRange2.stop:
                    # append if it's a valid range
                    seedRanges.append(splitRange2)
                newSeedRanges.append(range(intersection.start + offset, intersection.stop + offset))
                skipped = False
                break
            if skipped:
                newSeedRanges.append(seedRange)
        seedRanges = newSeedRanges
    print(min([seedRange.start for seedRange in seedRanges]))  # get the min start


fileInput = parseInput("input.in").split("\n")

seedsPart1 = list(map(int, re.findall("\\d+", fileInput[0])))
fileInput = fileInput[2:]

part1(seedsPart1)

fileInput = parseInput("input.in").split("\n\n")

part2()
