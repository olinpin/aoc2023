def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("input.in").split("\n")[:-1]

def part1():
    left, right = getBothLists(input)
    difference = 0
    for i in range(len(left)):
        difference += abs(left[i] - right[i])
    print(difference)

def part2():
    left, right = getBothLists(input)
    similarityScore = 0
    frequency = {}
    for num in right:
        frequency[num] = frequency.get(num, 0) + 1
    for num in left:
        similarityScore += num * frequency.get(num, 0)
    print(similarityScore)


def getBothLists(input):
    left = []
    right = []
    for pair in input:
        a,b = pair.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()
    return left, right
