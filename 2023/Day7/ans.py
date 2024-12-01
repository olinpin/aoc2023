import re
from functools import cmp_to_key


def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")

pokerTypes = {
        "FiveKind": 7,
        "FourKind": 6,
        "FullHouse": 5,
        "ThreeKind": 4,
        "TwoPair": 3,
        "OnePair": 2,
        "HighCard": 1
        }
cardsPart1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cardsPart1.reverse()

cardsPart2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cardsPart2.reverse()


def compareCardsPart1(x, y):
    if x[2] == y[2]:
        xHand = x[0]
        yHand = y[0]
        for i in range(len(xHand)):
            if xHand[i] == yHand[i]:
                continue
            else:
                return cardsPart1.index(xHand[i]) - cardsPart1.index(yHand[i])
    return x[2] - y[2]


def part1():
    match = re.findall("([\\d\\w]+) (\\d+)", fileInput)
    game = []
    for hand, bid in match:
        diffCards = set(list(hand))
        numberOfDiffCards = len(diffCards)
        if numberOfDiffCards == 1:
            game.append([hand, bid, pokerTypes["FiveKind"]])
        elif numberOfDiffCards == 2:
            occurences = hand.count(list(diffCards)[0])
            if occurences in [4, 1]:
                game.append([hand, bid, pokerTypes["FourKind"]])
            else:
                game.append([hand, bid, pokerTypes["FullHouse"]])
        elif numberOfDiffCards == 3:
            occurences1 = hand.count(list(diffCards)[0])
            occurences2 = hand.count(list(diffCards)[1])
            if occurences1 == 2 or occurences2 == 2:
                game.append([hand, bid, pokerTypes["TwoPair"]])
            else:
                game.append([hand, bid, pokerTypes["ThreeKind"]])
        elif numberOfDiffCards == 4:
            game.append([hand, bid, pokerTypes["OnePair"]])
        else:
            game.append([hand, bid, pokerTypes["HighCard"]])

    sortedGame = sorted(game, key=cmp_to_key(compareCardsPart1))

    res = 0
    for index in range(len(sortedGame)):
        res += (index + 1) * int(sortedGame[index][1])
    print(res)


def compareCardsPart2(x, y):
    if x[2] == y[2]:
        xHand = x[0]
        yHand = y[0]
        for i in range(len(xHand)):
            if xHand[i] == yHand[i]:
                continue
            else:
                return cardsPart2.index(xHand[i]) - cardsPart2.index(yHand[i])
    return x[2] - y[2]


def part2():
    match = re.findall("([\\d\\w]+) (\\d+)", fileInput)
    game = []
    for hand, bid in match:
        diffCards = set(list(hand))
        numberOfDiffCards = len(diffCards)
        if "J" in diffCards and numberOfDiffCards != 1:
            numberOfDiffCards -= 1
        Js = hand.count("J")
        if "J" in diffCards:
            diffCards = list(diffCards)
            diffCards.remove("J")
        if numberOfDiffCards == 1:
            game.append([hand, bid, pokerTypes["FiveKind"]])
        elif numberOfDiffCards == 2:
            occurences1 = hand.count(list(diffCards)[0]) + Js
            occurences2 = hand.count(list(diffCards)[1]) + Js
            if occurences1 == 4 or occurences2 == 4:
                game.append([hand, bid, pokerTypes["FourKind"]])
            else:
                game.append([hand, bid, pokerTypes["FullHouse"]])
        elif numberOfDiffCards == 3:
            occurences1 = hand.count(list(diffCards)[0]) + Js
            occurences2 = hand.count(list(diffCards)[1]) + Js
            occurences3 = hand.count(list(diffCards)[2]) + Js
            if occurences1 == 3 or occurences2 == 3 or occurences3 == 3:
                game.append([hand, bid, pokerTypes["ThreeKind"]])
            else:
                game.append([hand, bid, pokerTypes["TwoPair"]])
        elif numberOfDiffCards == 4:
            game.append([hand, bid, pokerTypes["OnePair"]])
        else:
            game.append([hand, bid, pokerTypes["HighCard"]])

    sortedGame = sorted(game, key=cmp_to_key(compareCardsPart2))

    res = 0
    for index in range(len(sortedGame)):
        res += (index + 1) * int(sortedGame[index][1])
    print(res)
