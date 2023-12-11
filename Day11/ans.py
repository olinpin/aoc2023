def parseInput(file):
    with open(file, "r") as f:
        return f.read()


def part1():
    lines = fileInput.splitlines()
    lines = [[*line] for line in lines]
    emptyCols = [*range(len(lines))]
    for index in range(len(lines)):
        line = lines[index]
        if "#" in line:
            i = -1
            for _ in range(line.count("#")):
                i = line.index("#", i+1)
                if i in emptyCols:
                    emptyCols.remove(i)

    count = 0
    for i in emptyCols:
        for index in range(len(lines)):
            lines[index].insert(i+count, ".")
        count += 1

    duplicateRows = []
    for i in range(len(lines)):
        line = lines[i]
        if "#" not in line:
            duplicateRows.append(i)
    count = 0
    for i in duplicateRows:
        lines.insert(i + count, lines[i + count])
        count += 1

    # shortest path
    hashtags = []
    for row in range(len(lines)):
        line = lines[row]
        if "#" not in line:
            continue
        i = -1
        for _ in range(line.count("#")):
            i = line.index("#", i+1)
            hashtags.append((row, i))

    length = 0
    count = 1
    for coord1 in hashtags:
        for coord2 in hashtags[count:]:
            x = abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])
            length += x
        count += 1

    print(length)


fileInput = parseInput("input.in")
