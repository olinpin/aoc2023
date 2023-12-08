import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


class WastelandMap:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.name} = [{self.left}, {self.right}]"


fileInput = parseInput("input.in")


def part1():
    instructions, lines = fileInput.split("\n\n")
    wasteland = []
    for line in lines.split("\n"):
        match = re.findall("\\w+", line)
        if len(match) == 0:
            continue
        wasteland.append(WastelandMap(match[0], match[1], match[2]))
    next = "AAA"
    end = "ZZZ"
    index = 0
    while next != end:
        for w in wasteland:
            if w.name == next:
                currIndex = index % len(instructions)
                if instructions[currIndex] == "R":
                    next = w.right
                    break
                else:
                    next = w.left
                    break
        index += 1
    print(index)
