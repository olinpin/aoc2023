import sys

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("example.in")


def part1():
    lines = fileInput.strip().splitlines()
    grid = [[*line] for line in lines]
    print(grid)
    x, y = 0, 0
    shortest = shortestPath(x, y, grid)
    print(shortest)


cache = {}
def shortestPath(x, y, grid, straight=0, direction="R"):
    if (x, y) in cache:
        return cache[(x, y)]
    destX, destY = (len(grid), len(grid[0]))
    
    shortests = []
    if (x, y) != (destX, destY):
        # create new shortPath
        if (x < destX and direction != "L"):
            possibleShortest = None
            if direction == "R":
                if straight != 3:
                    possibleShortest = shortestPath(x+1, y, grid, straight+1, "R")

            else:
                possibleShortest = shortestPath(x+1, y, grid, straight, "R")
            if possibleShortest is not None:
                shortests.append(possibleShortest)
        if (y < destY and direction != "U"):
            possibleShortest = None
            if direction == "D":
                if straight != 3:
                    possibleShortest = shortestPath(x, y+1, grid, straight+1, "D")

            else:
                possibleShortest = shortestPath(x, y+1, grid, straight, "D")
            if possibleShortest is not None:
                shortests.append(possibleShortest)
        # same for the other cases

    shortests.sort()
    print(shortests)
    return int(grid[x][y]) + (shortests[0] if len(shortests) > 0 else 0)




part1()
