# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day15_input.txt"
check_row_y = 2000000
#filename = "adventofcode2022_day15_input_test.txt"
#check_row_y = 10

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

print(lines)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def print_grid(grid):
    output = []
    for row_chars in grid:
        print(''.join(row_chars))

xmin = xmax = ymin = ymax = 0
bx_on_check_row = set()
sensors = []
for line in lines:
    parts = [p1 for subline in line.split(':') for p1 in subline.split() if '=' in p1]
    parts = [int(p2[1].replace(',', '')) for p2 in [p1.split('=') for p1 in parts]]
    (sx, sy), (bx, by) = (parts[0], parts[1]), (parts[2], parts[3])
    if sensors == []:
        xmin = xmax = sx
        ymin = ymax = sy
    if min([sx, bx]) < xmin: xmin = min([sx, bx])
    if min([sy, by]) < ymin: ymin = min([sy, by])
    if max([sx, bx]) > xmax: xmax = max([sx, bx])
    if max([sy, by]) > ymax: ymax = max([sy, by])
    if by == check_row_y:
        bx_on_check_row.add(bx)
    sensors.append(((sx, sy), (bx, by), manhattan_distance(sx, sy, bx, by)))

print("Max: (%s, %s) - (%s, %s)" % (xmin, ymin, xmax, ymax))
print("Number of sensors: %s" % len(sensors))
print("Row to check: %s" % check_row_y)
print("Beacons on the 'check row': %s" % len(bx_on_check_row))

check_row = set()
for ((sx, sy), (bx, by), d) in sensors:
    if check_row_y-d <= sy and check_row_y+d >= sy:
        for x in range(-int(1e7), int(1e7)):
            dm = manhattan_distance(sx, sy, x, check_row_y)
            if dm <= d:
                if not (x in bx_on_check_row):
                    check_row.add(x)

print("Number of positions on row %s where a beacon cannot be: %s" % (check_row_y, len(check_row)))



