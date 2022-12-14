# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2021_day25_input.txt"
#filename = "adventofcode2021_day25_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

print(lines)

grid = [list(line) for line in lines]
maxR = len(grid)
maxC = len(grid[0])

steps = 0
print(steps)
for line in grid:
    print(''.join(line))

loop = True
while loop:
    step_moves = 0
    # move each > cucumber east
    move_queue = []
    for r in range(maxR):
        for c in range(maxC):
            nextC = c+1
            if nextC == maxC: nextC = 0
            if grid[r][c] == '>' and grid[r][nextC] == '.':
                move_queue.append(((c, r), (nextC, r)))
    for ((c, r), (nextC, nextR)) in move_queue:
        grid[r][c] = '.'
        grid[nextR][nextC] = '>'
    step_moves += len(move_queue)
    # move each v cucumber south
    move_queue = []
    for r in range(maxR):
        for c in range(maxC):
            nextR = r+1
            if nextR == maxR: nextR = 0
            if grid[r][c] == 'v' and grid[nextR][c] == '.':
                move_queue.append(((c, r), (c, nextR)))
    for ((c, r), (nextC, nextR)) in move_queue:
        grid[r][c] = '.'
        grid[nextR][nextC] = 'v'
    step_moves += len(move_queue)

    steps += 1
    """
    if steps  in (1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 55, 56, 57, 58, 59):
        print(steps)
        for line in grid:
            print(''.join(line))
        print("Moves: %s" % step_moves)
    """

    if step_moves == 0:
        loop = False

print("Steps before stopping: %s" % steps)