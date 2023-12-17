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


def part2():
    lines = fileInput.strip().splitlines()
    for line in lines:
        energized.append(["." for _ in line])
        grid.append([*line])
    maxTotal = 0
    for y in range(len(grid)):
        for x in (0, len(grid[0])-1):
            energized.clear()
            cache.clear()
            for line in lines:
                energized.append(["." for _ in line])
            addLight(x, y, "right")
            total = 0
            for line in energized:
                total += sum(1 for ch in line if ch == "#")
            maxTotal = max(total, maxTotal)

    for x in range(len(grid[0])):
        for y in (0, len(grid)-1):
            energized.clear()
            cache.clear()
            for line in lines:
                energized.append(["." for _ in line])
            addLight(x, y, "down")
            total = 0
            for line in energized:
                total += sum(1 for ch in line if ch == "#")
            maxTotal = max(total, maxTotal)
    print(maxTotal)


def strprint(lines):
    for line in lines:
        print("".join(line))
    print()


cache = {}
def addLight(x, y, direction="right"):

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
                    addLight(x, y, "up")
                    addLight(x, y, "down")
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
                    addLight(x, y, "up")
                    addLight(x, y, "down")
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
                    addLight(x, y, "left")
                    addLight(x, y, "right")
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
                    addLight(x, y, "left")
                    addLight(x, y, "right")
                    return
            else:
                return
