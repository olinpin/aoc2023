import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()

def strprint(lines):
    for line in lines:
        print("".join(line))

fileInput = parseInput("example.in")

hexToDecDict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

def hexToInt(hex):
    letters = list(hex)
    num = 0
    for i, letter in enumerate(letters):
        num += hexToDecDict[letter] * (15**i)
    return num

def part2():
    lines = fileInput.strip().splitlines()
    instructions = []
    hexInstructions = []
    for line in lines:
        match = re.findall('#(.*)\)', line)[0]
        dir = int(match[-1])
        if dir == 0:
            hexInstructions.append(('R', match[:5]))
        if dir == 1:
            hexInstructions.append(('D', match[:5]))
        if dir == 2:
            hexInstructions.append(('L', match[:5]))
        if dir == 3:
            hexInstructions.append(('U', match[:5]))

    for instruction in hexInstructions:
        instructions.append((instruction[0], hexToInt(instruction[1])))
    print(instructions)
    # print(instructions)
    dig(instructions)%


def part1():
    lines = fileInput.strip().splitlines()
    instructions = []
    for line in lines:
        match = re.findall('([RULD]).(\d+)', line)[0]
        instructions.append((match[0], int(match[1])))
    # print(instructions)
    dig(instructions)

def dig(instructions):
    hole = [["#"]]

    currentX = 0
    currentY = 0
    # dig trench
    for direction, depth in instructions:
        if direction == "R":
            # make sure we have enough space
            if currentX + depth >= len(hole[0]):
                for row in hole:
                    row.extend(["."] * (currentX + depth + 1 - len(row)))

            for _ in range(depth):
                currentX += 1
                hole[currentY][currentX] = "#"
        elif direction == "L":
            if currentX - depth < 0:
                for row in hole:
                    for _ in range(depth - currentX):
                        row.insert(0, ".")
                currentX = depth

            for _ in range(depth):
                currentX -= 1
                hole[currentY][currentX] = "#"
        elif direction == "U":
            if currentY - depth < 0:
                for _ in range(depth - currentY):
                    hole.insert(0, ["."] * len(hole[0]))

                currentY = depth
            for _ in range(depth):
                currentY -= 1
                hole[currentY][currentX] = "#"
        elif direction == "D":
            # make sure we have enough space
            if currentY + depth > len(hole)-1:
                for _ in range(len(hole)-1, currentY + depth):
                    hole.append(["." for _ in hole[0]])

            for _ in range(depth):
                currentY += 1
                hole[currentY][currentX] = "#"

    # strprint(hole)
    # dig the hole inside the trench
    # for i, y in enumerate(hole):
    #     for j, x in enumerate(y):
    #         if hole[i][j] == ".":
    #             hole[i][j] = "O"
    #         else:
    #             break
    # for i, y in enumerate(hole):
    #     for j, x in enumerate(y):
    #         if hole[i][len(y)-1-j] == ".":
    #             hole[i][len(y)-1-j] = "O"
    #         else:
    #             break
    #
    # for i, x in enumerate(hole[0]):
    #     for j, y in enumerate(hole):
    #         if hole[j][i] == "." or hole[j][i] == "O":
    #             hole[j][i] = "O"
    #         else:
    #             break
    #
    # for i, x in enumerate(hole[0]):
    #     for j, y in enumerate(hole):
    #         if hole[-1-j][i] == "." or hole[j][i] == "O":
    #             hole[-1-j][i] = "O"
    #         else:
    #             break
    coordsLeft = []
    # first fill
    coordsLeft = coordsLeft + [(0, i) for i in range(len(hole))]
    coordsLeft = coordsLeft + [(len(hole[0])-1, i) for i in range(len(hole))]
    coordsLeft = coordsLeft + [(i, 0) for i in range(len(hole[0]))]
    coordsLeft = coordsLeft + [(i, len(hole)-1) for i in range(len(hole[0]))]
    # print(coordsLeft)
    # print(len(hole), len(hole[0]))
    coordExplored = []
    while coordsLeft != []:
        # print(coordsLeft)
        coord = coordsLeft.pop()
        x = coord[0]
        y = coord[1]
        # print(x, y)
        if hole[y][x] == ".":
            hole[y][x] = "O"
        else:
            continue
        if x-1 >=0:
            c = (x-1, y)
            if hole[y][x-1] not in ("O", "#"):
                coordsLeft.append(c)
        if x+1 < len(hole[0]):
            c = (x+1, y)
            if hole[y][x+1] not in ("O", "#"):
                coordsLeft.append(c)
        if y-1 >=0:
            c = (x, y-1)
            if hole[y-1][x] not in ("O", "#"):
                coordsLeft.append(c)
        if y+1 < len(hole):
            c = (x, y+1)
            if hole[y+1][x] not in ("O", "#"):
                coordsLeft.append(c)

    # print()
    # strprint(hole)
    # for i, row in enumerate(hole):
    #     for j, col in enumerate(row):
    #         if hole[i][j] == ".":
    #             hole[i][j] = "#"

    result = 0
    for row in hole:
        result += row.count("#")
        result += row.count(".")
    print(result)



part2()
