from typing import List, Callable, Tuple
def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("input.in").split("\n")[:-1]

def part1():
    matrix = [list(i) for i in input]
    found = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            found += int(search(down, x, y, matrix))
            found += int(search(up, x, y, matrix))
            found += int(search(left, x, y, matrix))
            found += int(search(right, x, y, matrix))
            found += int(search(topRight, x, y, matrix))
            found += int(search(topLeft, x, y, matrix))
            found += int(search(bottomRight, x, y, matrix))
            found += int(search(bottomLeft, x, y, matrix))
    print(found)

def search(updateCoords: Callable[[int, int], Tuple[int,int]], x: int, y: int, matrix: List[List[str]]) -> bool:
    if checkCoord("X", x, y, matrix):
        x, y = updateCoords(x, y)
        if checkCoord("M", x, y, matrix):
            x, y = updateCoords(x, y)
            if checkCoord("A", x, y, matrix):
                x, y = updateCoords(x, y)
                return checkCoord("S", x, y, matrix)
    return False

def down(x: int, y: int) -> Tuple[int, int]:
    return (x+1, y)

def up(x: int, y: int) -> Tuple[int, int]:
    return (x-1, y)

def left(x: int, y: int) -> Tuple[int, int]:
    return (x, y-1)

def right(x: int, y: int) -> Tuple[int, int]:
    return (x, y+1)

def topRight(x: int, y: int) -> Tuple[int, int]:
    return (x-1, y+1)

def topLeft(x: int, y: int) -> Tuple[int, int]:
    return (x-1, y-1)

def bottomRight(x: int, y: int) -> Tuple[int, int]:
    return (x+1, y+1)

def bottomLeft(x: int, y: int) -> Tuple[int, int]:
    return (x+1, y-1)

def checkCoord(letter: str, x: int, y: int, matrix: List[List[str]]) -> bool:
    return validCoordinates(x, y, matrix) and matrix[x][y] == letter

def validCoordinates(x: int, y: int, matrix: List[List[str]]) -> bool:
    return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[x])
