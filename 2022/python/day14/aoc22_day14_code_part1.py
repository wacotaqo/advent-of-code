# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day14_input.txt"
#filename = "adventofcode2022_day14_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()


print(lines)
xmin = 500
xmax = 500
ymin = 0
ymax = 0
rocks = []
rocklines = []
for line in lines:
    rockline = [(int(x), int(y)) for (x,y) in [(r.split(',')) for r in line.split(' -> ')]]
    for (x,y) in rockline:
        if x < xmin: xmin = x
        if x > xmax: xmax = x
        if y < ymin: ymin = y
        if y > ymax: ymax = y
    # duplicate inner vertices
    inner = rockline[1:-1]
    inner2 = inner[:]
    rockline = [rockline[0]] + [i for sublist in list(zip(inner, inner2)) for i in sublist] + [rockline[-1]]
    # group as lines to draw later
    rockline = [(rockline[i], rockline[i+1]) for i in range(0,len(rockline)-1,2)]

    rocklines.append(rockline)

print("Max: (%s, %s) - (%s, %s)" % (xmin, ymin, xmax, ymax))
space = [['.' for x in range(xmax-xmin+2)] for x in range(ymax-ymin+1)]

for rockline in rocklines:
    #print(rockline)
    for ((fromx, fromy), (tox, toy)) in rockline:
        #print("%s, %s -> %s, %s" % (fromx, fromy, tox, toy))
        if fromx == tox:
            if fromy < toy:
                s = 1
            else:
                s = -1
            for y in range(fromy, toy+s, s):
                space[y-ymin][fromx-xmin+1] = '#'
        else: # fromy == toy
            if fromx < tox:
                s = 1
            else:
                s = -1
            for x in range(fromx, tox+s, s):
                space[fromy-ymin][x-xmin+1] = '#'

space[0][500-xmin] = '+'
for line in space:
    print(''.join(line))

FALL_DIRS = [(0,1), (-1, 1), (1, 1)]
MODE_FALL = 0
MODE_REST = 1
MODE_FALLFOREVER = 2
MODE_SANDBLOCKED = 3

sand_startx = 500-xmin+1
sand_starty = 0
sand_dropped = 0
mode = MODE_FALL
for _ in range(10000):
    sand = (sand_startx, sand_starty)
    sand_dropped += 1

    mode = MODE_FALL
    for _ in range(10000):
        fall_further = None
        for (fx, fy) in FALL_DIRS:
            newx = sand[0] + fx
            newy = sand[1] + fy
            if newy > ymax:
                print("Sand falling forever....!")
                mode = MODE_FALLFOREVER
                break
            elif space[newy][newx] == '.':
                fall_further = (newx, newy)
                break
        if mode == MODE_FALLFOREVER:
            space[sand[1]][sand[0]] = 'v'
            break
        elif not fall_further:
            mode = MODE_REST
            space[sand[1]][sand[0]] = 'o'
            break
        else:
            sand = fall_further

    if mode == MODE_FALLFOREVER:
        break

    if space[sand_starty][sand_startx] == 'o':
        print("Sand filled and cannot fall anymore!")
        mode = MODE_SANDBLOCKED
        break

for line in space:
    print(''.join(line))
print("Stopped with mode: %s" % mode)
print("Number of sand dropped: %s" % sand_dropped)
print("Number of sand filled: %s" % (sand_dropped-1))
