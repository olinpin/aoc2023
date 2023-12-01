import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split()

sum = 0
for line in input:
    match = re.findall("\\d", line)
    first = match[0]
    last = match[-1]
    if first and last:
        num = str(first) + str(last)
        sum += int(num)
    else:
        break

print(sum)
