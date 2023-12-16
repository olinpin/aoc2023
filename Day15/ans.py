def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")


def part1():
    sequences = fileInput.strip().split(",")
    total = 0
    for sequence in sequences:
        sequenceTotal = 0
        for character in [*sequence]:
            sequenceTotal += ord(character)
            sequenceTotal *= 17
            sequenceTotal %= 256
        total += sequenceTotal
    print(total)
