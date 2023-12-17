def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")


energized = []
grid = []
def part1():
    lines = fileInput.strip().splitlines()
    for line in lines:
        energized.append(["." for _ in line])
        grid.append([*line])
    addLight(0, 0)
    total = 0
    for line in energized:
        total += sum(1 for ch in line if ch == "#")
    print(total)


def strprint(lines):
    for line in lines:
        print("".join(line))


cache = {}
def addLight(x, y, split=0, direction="right"):
    if (x, y, direction) in cache:
        return
    cache[(x, y, direction)] = True
    energized[y][x] = "#"
    while True:
        if direction == "right":
            for _ in range(x, len(grid[0]) - 1):
                x += 1
                energized[y][x] = "#"
                if grid[y][x] == "/":
                    direction = "up"
                    break
                elif grid[y][x] == "\\":
                    direction = "down"
                    break
                elif grid[y][x] == "|":
                    addLight(x, y, split+1, "up")
                    addLight(x, y, split+1, "down")
                    return
            else:
                return
        elif direction == "left":
            for _ in range(x):
                x -= 1
                energized[y][x] = "#"
                if grid[y][x] == "/":
                    direction = "down"
                    break
                elif grid[y][x] == "\\":
                    direction = "up"
                    break
                elif grid[y][x] == "|":
                    addLight(x, y, split+1, "up")
                    addLight(x, y, split+1, "down")
                    return
            else:
                return
        elif direction == "down":
            for _ in range(y, len(grid)-1):
                y += 1
                energized[y][x] = "#"
                if grid[y][x] == "/":
                    direction = "left"
                    break
                elif grid[y][x] == "\\":
                    direction = "right"
                    break
                elif grid[y][x] == "-":
                    addLight(x, y, split+1, "left")
                    addLight(x, y, split+1, "right")
                    return
            else:
                return
        elif direction == "up":
            for _ in range(y):
                y -= 1
                energized[y][x] = "#"
                if grid[y][x] == "/":
                    direction = "right"
                    break
                elif grid[y][x] == "\\":
                    direction = "left"
                    break
                elif grid[y][x] == "-":
                    addLight(x, y, split+1, "left")
                    addLight(x, y, split+1, "right")
                    return
            else:
                return
