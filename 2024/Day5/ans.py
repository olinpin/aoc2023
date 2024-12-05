import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")[:-1]

def part1():
    print(input)
    rules = {}
    ordering = False
    allOrdering = []
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
                    break
            else:
                allOrdering.append(orders)
    sum = 0
    for order in allOrdering:
        mid = int((len(order) - 1) / 2)
        sum += order[mid]
    print(sum)
