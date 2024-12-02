def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("input.in").split("\n")[:-1]

def part1():
    safe = 0
    for report in input:
        levels = [int(a) for a in report.split()]
        allIncreasingOrDecreasing = (levels == sorted(levels) or levels == sorted(levels, reverse=True)) and len(set(levels)) == len(levels)
        if allIncreasingOrDecreasing:
            for i in range(1, len(levels)):
                diff = abs(levels[i-1] - levels[i]) 
                if  diff > 3:
                    break
            else:
                safe += 1
    print(safe)


def part2():
    safe = 0
    for report in input:
        levels = [int(a) for a in report.split()]
        sortedLevels = sorted(levels)
        reversedSortedLevels = sorted(levels, reverse=True)
        reversed = 0
        normal = 0
        for i in range(len(levels)):
            if levels[i] != sortedLevels[i]:
                normal += 1
            if levels[i] != reversedSortedLevels[i]:
                reversed += 1
        lenLevels = len(levels)
        setLen = len(set(levels))
        # either there is one mistake in the increasing/decreasing order, then there can't be duplicate numbers
        oneMistake = (normal == 2 or reversed == 2) and setLen == lenLevels
        # or there are no mistakes in the order, so there can be a duplicate
        noMistakes = (normal == 0 or reversed == 0) and setLen in [lenLevels, lenLevels-1]
        if oneMistake or noMistakes:
            i = 0
            j = 1
            correct = True
            while j < len(levels):
                diff = abs(levels[i] - levels[j])
                if diff > 3:
                    j += 1
                    if j == len(levels):
                        break
                    diff = abs(levels[i] - levels[j]) 
                    if  diff > 3:
                        correct = False
                        break
                    else:
                        i += 1
                j += 1
                i += 1
            if correct:
                safe += 1
    print(safe)
