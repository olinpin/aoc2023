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
    while row < len(field):
        if not started:
            if "S" in field[row]:
                started = True
                column = field[row].index("S")
                current = row * len(field) + column
                if field[row-1][column] in ("|", "7", "F"):
                    row -= 1
                elif field[row+1][column] in ("L", "J"):
                    row += 1
                elif field[row][column-1] == "-":
                    column -= 1
                last = current
            else:
                row += 1
                continue

        current = row * len(field) + column
        currentSymbol = field[row][column]
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


inputFile = parseInput("input.in")
