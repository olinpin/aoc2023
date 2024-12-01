def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part(part2=False):
    patterns = fileInput.split("\n\n")
    res = 0
    for pattern in patterns:
        splitted = pattern.split("\n")
        trans = transpose(pattern)
        if part2:
            rows = findDuplicatesPart2(splitted)
            columns = findDuplicatesPart2(trans)
        else:
            rows = findDuplicates(splitted)
            columns = findDuplicates(trans)
        res += max(100 * rows, columns)
    print(res)


def findDuplicatesPart2(splitted):
    for index in range(len(splitted)):
        bottomHalf = splitted[index:]
        topHalf = splitted[:index]
        topHalf.reverse()

        discrepencies = 0
        for upper, lower in zip(topHalf, bottomHalf):
            for upper_char, lower_char in zip(upper, lower):
                if upper_char != lower_char:
                    discrepencies += 1
                if discrepencies > 1:
                    break
            if discrepencies > 1:
                break
        if discrepencies == 1:
            return index
    return 0


def findDuplicates(splitted):
    if splitted[-1] == "":
        splitted.remove("")
    for index, line in enumerate(splitted):
        # start at the second line
        if index == 0:
            continue
        if line == splitted[index-1]:
            possibleMatch = index
            i = 0
            while index + i < len(splitted) and (index - i - 1) >= 0:
                if splitted[index + i] != splitted[index - i - 1]:
                    break
                i += 1
            else:
                return possibleMatch
    return 0


def transpose(pattern):
    pattern = pattern.split("\n")
    newPattern = {}
    for row in pattern:
        for i, column in enumerate([*row]):
            if newPattern.get(i, None) is None:
                newPattern[i] = []
            newPattern[i].append(column)

    return list(newPattern.values())


def strprint(lines):
    for line in lines:
        print("".join(line))


fileInput = parseInput("input.in")

part(True)
