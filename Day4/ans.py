import re


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in").split("\n")

# delete the extra line
fileInput.pop(-1)


def part1(input):
    totalPoints = 0
    for line in input:
        numbers = line.split("|")
        myNumbers = numbers[0].split(":")[1]
        myNumbers = re.findall("\\d+", myNumbers)
        winningNumbers = re.findall("\\d+", numbers[1])
        points = 0
        for number in myNumbers:
            if number in winningNumbers:
                points += 1 if points == 0 else points
        totalPoints += points

    return totalPoints


def part2():
    cards = {}
    index = 0
    cards[index] = 1
    for line in fileInput:
        numbers = line.split("|")
        myNumbers = numbers[0].split(":")[1]
        myNumbers = re.findall("\\d+", myNumbers)
        winningNumbers = re.findall("\\d+", numbers[1])
        same = 0
        for number in myNumbers:
            if number in winningNumbers:
                same += 1
        for number in range(max(same, 1)):
            key = number + index + 1  # get the number of the next card
            if key >= len(fileInput):
                # break if you're at the end of cards
                break
            cards.setdefault(key, 1)
            if same > 0:
                cards[key] += cards[index]
        index += 1
    print(sum(cards.values()))
