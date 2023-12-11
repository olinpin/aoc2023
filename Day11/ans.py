def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part(part2=False):
    lines = fileInput.splitlines()
    lines = [[*line] for line in lines]
    emptyCols = [*range(len(lines))]

    # get empty columns
    for index in range(len(lines)):
        line = lines[index]
        if "#" in line:
            i = -1
            for _ in range(line.count("#")):
                i = line.index("#", i+1)
                if i in emptyCols:
                    emptyCols.remove(i)

    # get empty rows
    emptyRows = []
    for i in range(len(lines)):
        line = lines[i]
        if "#" not in line:
            emptyRows.append(i)

    # shortest path
    hashtags = []
    increase = 1
    if part2:
        increase = 1_000_000 - 1
    for row in range(len(lines)):
        line = lines[row]
        if "#" not in line:
            continue
        i = -1
        for _ in range(line.count("#")):
            i = line.index("#", i+1)
            newRow = sum([int(row > num) for num in emptyRows]) * increase + row
            newI = sum([int(i > num) for num in emptyCols]) * increase + i
            hashtags.append((newRow, newI))

    length = 0
    count = 1
    for coord1 in hashtags:
        for coord2 in hashtags[count:]:
            x = abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])
            length += x
        count += 1

    print(length)


fileInput = parseInput("input.in")
part()
