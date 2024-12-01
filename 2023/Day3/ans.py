import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")


def part1():
    partNumbers = 0
    lineIndex = 0
    lastLineSymbols = []
    lastLineNumbers = []
    for line in input:
        match = re.findall("\\d+|\\.+|\\W", line)
        currentLength = 0
        currentLineSymbols = []
        currentLineNumbers = []
        for itemIndex in range(len(match)):
            item = match[itemIndex]
            currentLength += len(item)
            start = currentLength - len(item)
            end = currentLength + 1

            # check if there is a symbol on the left or right of a number
            if item.isnumeric():
                next = itemIndex > 0 and "." not in match[itemIndex-1]
                previous = itemIndex != len(match)-1 and "." not in match[itemIndex + 1]
                lastLine = checkLastLine(lastLineSymbols, start, end)
                if next or previous or lastLine:
                    partNumbers += int(item)
                    continue
                else:
                    currentLineNumbers.append((start, end, item))
            elif "." not in item:
                currentLineSymbols.append(currentLength)
                # check the numbers in last row
                for first, last, number in lastLineNumbers[:]:
                    if currentLength >= first and currentLength <= last:
                        partNumbers += int(number)
                        lastLineNumbers.remove((first, last, number))
                    if first > currentLength:
                        break

        lastLineSymbols = currentLineSymbols
        lastLineNumbers = currentLineNumbers
        lineIndex += 1
    print(partNumbers)


def checkLastLine(lastLineSymbols, start, end):
    for symbol in lastLineSymbols:
        if symbol >= start and symbol <= end:
            return True
    return False


def part2():
    lineIndex = 0
    lastLineSymbols = []
    lastLineNumbers = []
    possibleGears = {}
    for line in input:
        match = re.findall("\\d+|\\.+|\\W", line)
        currentLength = 0
        currentLineSymbols = []
        currentLineNumbers = []
        for itemIndex in range(len(match)):
            item = match[itemIndex]
            currentLength += len(item)
            start = currentLength - len(item)
            end = currentLength + 1
            # row and column of the current symbol
            tupleNumber = (lineIndex, currentLength-1)

            # check if there is a symbol on the left or right of a number
            if item.isnumeric():
                next = itemIndex > 0 and "*" in match[itemIndex-1]
                previous = itemIndex != len(match) - 1 and "*" in match[itemIndex + 1]
                for symbol in lastLineSymbols:
                    if symbol >= start and symbol <= end:
                        possibleGears.setdefault((lineIndex - 1, symbol-1), []).append(int(item))
                if next or previous:
                    if next:
                        tupleNumber = (lineIndex, start - 1)
                    else:
                        tupleNumber = (lineIndex, end - 1)
                    possibleGears.setdefault(tupleNumber, []).append(int(item))
                    continue
                else:
                    currentLineNumbers.append((start, end, item))
            elif "*" in item:
                currentLineSymbols.append(currentLength)
                # check the numbers in last row
                for first, last, number in lastLineNumbers[:]:
                    if currentLength >= first and currentLength <= last:
                        possibleGears.setdefault(tupleNumber, []).append(int(number))
                    if first > currentLength:
                        break

        lastLineSymbols = currentLineSymbols
        lastLineNumbers = currentLineNumbers
        lineIndex += 1
    gearRatios = 0
    for gear in possibleGears.values():
        if len(gear) == 2:
            gearRatios += gear[0] * gear[1]

    print(gearRatios)
