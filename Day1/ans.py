import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split()

def part1():
    sum = 0
    for line in input:
        match = re.findall("\\d", line)
        first = match[0]
        last = match[-1]
        if first and last:
            num = str(first) + str(last)
            sum += int(num)
        else:
            break

    print(sum)

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def part2():
    sum = 0
    for line in input:
        match = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\\d))", line)
        first = match[0]
        last = match[-1]
        if not first.isnumeric():
            first = digits.index(first)
        if not last.isnumeric():
            last = digits.index(last)
        if first and last:
            num = f"{first}{last}"
            sum += int(num)
        else:
            print("breaking")
            break
    print(sum)

