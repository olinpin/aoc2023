from typing import List, Callable, Optional, Tuple


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")[:-1]


def part1():
    matrix = [list(i) for i in input]
    found = 0
    directions = [
        down,
        up,
        left,
        right,
        topRight,
        topLeft,
        bottomRight,
        bottomLeft,
    ]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            for direction in directions:
                found += int(search(direction, x, y, matrix))
    print(found)


def part2():
    matrix = [list(i) for i in input]
    found = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            found += int(search2(x, y, matrix))
    print(found)


def search(
    updateCoords: Callable[[int, int], Tuple[int, int]],
    x: int,
    y: int,
    matrix: List[List[str]],
) -> bool:
    if checkCoord("X", x, y, matrix):
        x, y = updateCoords(x, y)
        if checkCoord("M", x, y, matrix):
            x, y = updateCoords(x, y)
            if checkCoord("A", x, y, matrix):
                x, y = updateCoords(x, y)
                return checkCoord("S", x, y, matrix)
    return False


def search2(x: int, y: int, matrix: List[List[str]]) -> bool:
    if checkCoord("A", x, y, matrix):
        tLeftX, tLeftY = topLeft(x, y)
        tRightX, tRightY = topRight(x, y)
        bLeftX, bLeftY = bottomLeft(x, y)
        bRightX, bRightY = bottomRight(x, y)
        cross1 = set(
            [getCoord(tLeftX, tLeftY, matrix), getCoord(bRightX, bRightY, matrix)]
        )
        cross2 = set(
            [getCoord(tRightX, tRightY, matrix), getCoord(bLeftX, bLeftY, matrix)]
        )
        return cross1 == set(["S", "M"]) and cross1 == cross2
    return False


def down(x: int, y: int) -> Tuple[int, int]:
    return (x + 1, y)


def up(x: int, y: int) -> Tuple[int, int]:
    return (x - 1, y)


def left(x: int, y: int) -> Tuple[int, int]:
    return (x, y - 1)


def right(x: int, y: int) -> Tuple[int, int]:
    return (x, y + 1)


def topRight(x: int, y: int) -> Tuple[int, int]:
    return (x - 1, y + 1)


def topLeft(x: int, y: int) -> Tuple[int, int]:
    return (x - 1, y - 1)


def bottomRight(x: int, y: int) -> Tuple[int, int]:
    return (x + 1, y + 1)


def bottomLeft(x: int, y: int) -> Tuple[int, int]:
    return (x + 1, y - 1)


def checkCoord(letter: str, x: int, y: int, matrix: List[List[str]]) -> bool:
    return validCoordinates(x, y, matrix) and matrix[x][y] == letter


def getCoord(x: int, y: int, matrix: List[List[str]]) -> Optional[str]:
    return matrix[x][y] if validCoordinates(x, y, matrix) else None


def validCoordinates(x: int, y: int, matrix: List[List[str]]) -> bool:
    return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[x])
