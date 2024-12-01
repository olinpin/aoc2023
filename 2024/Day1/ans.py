def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("input.in").split("\n")[:-1]

def part1():
    left = []
    right = []
    for pair in input:
        a,b = pair.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()
    difference = 0
    for i in range(len(left)):
        difference += abs(left[i] - right[i])
    print(difference)

def part2():
    left = []
    right = []
    for pair in input:
        a,b = pair.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()

    similarityScore = 0
    frequency = {}
    for num in right:
        f = frequency.get(num, 0) + 1
        frequency[num] = f
    for num in left:
        similarityScore += num * frequency.get(num, 0)
    print(similarityScore)
