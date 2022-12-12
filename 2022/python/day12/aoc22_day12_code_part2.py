# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day12_input.txt"
#filename = "adventofcode2022_day12_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read()
fh.close()

SC = 'S'
EC = 'E'
lowestC = 'a'
start = ()
end = ()
mainmap = []
elevationmap = []
r = 0
alternatives = deque()
for _ in assignment_input.split('\n'):
    cols = list(_)
    ecols = list(map(lambda x: ord(x)-ord(lowestC)+1, list(_)))
    if SC in cols:
        start = (cols.index(SC), r)
        ecols[start[0]] = 1
        alternatives.append((start, 0))
    if EC in cols:
        end = (cols.index(EC), r)
        ecols[end[0]] = 26
    mainmap.append(cols)
    elevationmap.append(ecols)
    r += 1

for r in mainmap:
    print(r)
print()
for r in elevationmap:
    print(r)
print()

already_been = set()
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
maxR = len(mainmap)
maxC = len(mainmap[0])

# For the hike, add all 'a's as starting points. 'a' has elevation 1
for r in range(maxR):
    for c in range(maxC):
        if elevationmap[r][c] == 1 and (r, c) != start:
            alternatives.append(((c, r), 0))

while alternatives:
    ((col, row), steps) = alternatives.popleft()
    # Different ways to end
    if (col, row) == end:
        print("Steps to destination: %s" % steps)
        break
    if (col, row) in already_been:
        continue
    already_been.add((col, row))

    # Try each direction
    for (dirC, dirR) in DIRS:
        nextC = col + dirC
        nextR = row + dirR
        if nextC >= 0 and nextC < maxC and nextR >= 0 and nextR < maxR and elevationmap[nextR][nextC] - elevationmap[row][col] <= 1:
            alternatives.append(((nextC, nextR), steps+1))
