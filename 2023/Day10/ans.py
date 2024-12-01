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

    s = "7" # I don't have the energy to do this automatically
    row = 0
    while row < len(field):
        if "S" in field[row]:
            field[row][field[row].index("S")] = s
            break
        row += 1

    insides = []
    for row in range(len(field)):
        for column in range(len(field[0])):
            if (row, column) in path:
                continue

            x, y = row, column
            pipes = 0
            while x < len(field) and y < len(field[0]):
                if (x, y) in path and field[x][y] not in ("7", "L"):
                    pipes += 1
                x += 1
                y += 1

            if pipes % 2 == 1:
                insides.append((row, column))

    print(len(insides))


inputFile = parseInput("input.in")
