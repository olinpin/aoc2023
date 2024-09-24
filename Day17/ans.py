from enum import Enum
from typing import List, Tuple, Dict
import heapq



class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

    def __lt__(self, other):
        if isinstance(other, Direction):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Direction):
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Direction):
            return self.value <= other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Direction):
            return self.value >= other.value
        return NotImplemented




def parseInput(file):
    with open(file, "r") as f:
        return f.read()


fileInput = parseInput("input.in")


remaining = []
shortestPath: Dict[Tuple[int, int], List[Direction]] = {}
shortestPathNum: Dict[Tuple[int, int], int] = {}

class Node:
    direction: Direction
    straight: int
    x: int
    y: int
    startX: int
    startY: int
    startDirection: Direction
    startStraight: int

    def __init__(self, direction: Direction, straight: int, x: int, y: int, startX: int, startY: int, startDirection: Direction, startStraight: int):
        self.direction = direction
        self.straight = straight
        self.x = x
        self.y = y
        self.startX = startX
        self.startY = startY
        self.startDirection = startDirection
        self.startStraight = startStraight

    def __str__(self):
        return f"{self.direction}, {self.straight}, ({self.x}, {self.y}), start: ({self.startX}, {self.startY})"



def part1():
    lines = fileInput.strip().splitlines()
    grid = [[int(num) for num in line] for line in lines]

    right = (Direction.RIGHT, 0, 1, 0, 0, 0, Direction.RIGHT, 0)
    down =  (Direction.DOWN, 0, 0, 1, 0, 0, Direction.DOWN, 0)
    heapq.heappush(remaining, (0, down))
    heapq.heappush(remaining, (0, right))

    shortestPath[(0,0, Direction.RIGHT, 0)] = []
    shortestPath[(0,0, Direction.DOWN, 0)] = []

    shortestPathNum[(0,0, Direction.RIGHT, 0)] = 0
    shortestPathNum[(0,0, Direction.DOWN, 0)] = 0

    while len(remaining) > 0:
        dijkstra(grid)

    for key in shortestPathNum.keys():
        if key[0] == len(grid)-1 and key[1] == len(grid[0])-1:
            print(key)
            pass
    print(shortestPathNum.get((len(grid)-1, len(grid[0])-1, Direction.RIGHT, True), False))
    print(shortestPathNum.get((len(grid)-1, len(grid[0])-1, Direction.RIGHT, False), False))
    print(shortestPathNum.get((len(grid)-1, len(grid[0])-1, Direction.DOWN, True), False))
    print(shortestPathNum.get((len(grid)-1, len(grid[0])-1, Direction.DOWN, False), False))



def addDirections(next, grid):
    currentCost = shortestPathNum[(next[2], next[3], next[0], next[1])]
    if next[3] == len(grid) -1 and next[2] == len(grid[0]) - 1:
        return
    if next[3] > 0 and next[0] != Direction.DOWN:
        # go up
        direction = Direction.UP
        straight = 0 if next[0] != direction else next[1] + 1
        if straight < 3:
            node = (direction, straight, next[2], next[3] - 1, next[2], next[3], next[0], next[1])
            key = (node[2], node[3], node[0], node[1])
            newCost = currentCost + grid[node[3]][node[2]]
            if key not in shortestPathNum or newCost < shortestPathNum[key]:
                heapq.heappush(remaining, (newCost, node))
    if next[3] < len(grid) - 1 and next[0] != Direction.UP:
        # go down
        direction = Direction.DOWN
        straight = 0 if next[0] != direction else next[1] + 1
        if straight < 3:
            node = (direction, straight, next[2], next[3] + 1, next[2], next[3], next[0], next[1])
            key = (node[2], node[3], node[0], node[1])
            newCost = currentCost + grid[node[3]][node[2]]
            if key not in shortestPathNum or newCost < shortestPathNum[key]:
                heapq.heappush(remaining, (newCost, node))
    if next[2] > 0 and next[0] != Direction.RIGHT:
        # go left
        direction = Direction.LEFT
        straight = 0 if next[0] != direction else next[1] + 1
        if straight < 3: 
            node = (direction, straight, next[2] - 1, next[3], next[2], next[3], next[0], next[1])
            key = (node[2], node[3], node[0], node[1])
            newCost = currentCost + grid[node[3]][node[2]]
            if key not in shortestPathNum or newCost < shortestPathNum[key]:
                heapq.heappush(remaining, (newCost, node))
    if next[2] < len(grid[0]) - 1 and next[0] != Direction.LEFT:
        # go right
        direction = Direction.RIGHT
        straight = 0 if next[0] != direction else next[1] + 1
        if straight < 3:
            node = (direction, straight, next[2] + 1, next[3], next[2], next[3], next[0], next[1])
            key = (node[2], node[3], node[0], node[1])
            newCost = currentCost + grid[node[3]][node[2]]
            if key not in shortestPathNum or newCost < shortestPathNum[key]:
                heapq.heappush(remaining, (newCost, node))


def dijkstra(grid: List[List[int]]) -> int: 
    next = heapq.heappop(remaining)[1]

    # print(next)

    currentKey = (next[2], next[3], next[0], next[1])
    previousKey = (next[4], next[5], next[6], next[7])
    if currentKey in shortestPath:
        minimum = shortestPathNum[currentKey]
        # print(minimum)
        shortest = shortestPathNum[previousKey] + grid[next[3]][next[2]]
        if minimum > shortest:
            shortestPathNum[currentKey] = shortest
            shortestPath[currentKey] = shortestPath[previousKey] + [next[0]]
            addDirections(next, grid)
    else:
        shortestPathNum[currentKey] = shortestPathNum[previousKey] + grid[next[3]][next[2]]
        shortestPath[currentKey] = shortestPath[previousKey] + [next[0]]

        addDirections(next, grid)

    return
    # save to cache


part1()
