def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")


def part1():
    columns = transpose(fileInput.splitlines())
    orgColumns = []
    for i, column in enumerate(columns[:]):
        orgColumns.append([])
        oIndex = column.index("O") if "O" in column else None
        if oIndex is None:
            orgColumns[i].append(column)
            continue
        splitColumn = "".join(column).split("#")
        for j, col in enumerate(splitColumn):
            orgColumns[i].append(list(col))
            oIndex = orgColumns[i][j].index("O") if "O" in orgColumns[i][j][1:] else None
            while True:
                dotIndex = orgColumns[i][j].index(".") if "." in orgColumns[i][j] else None
                if dotIndex is None or oIndex is None:
                    break
                if oIndex > dotIndex:
                    orgColumns[i][j][oIndex] = "."
                    orgColumns[i][j][dotIndex] = "O"
                oIndex += 1
                oIndex = (oIndex + orgColumns[i][j][oIndex:].index("O")) if "O" in orgColumns[i][j][oIndex:] else None
    for i, col in enumerate(orgColumns[:]):
        orgColumns[i] = "#".join(["".join(line) for line in col])
    res = 0
    rows = transpose(orgColumns)
    for i, line in enumerate(rows):
        res += (len(rows) - i) * sum(1 for ch in line if ch == "O")
    print(res)


def rollStones(columns):
    orgColumns = []
    for i, column in enumerate(columns[:]):
        orgColumns.append([])
        oIndex = column.index("O") if "O" in column else None
        if oIndex is None:
            orgColumns[i].append(column)
            continue
        splitColumn = "".join(column).split("#")
        for j, col in enumerate(splitColumn):
            orgColumns[i].append(list(col))
            oIndex = orgColumns[i][j].index("O") if "O" in orgColumns[i][j][1:] else None
            while True:
                dotIndex = orgColumns[i][j].index(".") if "." in orgColumns[i][j] else None
                if dotIndex is None or oIndex is None:
                    break
                if oIndex > dotIndex:
                    orgColumns[i][j][oIndex] = "."
                    orgColumns[i][j][dotIndex] = "O"
                oIndex += 1
                oIndex = (oIndex + orgColumns[i][j][oIndex:].index("O")) if "O" in orgColumns[i][j][oIndex:] else None
    for i, col in enumerate(orgColumns[:]):
        orgColumns[i] = "#".join(["".join(line) for line in col])
    return orgColumns


patternCache = {}
def part2():
    columns = transpose(fileInput.splitlines())
    cycles = 1_000_000_000
    index = 0
    while True:
        if index >= cycles:
            break
        index += 1
        for i in range(4):
            if str(columns) in patternCache:
                oldIndex = patternCache[str(columns)]
                c = index - oldIndex
                amt = (cycles-index)//c
                index += amt * c
            oldColumnLayout = columns[:]
            columns = rollStones(columns)
            columns = transpose(rotate(rotate(rotate(transpose(columns)))))
            patternCache[str(oldColumnLayout)] = index

    res = 0
    rows = transpose(columns)
    for i, line in enumerate(rows):
        res += (len(rows) - i) * sum(1 for ch in line if ch == "O")
    print(res)


def strprint(lines):
    for line in lines:
        print("".join(line))
    print()


def rotate(pattern):
    newPattern = {}
    for row in pattern:
        row = [*row]
        row.reverse()
        for i, column in enumerate(row):
            if newPattern.get(i, None) is None:
                newPattern[i] = []
            newPattern[i].append(column)
    res = list(newPattern.values())
    return res


def transpose(pattern):
    newPattern = {}
    for row in pattern:
        for i, column in enumerate([*row]):
            if newPattern.get(i, None) is None:
                newPattern[i] = []
            newPattern[i].append(column)
    res = list(newPattern.values())
    return res
