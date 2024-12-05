import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")[:-1]

def part1():
    allOrdering, _, _ = getOrderingAndRules(input)
    sum = 0
    for order in allOrdering:
        mid = int((len(order) - 1) / 2)
        sum += order[mid]
    print(sum)


def part2():
    _, rules, unOrdered = getOrderingAndRules(input)
    i = 0
    while i < len(unOrdered):
        ordering = unOrdered[i]
        previous = []
        for j in range(len(ordering)):
            intersection =  [x for x in rules.get(int(ordering[j]), set([])) if x in previous]
            if intersection != []:
                newI = ordering.index(intersection[0])
                value = ordering.pop(j)
                ordering.insert(newI, value)
                break
            previous.append(ordering[j])
        else:
            unOrdered[i] = previous
            i += 1
    sum = 0
    for order in unOrdered:
        mid = int((len(order) - 1) / 2)
        sum += order[mid]
    print(sum)


def getOrderingAndRules(input):
    rules = {}
    ordering = False
    allOrdering = []
    unOrdered = []
    for i in input:
        if i == '':
            ordering = True
            continue
        if not ordering:
            rule = re.findall('(\d+)\|(\d+)', i)
            for r in rule:
                rules[int(r[0])] = rules.get(int(r[0]), set([])) | set([int(r[1])])
        if ordering:
            orders = []
            for pageNumber in i.split(','):
                orders.append(int(pageNumber))
                intersection =  [x for x in rules.get(int(pageNumber), set([])) if x in orders]
                if intersection != []:
                    unOrdered.append([int(x) for x in i.split(',')])
                    break
            else:
                allOrdering.append(orders)
    return allOrdering, rules, unOrdered
