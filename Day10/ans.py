import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1():
    field = inputFile.splitlines()
    # print(field)
    started = False
    row = 0
    column = 0
    last = None
    step = 1
    field = [list(row) for row in field]
    while row < len(field):
        if not started:
            if "S" in field[row]:
                started = True
                column = field[row].index("S")
                current = row * len(field) + column
                if row != 0 and field[row-1][column] in ("|", "7", "F"):
                    row -= 1
                elif (row+1) != len(field) and field[row+1][column] in ("|", "L", "J"):
                    row += 1
                elif column != 0 and field[row][column-1] in ("-",):
                    column -= 1
                last = current
            else:
                row += 1
                continue

        current = row * len(field) + column
        currentSymbol = field[row][column]
        field[row][column] = "X"
        if currentSymbol == "S":
            break
        elif currentSymbol == "|":
            row += 1 if last == (row-1) * len(field) + column else -1
        elif currentSymbol == "-":
            if last == row * len(field) + column+1:
                column -= 1
            else:
                column += 1
        elif currentSymbol == "L":
            if last == row * len(field) + column+1:
                row -= 1
            else:
                column += 1
        elif currentSymbol == "J":
            if last == (row-1) * len(field) + column:
                column -= 1
            else:
                row -= 1
        elif currentSymbol == "7":
            if last == (row+1) * len(field) + column:
                column -= 1
            else:
                row += 1
        elif currentSymbol == "F":
            if last == (row+1) * len(field) + column:
                column += 1
            else:
                row += 1
        step += 1
        last = current

    print(int(step / 2))
    res = ""
    for x in field[:]:
        res += "".join(x) + "\n"
    print(res)


def part2():
    field = inputFile.splitlines()
    started = False
    row = 0
    column = 0
    last = None
    step = 1
    field = [list(row) for row in field]
    path = []
    while row < len(field):
        if not started:
            if "S" in field[row]:
                started = True
                column = field[row].index("S")
                current = row * len(field) + column
                path.append((row, column))
                if row != 0 and field[row-1][column] in ("|", "7", "F"):
                    row -= 1
                elif (row+1) != len(field) and field[row+1][column] in ("|", "L", "J"):
                    row += 1
                elif column != 0 and field[row][column-1] in ("-",):
                    column -= 1
                last = current
            else:
                row += 1
                continue

        current = row * len(field) + column
        currentSymbol = field[row][column]
        field[row][column] = "X"
        path.append((row, column))
        if currentSymbol == "S":
            break
        elif currentSymbol == "|":
            row += 1 if last == (row-1) * len(field) + column else -1
        elif currentSymbol == "-":
            if last == row * len(field) + column+1:
                column -= 1
            else:
                column += 1
        elif currentSymbol == "L":
            if last == row * len(field) + column+1:
                row -= 1
            else:
                column += 1
        elif currentSymbol == "J":
            if last == (row-1) * len(field) + column:
                column -= 1
            else:
                row -= 1
        elif currentSymbol == "7":
            if last == (row+1) * len(field) + column:
                column -= 1
            else:
                row += 1
        elif currentSymbol == "F":
            if last == (row+1) * len(field) + column:
                column += 1
            else:
                row += 1
        step += 1
        last = current
    # print(int(step / 2))

    # for i in range(len(field)):
    #     for j in range(len(field[0])):
    #         # field != . ??? Is that wrong?
    #         if ((i, j) not in path) and (field[i][j] != "." or i in (0, len(field)-1) or j in (0, len(field[0])-1)):
    #             field[i][j] = "*"

    insides1 = []
    partialInsides = []
    for row in range(len(field)):
        partialInsides = []
        inPath = False
        for column in range(len(field[0])):
            if (row, column) in path:
                insides1 += partialInsides
                partialInsides = []
                if (row, column+1) in path or (row, column-1) not in path:
                    inPath = False
                    continue
                else:
                    inPath = True
                # print(row, column, "Set ", inPath)
                # insides += currentInsides
                # for r, c in currentInsides:
                #     field[r][c] = "I"
                # currentInsides = []
            elif field[row][column] == ".":
                if inPath:
                    insides1.append((row, column))
                    # field[row][column] = "I"
            # elif (row, column) not in path:
            #     if inPath:
            #         field[row][column] = "X"
            #     else:
            #         field[row][column] = "Y"
            # else:
            #     field[row][column] = "O"



    insides2 = []
    for column in range(len(field[0])):
        inPath = False
        partialInsides = []
        for row in range(len(field)):
            if (row, column) in path:
                insides2 += partialInsides
                partialInsides = []
                if (row+1, column) in path or (row-1, column) not in path:
                    inPath = False
                    continue
                else:
                    inPath = True
                # print(row, column, "Set ", inPath)
                # insides += currentInsides
                # for r, c in currentInsides:
                #     field[r][c] = "I"
                # currentInsides = []
            elif field[row][column] == ".":
                if inPath:
                    partialInsides.append((row, column))
                    # field[row][column] = "I"
            # elif (row, column) not in path:
            #     if inPath:
                    # field[row][column] = "X"
            #     else:
            #         field[row][column] = "Y"
            # else:
            #     field[row][column] = "O"
    # print(insides1)
    # print(len(insides1))
    # print(insides2)
    # print(len(insides2))
    # print(list(set(insides1) & set(insides2)))
    print(len(list(set(insides1) & set(insides2))))
    for row, column in list(set(insides1) & set(insides2)):
        field[row][column] = "I"

    res = ""
    for x in field[:]:
        res += "".join(x) + "\n"
    print(res)


inputFile = parseInput("input.in")
inputFile = parseInput("example4.in")

part2()
