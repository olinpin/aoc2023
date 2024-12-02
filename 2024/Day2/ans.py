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


part1()
