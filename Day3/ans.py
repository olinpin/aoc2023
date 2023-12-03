import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")
# input = parseInput("example2.in").split("\n")


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
