import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")


def part1():
    sequences = fileInput.strip().split(",")
    total = 0
    for sequence in sequences:
        total += findHash(sequence)
    print(total)


def findHash(sequence):
    sequenceTotal = 0
    for character in [*sequence]:
        sequenceTotal += ord(character)
        sequenceTotal *= 17
        sequenceTotal %= 256
    return sequenceTotal


def part2():
    boxes = {}
    sequences = fileInput.strip().split(",")
    for sequence in sequences:
        match = re.findall("(\\w+)(=|-)(\\d+)?", sequence)[0]
        boxNumber = findHash(match[0])
        if boxNumber not in boxes:
            boxes[boxNumber] = []
        if match[1] == "-":
            for i, box in enumerate(boxes[boxNumber]):
                label = box[0]
                if match[0] == label:
                    boxes[boxNumber].pop(i)
                    break
        else:
            for i, box in enumerate(boxes[boxNumber]):
                label = box[0]
                if match[0] == label:
                    boxes[boxNumber][i] = (match[0], int(match[2]))
                    break
            else:
                boxes[boxNumber].append((match[0], int(match[2])))
    total = 0
    for boxNumber in boxes.keys():
        for i, lens in enumerate(boxes[boxNumber]):
            lensTotal = 1 + boxNumber
            lensTotal *= i + 1
            lensTotal *= lens[1]
            total += lensTotal
    print(total)
